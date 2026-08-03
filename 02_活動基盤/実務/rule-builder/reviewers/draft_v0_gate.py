"""draft_v0 進行制御 Gate（レビュー可能性の最低条件）。

FP-02 / FP-05 第一段階：条件未達なら Hermes 以降へ進めない。
internal_check（v1向け内容品質）とは別役割。
"""

from __future__ import annotations

import re

# 今回観察された思考ログ・探索ログの典型パターン
_LOG_MARKERS = (
    "┌─ Reasoning",
    "─ Reasoning ─",
    "Reasoning ────────────────────────────────",
    "No files found",
    "search_files",
    "Reached maximum iterations",
    "maximum iterations",
    "tool_choice",
    "ファイルが見つかり",
    "見つかりません",
    "The files aren't found",
    "The find also returned nothing",
)

_HEADING_RE = re.compile(r"(?m)^#{1,3}\s+\S+")


def run_draft_v0_gate(draft: str, *, item_id: str, title: str) -> tuple[bool, str]:
    """レビュー可能性 Gate。

    PASS 条件（すべて満たす）:
    1. 対象ルールの文書として読める（Markdown見出し＋本文）
    2. 思考ログ・探索ログではない
    3. 人間が中身を判断できる（最低限の本文量）
    """
    text = (draft or "").strip()
    issues: list[str] = []

    if not text:
        return False, "FAIL: draft_v0 が空です"

    # 2. 思考ログ・探索ログではない
    for marker in _LOG_MARKERS:
        if marker in text:
            issues.append(f"思考/探索ログを検出: {marker!r}")

    # ログ比率が高い（Reasoning枠が本文を支配）
    if text.count("Reasoning") >= 2:
        issues.append("Reasoning 記述が複数あり、文書として読めない")

    # 1. 対象ルールの文書として読める
    if not _HEADING_RE.search(text):
        issues.append("Markdown見出し（# …）が無い")

    # 3. 人間が中身を判断できる（最低限の本文）
    # 見出し行と空行を除いた実質文字数
    body_lines = [
        ln.strip()
        for ln in text.splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    body = "\n".join(body_lines)
    if len(body) < 80:
        issues.append("本文が短く、中身を判断できない")

    if issues:
        return False, "FAIL:\n- " + "\n- ".join(issues)

    return True, "PASS: レビュー可能性の最低条件を満たす"
