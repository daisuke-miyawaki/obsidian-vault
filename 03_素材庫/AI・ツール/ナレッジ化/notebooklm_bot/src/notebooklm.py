from __future__ import annotations

import json
import time

from playwright.sync_api import Locator, Page, TimeoutError as PlaywrightTimeout

from .config_loader import AppConfig
from .exceptions import RateLimitError
from . import selectors as sel


class NotebookLMClient:
    def __init__(self, page: Page, config: AppConfig) -> None:
        self.page = page
        self.config = config
        self.config.screenshots_dir.mkdir(parents=True, exist_ok=True)

    def screenshot(self, name: str) -> None:
        path = self.config.screenshots_dir / f"{name}.png"
        try:
            self.page.screenshot(path=str(path), full_page=True)
            print(f"  スクリーンショット: {path}")
        except Exception as exc:
            print(f"  スクリーンショット取得スキップ: {exc}")

    def _is_notebook_page(self) -> bool:
        return "/notebook/" in self.page.url

    def _wait_for_notebook_page(self, timeout_ms: int = 60_000) -> None:
        deadline = time.time() + timeout_ms / 1000
        while time.time() < deadline:
            if self._is_notebook_page():
                self.page.wait_for_timeout(1500)
                return
            self.page.wait_for_timeout(500)
        raise RuntimeError(
            f"ノートブック画面に入れませんでした（現在URL: {self.page.url}）"
        )

    def _click_first_selector(self, selectors: list[str], timeout: int = 8000) -> bool:
        for selector in selectors:
            try:
                loc = self.page.locator(selector).first
                if loc.count() == 0:
                    continue
                loc.wait_for(state="visible", timeout=timeout)
                loc.click(timeout=timeout)
                return True
            except (PlaywrightTimeout, Exception):
                continue
        return False

    def _click_first_text(self, texts: list[str], timeout: int = 5000) -> bool:
        for text in texts:
            for getter in (
                lambda t=text: self.page.get_by_role("button", name=t, exact=False),
                lambda t=text: self.page.get_by_text(t, exact=False),
            ):
                try:
                    loc = getter().first
                    if loc.count() == 0:
                        continue
                    loc.click(timeout=timeout)
                    return True
                except (PlaywrightTimeout, Exception):
                    continue
        return False

    def _fill_first_selector(self, selectors: list[str], value: str) -> Locator:
        for selector in selectors:
            try:
                loc = self.page.locator(selector).first
                if loc.count() == 0:
                    continue
                loc.wait_for(state="visible", timeout=5000)
                loc.click()
                loc.fill(value)
                return loc
            except (PlaywrightTimeout, Exception):
                continue
        raise RuntimeError("URL入力欄が見つかりません")

    def _count_sources(self) -> int:
        total = 0
        for selector in sel.SOURCE_ROW_SELECTORS:
            count = self.page.locator(selector).count()
            if count > 0:
                return count
        return total

    def _debug_buttons(self) -> str:
        buttons = self.page.locator("button")
        info = []
        for i in range(min(buttons.count(), 25)):
            btn = buttons.nth(i)
            try:
                info.append(
                    {
                        "i": i,
                        "aria": btn.get_attribute("aria-label"),
                        "text": btn.inner_text(timeout=500)[:80],
                        "visible": btn.is_visible(),
                    }
                )
            except Exception:
                pass
        payload = {
            "url": self.page.url,
            "title": self.page.title(),
            "is_notebook_page": self._is_notebook_page(),
            "buttons": info,
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    def _abs_url(self, href: str) -> str:
        if href.startswith("http"):
            return href
        if href.startswith("/"):
            return "https://notebooklm.google.com" + href
        return self.config.base_url.rstrip("/") + "/" + href.lstrip("/")

    def open_home(self) -> None:
        self.page.goto(self.config.base_url, wait_until="domcontentloaded", timeout=120_000)
        self.page.wait_for_timeout(2500)

    def open_notebook(self) -> None:
        url_file = self.config.notebook_url_file
        if url_file.exists():
            url = url_file.read_text(encoding="utf-8").strip()
            if url and "/notebook/" in url:
                self.page.goto(self._abs_url(url), wait_until="domcontentloaded", timeout=120_000)
                self.page.wait_for_timeout(2000)
                if self._is_notebook_page():
                    return
        self.ensure_notebook(self.config.notebook_name)

    def ensure_notebook(self, name: str) -> None:
        self.open_home()
        self.page.wait_for_load_state("networkidle", timeout=60_000)

        # Open existing notebook by title on home
        try:
            card = self.page.locator("mat-card, a[href*='/notebook/']").filter(has_text=name).first
            if card.count() > 0 and card.is_visible():
                card.click(timeout=8000)
                self._wait_for_notebook_page()
                self._save_notebook_url()
                print(f"  既存ノートブックを開きました: {self.page.url}")
                return
        except (PlaywrightTimeout, Exception):
            pass

        # Create new notebook (Japanese UI: ノートブックを新規作成)
        if not self._click_first_selector(sel.CREATE_NOTEBOOK_SELECTORS):
            if not self._click_first_text(sel.CREATE_NOTEBOOK_TEXTS):
                self.screenshot("create_notebook_fail")
                raise RuntimeError(
                    "「ノートブックを新規作成」ボタンが見つかりません\n"
                    + self._debug_buttons()
                )

        self._wait_for_notebook_page()
        self._save_notebook_url()
        print(f"  ノートブックを開きました: {self.page.url}")

    def _is_add_source_dialog_open(self) -> bool:
        return self.page.locator("mat-dialog-container").count() > 0

    def _save_notebook_url(self) -> None:
        if not self._is_notebook_page():
            return
        self.config.notebook_url_file.parent.mkdir(parents=True, exist_ok=True)
        clean_url = self.page.url.split("?")[0]
        self.config.notebook_url_file.write_text(clean_url, encoding="utf-8")

    def _open_add_source_dialog(self) -> None:
        if not self._is_notebook_page():
            self.ensure_notebook(self.config.notebook_name)

        if self._is_add_source_dialog_open():
            return

        if self._click_first_selector(sel.ADD_SOURCE_SELECTORS):
            self.page.wait_for_timeout(1200)
            if self._is_add_source_dialog_open():
                return

        # Open add-source dialog via URL flag (avoids backdrop blocking the button)
        base = self.page.url.split("?")[0]
        if "/notebook/" in base:
            self.page.goto(base + "?addSource=true", wait_until="domcontentloaded", timeout=60_000)
            self.page.wait_for_timeout(2500)
            if self._is_add_source_dialog_open():
                return

        self.screenshot("add_source_button_fail")
        raise RuntimeError(
            "「ソースを追加」ダイアログを開けません\n" + self._debug_buttons()
        )

    def _fill_url_in_dialog(self, url: str) -> None:
        dialog = self.page.locator("mat-dialog-container")
        for selector in sel.URL_INPUT_SELECTORS:
            loc = dialog.locator(selector).first
            if loc.count() == 0:
                continue
            loc.wait_for(state="visible", timeout=5000)
            loc.click()
            loc.fill(url)
            self.page.wait_for_timeout(800)
            insert = dialog.locator("button:has-text('挿入'), button:has-text('Insert')").first
            if insert.count() > 0 and insert.is_enabled():
                insert.click()
            else:
                loc.press("Enter")
            return
        raise RuntimeError("URL入力欄が見つかりません")

    def add_youtube_urls(self, urls: list[str]) -> None:
        self.open_notebook()
        if not self._is_notebook_page():
            self.ensure_notebook(self.config.notebook_name)
        for url in urls:
            if self._source_url_exists(url):
                print(f"  ソース済みスキップ: {url}")
                continue
            self._add_single_youtube_url(url)

    def _source_url_exists(self, url: str) -> bool:
        # YouTube video id で既存ソースを確認
        video_id = url.split("v=")[-1].split("&")[0]
        body = self.page.locator("body").inner_text()
        return video_id in body and "video_youtube" in self.page.content()

    def _add_single_youtube_url(self, url: str) -> None:
        before_count = self._count_sources()
        self._open_add_source_dialog()

        # 2026 JP UI: YouTube URL は「ウェブサイト」タブから追加
        dialog = self.page.locator("mat-dialog-container")
        clicked = False
        for text in sel.WEBSITE_TAB_TEXTS:
            btn = dialog.get_by_role("button", name=text, exact=False)
            if btn.count() > 0:
                btn.first.click(timeout=5000)
                clicked = True
                break
        if not clicked:
            if not self._click_first_selector(sel.WEBSITE_SOURCE_SELECTORS):
                if not self._click_first_selector(sel.YOUTUBE_SOURCE_SELECTORS):
                    self.screenshot("website_tab_fail")
                    raise RuntimeError("「ウェブサイト」タブが見つかりません")

        self.page.wait_for_timeout(1000)
        self._fill_url_in_dialog(url)
        self._wait_for_source_added(before_count)
        print(f"  ソース追加完了: {url}")

    def _wait_for_source_added(self, before_count: int) -> None:
        deadline = time.time() + self.config.source_index_timeout_sec
        while time.time() < deadline:
            self.page.wait_for_timeout(1500)
            after = self._count_sources()
            if after > before_count:
                self.page.wait_for_timeout(2000)
                return
            loading = self.page.locator("[role='progressbar'], mat-spinner, .loading")
            if loading.count() == 0:
                # Dialog closed — assume added even if count unchanged
                dialog = self.page.locator("mat-dialog-container")
                if dialog.count() == 0:
                    self.page.wait_for_timeout(2000)
                    return
        self.page.wait_for_timeout(2000)

    def _find_chat_input(self) -> Locator:
        chat = self.page.locator("textarea[aria-label='クエリボックス']").first
        if chat.count() > 0 and chat.is_visible():
            return chat
        for selector in sel.CHAT_INPUT_SELECTORS:
            loc = self.page.locator(selector)
            if loc.count() > 0:
                candidate = loc.last
                if candidate.is_visible():
                    return candidate
        raise RuntimeError("チャット入力欄が見つかりません")

    def _title_match_keys(self, title: str, source_url: str | None = None) -> list[str]:
        keys: list[str] = []
        for n in (12, 15, 20, 25):
            keys.append(title[:n])
        for marker in ("isaさん⑰", "isaさん⑯", "isaさん⑮", "isaさん⑭", "isaさん⑬",
                       "isaさん⑫", "isaさん⑪", "isaさん⑩", "isaさん⑨", "isaさん⑧",
                       "isaさん⑦", "isaさん⑥", "isaさん⑤", "isaさん④", "isaさん③",
                       "isaさん②", "isaさん①", "最終話"):
            if marker in title:
                keys.append(marker)
        if source_url and "v=" in source_url:
            keys.append(source_url.split("v=")[-1].split("&")[0])
        return [k for k in keys if k]

    def _find_source_row_index(self, title: str, source_url: str | None = None) -> int | None:
        keys = self._title_match_keys(title, source_url)
        rows = self.page.locator(", ".join(sel.SOURCE_ROW_SELECTORS))
        count = rows.count()
        for i in range(count):
            try:
                text = rows.nth(i).inner_text(timeout=2000)
            except Exception:
                continue
            if any(key in text for key in keys):
                return i

        # フォールバック: ソース一覧のテキスト全体から部分一致
        for key in keys:
            if len(key) < 8:
                continue
            hit = self.page.get_by_text(key, exact=False)
            if hit.count() > 0:
                for j in range(hit.count()):
                    try:
                        row = hit.nth(j).locator("xpath=ancestor::*[contains(@class,'single-source')][1]")
                        if row.count() > 0:
                            for i in range(count):
                                if rows.nth(i).inner_text(timeout=1000) == row.first.inner_text(timeout=1000):
                                    return i
                    except Exception:
                        continue
        return None

    def select_only_source(self, title: str, source_url: str | None = None) -> None:
        """対象動画だけを有効にし、他ソースは除外する（NotebookLMは外す＝EXCLUDE）。"""
        self.open_notebook()
        self.page.wait_for_timeout(1500)
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(300)

        # まず全ソースを有効化
        for label in sel.SELECT_ALL_CHECKBOX_TEXTS:
            cb = self.page.get_by_role("checkbox", name=label)
            if cb.count() > 0:
                try:
                    if not cb.is_checked():
                        cb.click()
                        self.page.wait_for_timeout(1000)
                except Exception:
                    pass
                break

        rows = self.page.locator(", ".join(sel.SOURCE_ROW_SELECTORS))
        count = rows.count()
        target_idx = self._find_source_row_index(title, source_url)

        if target_idx is None:
            self.screenshot("select_source_fail")
            raise RuntimeError(f"ソース行が見つかりません: {title[:50]}")

        for i in range(count):
            row = rows.nth(i)
            checkbox = row.locator("mat-checkbox, input[type='checkbox']").first
            if checkbox.count() == 0:
                continue
            want_checked = i == target_idx
            try:
                checked = checkbox.is_checked()
            except Exception:
                checked = True
            if checked != want_checked:
                checkbox.click()
                self.page.wait_for_timeout(400)

        self.page.wait_for_timeout(800)
        print(f"  ソース単独選択: {title[:45]}...")

    def _reset_chat(self) -> None:
        """チャット履歴が長いとNotebookLMが拒否するため、ページを再読み込みしてリセット。"""
        if not self._is_notebook_page():
            self.open_notebook()
        self.page.reload(wait_until="domcontentloaded", timeout=120_000)
        self.page.wait_for_timeout(2500)

    def _start_new_chat(self) -> None:
        """質問前に空のチャットスレッドへ切り替える（履歴蓄積による拒否を防ぐ）。"""
        if not self._is_notebook_page():
            self.open_notebook()

        if self._click_first_selector(sel.NEW_CHAT_SELECTORS, timeout=5000):
            self.page.wait_for_timeout(2000)
            print("  新しいチャットを開始")
            return
        if self._click_first_text(sel.NEW_CHAT_TEXTS, timeout=5000):
            self.page.wait_for_timeout(2000)
            print("  新しいチャットを開始")
            return

        if self._click_first_selector(sel.CHAT_OPTIONS_SELECTORS, timeout=5000):
            self.page.wait_for_timeout(800)
            if self._click_first_text(sel.CHAT_MENU_NEW_TEXTS, timeout=3000):
                self.page.wait_for_timeout(2000)
                print("  メニューから新しいチャット")
                return
            if self._click_first_text(sel.CHAT_MENU_CLEAR_TEXTS, timeout=3000):
                self.page.wait_for_timeout(1000)
                confirm = self.page.get_by_role("button", name="削除", exact=True)
                if confirm.count() > 0 and confirm.first.is_visible():
                    confirm.first.click(timeout=5000)
                    self.page.wait_for_timeout(2500)
                print("  チャット履歴を削除")
                return
            self.page.keyboard.press("Escape")
            self.page.wait_for_timeout(300)

        if self._count_model_responses() > 0:
            self._reset_chat()
            print("  チャットをリセット（ページ再読み込み）")

    def _is_refusal_response(self, text: str) -> bool:
        refusal_markers = (
            "答えられません",
            "cannot answer this question",
            "rephrase your question",
            "別の質問をしてみてください",
        )
        return any(m in text for m in refusal_markers)

    def _is_rate_limit_response(self, text: str) -> bool:
        limit_markers = (
            "1日の上限",
            "daily limit",
            "現在、回答できません",
            "現在回答できません",
        )
        return any(m in text for m in limit_markers)

    def ask(self, prompt: str, *, source_title: str | None = None, source_url: str | None = None) -> str:
        self.open_notebook()
        if not self._is_notebook_page():
            self.ensure_notebook(self.config.notebook_name)

        self._start_new_chat()

        if source_title:
            self.select_only_source(source_title, source_url)

        # Close add-source dialog if still open
        if self._is_add_source_dialog_open():
            close = self.page.locator("button[aria-label='閉じる'], button:has-text('close')").first
            if close.count() > 0:
                close.click()
                self.page.wait_for_timeout(1000)

        before = self._count_model_responses()
        chat = self._find_chat_input()
        chat.click()
        chat.fill(prompt)
        self.page.wait_for_timeout(500)

        send = self.page.locator("button.submit-button[aria-label='送信']").last
        if send.count() > 0:
            try:
                send.wait_for(state="visible", timeout=5000)
                for _ in range(20):
                    if send.is_enabled():
                        send.click()
                        break
                    self.page.wait_for_timeout(300)
                else:
                    chat.press("Enter")
            except Exception:
                chat.press("Enter")
        elif not self._click_first_selector(sel.SEND_BUTTON_SELECTORS):
            chat.press("Enter")

        return self._wait_for_new_response(before)

    def _count_model_responses(self) -> int:
        loc = self.page.locator(".to-user-container")
        if loc.count() > 0:
            return loc.count()
        return self._count_chat_turns()

    def _is_generating(self) -> bool:
        for selector in sel.GENERATING_STOP_SELECTORS:
            loc = self.page.locator(selector)
            if loc.count() > 0 and loc.first.is_visible():
                return True
        return False

    def _count_chat_turns(self) -> int:
        for selector in sel.RESPONSE_CONTAINER_SELECTORS:
            loc = self.page.locator(selector)
            if loc.count() > 0:
                return loc.count()
        return 0

    def _wait_for_new_response(self, previous_count: int) -> str:
        deadline = time.time() + self.config.reply_timeout_sec
        last_text = ""
        stable_ticks = 0

        while time.time() < deadline:
            current_count = self._count_model_responses()
            text = self._extract_latest_response_text()
            generating = self._is_generating()

            if (
                text
                and self._is_rate_limit_response(text)
                and not generating
            ):
                self.screenshot("response_rate_limit")
                raise RateLimitError(
                    "NotebookLM の1日のチャット上限に達しました。明日以降に再開するか、プランをアップグレードしてください。"
                )

            if (
                text
                and self._is_refusal_response(text)
                and not generating
                and current_count > previous_count
            ):
                self.screenshot("response_refusal")
                raise RuntimeError("NotebookLM が質問を拒否しました（チャット履歴またはプロンプト）")

            if current_count > previous_count and text:
                if generating:
                    last_text = text
                    stable_ticks = 0
                elif text != last_text:
                    last_text = text
                    stable_ticks = 0
                else:
                    stable_ticks += 1
                    if stable_ticks >= 2 and len(text) > 200:
                        return text.strip()
                last_text = text
            elif text and len(text) > 200 and not generating:
                # 既存回答の取りこぼし防止
                stable_ticks += 1
                last_text = text
                if stable_ticks >= 2:
                    return text.strip()

            self.page.wait_for_timeout(2000)

        if last_text and len(last_text) > 200:
            if self._is_refusal_response(last_text):
                self.screenshot("response_refusal")
                raise RuntimeError("NotebookLM が質問を拒否しました（チャット履歴またはプロンプト）")
            return last_text.strip()
        self.screenshot("response_timeout")
        raise RuntimeError("NotebookLM から回答を取得できませんでした")

    def _extract_latest_response_text(self) -> str:
        for selector in sel.RESPONSE_CONTAINER_SELECTORS:
            loc = self.page.locator(selector)
            if loc.count() > 0:
                return loc.last.inner_text()
        pair = self.page.locator(sel.CHAT_PAIR_SELECTOR).last
        if pair.count() > 0:
            to_user = pair.locator(".to-user-container")
            if to_user.count() > 0:
                return to_user.first.inner_text()
        return ""
