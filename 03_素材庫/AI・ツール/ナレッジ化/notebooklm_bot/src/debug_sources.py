"""ソース行のHTMLをダンプする診断用。"""
from __future__ import annotations

import json

from .auth import with_browser
from .config_loader import load_config
from .notebooklm import NotebookLMClient
from . import selectors as sel


def main() -> None:
    config = load_config()
    rows_data = []

    with with_browser(config) as (_, __, page):
        client = NotebookLMClient(page, config)
        client.ensure_notebook(config.notebook_name)
        page.wait_for_timeout(3000)

        rows = page.locator(".single-source-container, [class*='single-source']")
        count = rows.count()
        print(f"rows: {count}")

        for i in range(min(count, 20)):
            row = rows.nth(i)
            try:
                rows_data.append({
                    "i": i,
                    "text": row.inner_text(timeout=2000)[:200],
                    "html": row.inner_html()[:1500],
                    "aria": row.get_attribute("aria-label"),
                })
            except Exception as e:
                rows_data.append({"i": i, "error": str(e)})

        # ソース詳細パネル用: 最初の行をクリック
        if count > 0:
            rows.nth(0).click(timeout=5000)
            page.wait_for_timeout(2000)
            detail_html = page.locator("body").inner_html()
            youtube_in_page = "youtube" in detail_html.lower()
            rows_data.append({"after_click_youtube_in_page": youtube_in_page})
            page.screenshot(path=str(config.screenshots_dir / "source_click_0.png"), full_page=True)

    out = config.state_dir / "source_rows_debug.json"
    out.write_text(json.dumps(rows_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
