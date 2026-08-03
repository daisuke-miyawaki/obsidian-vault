"""NotebookLM UI diagnostic — run: python -m src.debug_ui"""
from __future__ import annotations

import json

from .auth import with_browser
from .config_loader import load_config
from . import selectors as sel


def dump_page(page, label: str) -> dict:
    buttons = page.locator("button")
    btn_info = []
    for i in range(min(buttons.count(), 40)):
        btn = buttons.nth(i)
        try:
            btn_info.append(
                {
                    "i": i,
                    "aria": btn.get_attribute("aria-label"),
                    "text": (btn.inner_text(timeout=500) or "")[:100],
                    "class": (btn.get_attribute("class") or "")[:120],
                    "visible": btn.is_visible(),
                }
            )
        except Exception as e:
            btn_info.append({"i": i, "error": str(e)})

    links = page.locator("a[href*='/notebook/']")
    link_info = []
    for i in range(min(links.count(), 10)):
        link = links.nth(i)
        try:
            link_info.append({"href": link.get_attribute("href"), "text": link.inner_text(timeout=500)[:80]})
        except Exception:
            pass

    return {
        "label": label,
        "url": page.url,
        "title": page.title(),
        "is_notebook": "/notebook/" in page.url,
        "notebook_links": link_info,
        "buttons": btn_info,
    }


def main() -> None:
    config = load_config()
    config.screenshots_dir.mkdir(parents=True, exist_ok=True)
    reports = []

    with with_browser(config) as (_, __, page):
        page.goto(config.base_url, wait_until="domcontentloaded", timeout=120_000)
        page.wait_for_timeout(4000)
        reports.append(dump_page(page, "home"))
        page.screenshot(path=str(config.screenshots_dir / "debug_home.png"), full_page=True)

        clicked = False
        for selector in sel.CREATE_NOTEBOOK_SELECTORS:
            loc = page.locator(selector).first
            if loc.count() > 0 and loc.is_visible():
                print(f"Clicking create: {selector}")
                loc.click(timeout=8000)
                clicked = True
                break
        if not clicked:
            for text in ["Create new notebook", "新しいノートブック"]:
                loc = page.get_by_text(text, exact=False).first
                if loc.count() > 0:
                    print(f"Clicking text: {text}")
                    loc.click(timeout=8000)
                    clicked = True
                    break

        page.wait_for_timeout(5000)
        reports.append(dump_page(page, "after_create_click"))
        page.screenshot(path=str(config.screenshots_dir / "debug_after_create.png"), full_page=True)

        if "/notebook/" not in page.url:
            link = page.locator("a[href*='/notebook/']").first
            if link.count() > 0:
                href = link.get_attribute("href") or ""
                if href.startswith("/"):
                    href = "https://notebooklm.google.com" + href
                print(f"Navigating to first notebook: {href}")
                page.goto(href, wait_until="domcontentloaded")
                page.wait_for_timeout(4000)

        reports.append(dump_page(page, "notebook_page"))
        page.screenshot(path=str(config.screenshots_dir / "debug_notebook.png"), full_page=True)

        found = []
        for selector in sel.ADD_SOURCE_SELECTORS:
            loc = page.locator(selector)
            if loc.count() > 0:
                found.append({"selector": selector, "count": loc.count(), "visible": loc.first.is_visible()})
        reports.append({"add_source_matches": found})

    out = config.state_dir / "debug_report.json"
    out.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Report: {out}")
    print(f"Screenshots: {config.screenshots_dir}")


if __name__ == "__main__":
    main()
