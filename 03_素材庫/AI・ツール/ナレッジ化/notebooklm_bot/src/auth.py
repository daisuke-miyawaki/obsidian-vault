from __future__ import annotations

import signal
import subprocess
import time
from pathlib import Path

from playwright.sync_api import BrowserContext, Playwright, sync_playwright

from .config_loader import AppConfig


def _release_stale_browser_lock(profile_dir: Path) -> None:
    """前回の Playwright Chrome が残っていると起動できないため、終了してロックを外す。"""
    import os
    import subprocess

    marker = "notebooklm_bot/state/browser_profile"
    try:
        out = subprocess.check_output(["pgrep", "-f", marker], text=True)
        for line in out.strip().splitlines():
            if not line.strip().isdigit():
                continue
            pid = int(line.strip())
            try:
                os.kill(pid, signal.SIGTERM)
                print(f"  古いブラウザプロセスを終了: pid={pid}")
            except ProcessLookupError:
                pass
            except PermissionError:
                print(f"  警告: pid={pid} を終了できませんでした")
    except subprocess.CalledProcessError:
        pass

    time.sleep(2)

    for name in ("SingletonLock", "SingletonSocket", "SingletonCookie"):
        path = profile_dir / name
        try:
            if path.exists() or path.is_symlink():
                path.unlink()
        except OSError:
            pass


def launch_persistent_context(
    playwright: Playwright,
    config: AppConfig,
) -> BrowserContext:
    config.profile_dir.mkdir(parents=True, exist_ok=True)
    _release_stale_browser_lock(config.profile_dir)
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=str(config.profile_dir),
        headless=config.headless,
        locale="ja-JP",
        viewport={"width": 1400, "height": 900},
        args=["--disable-blink-features=AutomationControlled"],
    )
    return context


def interactive_login(config: AppConfig) -> None:
    """Open NotebookLM and wait until the user finishes Google login."""
    with sync_playwright() as playwright:
        context = launch_persistent_context(playwright, config)
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(config.base_url, wait_until="domcontentloaded", timeout=120_000)
        print("\n=== NotebookLM ログイン ===")
        print("1. ブラウザで Google アカウントにログインしてください")
        print("2. NotebookLM のホーム画面が表示されたら、このターミナルで Enter を押してください\n")
        input("ログイン完了後 Enter ... ")
        context.storage_state(path=str(config.state_dir / "storage_state.json"))
        print(f"セッションを保存しました: {config.profile_dir}")
        context.close()


def with_browser(config: AppConfig):
    """Context manager yielding (playwright, context, page)."""

    class _BrowserSession:
        def __enter__(self):
            self._playwright = sync_playwright().start()
            self.context = launch_persistent_context(self._playwright, config)
            self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
            return self._playwright, self.context, self.page

        def __exit__(self, exc_type, exc, tb):
            try:
                self.context.close()
            finally:
                self._playwright.stop()

    return _BrowserSession()
