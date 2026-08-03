"""NotebookLM ノートブックからソース一覧（タイトル+URL）を抽出する。"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from .auth import with_browser
from .config_loader import load_config
from .notebooklm import NotebookLMClient


def extract_sources(config_path: Path | None = None) -> list[dict[str, str]]:
    config = load_config(config_path)
    results: list[dict[str, str]] = []

    with with_browser(config) as (_, __, page):
        client = NotebookLMClient(page, config)
        client.ensure_notebook(config.notebook_name)
        page.wait_for_timeout(3000)

        # ソース行からタイトルと YouTube URL を拾う
        rows = page.locator(".single-source-container, [class*='single-source']")
        count = rows.count()
        print(f"ソース行: {count} 件")

        for i in range(count):
            row = rows.nth(i)
            try:
                title = row.inner_text(timeout=3000).strip().split("\n")[0].strip()
                title = re.sub(r"^(check|video_youtube)\s*", "", title).strip()
            except Exception:
                title = f"source_{i+1}"

            url = ""
            for link in row.locator("a[href*='youtube'], a[href*='youtu.be']").all():
                href = link.get_attribute("href") or ""
                if "youtube" in href or "youtu.be" in href:
                    url = href
                    break

            if not url:
                # 行の HTML から video id を探す
                html = row.inner_html()
                m = re.search(r"watch\?v=([a-zA-Z0-9_-]{11})", html)
                if m:
                    url = f"https://www.youtube.com/watch?v={m.group(1)}"

            if title and url:
                results.append({"title": title, "url": url})
                print(f"  {len(results):03d}: {title[:50]} | {url}")

        if not results:
            # ページ全体から YouTube URL を抽出（フォールバック）
            content = page.content()
            ids = re.findall(r"watch\?v=([a-zA-Z0-9_-]{11})", content)
            seen: set[str] = set()
            for vid in ids:
                if vid in seen:
                    continue
                seen.add(vid)
                results.append({
                    "title": f"video_{vid}",
                    "url": f"https://www.youtube.com/watch?v={vid}",
                })
            print(f"フォールバック: {len(results)} 件の video id を検出")

        client.screenshot("extract_sources")

    return results


def write_urls_file(config_path: Path | None, sources: list[dict[str, str]]) -> Path:
    config = load_config(config_path)
    lines = [f"{s['title']}|{s['url']}" for s in sources]
    config.urls_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"書き込み: {config.urls_file} ({len(lines)} 行)")
    return config.urls_file


def main() -> int:
    config_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    sources = extract_sources(config_path)
    if not sources:
        print("ソースを取得できませんでした", file=sys.stderr)
        return 1
    out = write_urls_file(config_path, sources)
    dump = load_config(config_path).state_dir / "extracted_sources.json"
    dump.write_text(json.dumps(sources, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON: {dump}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
