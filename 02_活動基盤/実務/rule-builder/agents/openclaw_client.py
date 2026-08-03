"""OpenClaw 相当：調査・下書き v0。

draft_v0 の形式保証は本モジュールの出口で行う（Gemini／Hermes 共通）。
"""

from __future__ import annotations

import re

from agents import gemini_client, llm_client
from config import settings
from reviewers.draft_v0_gate import run_draft_v0_gate

_FORMAT_RULES = """
【出力形式・必須（形式保証）】
- 出力は Markdown のルール文書のみとする
- 先頭は # 見出し（項目名）
- Reasoning／思考過程／探索ログ／ツール実行ログ／「ファイルが見つからない」等は一切含めない
- 説明の前置きや後書きも不要。文書本文だけを出力する
"""

OPENCLAW_DRAFT_PROMPT = """あなたは OpenClaw（実行部隊）の下書き担当です。
ルールの下書き v0 を Markdown で作成してください。
""" + _FORMAT_RULES + """
【制約】
- 正式保存はしない（下書きのみ）
- 提案を増やしすぎない
- 1項目1目的
- 参照パスが読めなくても、項目名と下記ヒントから文書を書く（探索ログは出さない）

【参照ファイルパス（参考。探索結果は出力に書かない）】
{references}

【項目】{title}（id: {item_id}）

【Tier構造（memory-policy の場合のヒント）】
- Tier1: 常時参照（AI思考OS, User Model, Core Values 等）
- Tier2: 要約保存（Failure Library, Decision Log 等）
- Tier3: 長期保管（会話ログ, リサーチ, 日誌）
"""

_REWRITE_PROMPT = """次のテキストを、ルールの Markdown 文書だけに書き直してください。
""" + _FORMAT_RULES + """
【項目】{title}（id: {item_id}）

【元テキスト】
{raw}
"""

_HEADING_RE = re.compile(r"(?m)^#{1,3}\s+\S+")


def _extract_markdown_body(text: str) -> str:
    """先頭の思考／探索ログを除き、最初の Markdown 見出し以降を取り出す。"""
    text = (text or "").strip()
    if not text:
        return ""
    match = _HEADING_RE.search(text)
    if match:
        return text[match.start() :].strip()
    return text


def _strip_log_lines(text: str) -> str:
    """残ったログ行を落とす（形式保証の後処理）。"""
    drop_substrings = (
        "┌─ Reasoning",
        "Reasoning ─",
        "No files found",
        "search_files",
        "Reached maximum iterations",
        "maximum iterations",
        "tool_choice",
        "ファイルが見つかり",
        "The files aren't found",
        "The find also returned nothing",
    )
    lines: list[str] = []
    for line in text.splitlines():
        if any(s in line for s in drop_substrings):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _minimal_document(*, item_id: str, title: str) -> str:
    """LLMが形式を満たせない場合の最低限 Markdown（出口の最終保証）。"""
    return f"""# {title}

## 目的
本項目（id: {item_id}）のルール下書き。人間が中身を判断できる最小構成とする。

## 定義
- 本文書は draft_v0 の形式保証用に整えた Markdown である。
- 参照ファイルの探索結果や思考ログは含めない。

## 内容メモ
- 項目名: {title}
- 識別子: {item_id}
- 後工程（Hermes 収束・内部チェック・外部レビュー・人間確認）で内容を精緻化する。
"""


def _ensure_reviewable_form(
    raw: str, *, item_id: str, title: str
) -> str:
    """Gemini／Hermes 共通の出口で形式保証する。"""
    candidate = _strip_log_lines(_extract_markdown_body(raw))
    passed, _ = run_draft_v0_gate(candidate, item_id=item_id, title=title)
    if passed:
        return candidate

    # 1回だけ書き直し依頼（同じ出口条件）
    rewrite = llm_client.generate(
        _REWRITE_PROMPT.format(title=title, item_id=item_id, raw=raw[:4000]),
        role="openclaw",
    )
    candidate = _strip_log_lines(_extract_markdown_body(rewrite))
    passed, _ = run_draft_v0_gate(candidate, item_id=item_id, title=title)
    if passed:
        return candidate

    # 最終保証：最小 Markdown（ログ混入を出口で排除）
    return _minimal_document(item_id=item_id, title=title)


def create_draft_v0(*, item_id: str, title: str, references: list[str]) -> str:
    if gemini_client.call_count("openclaw") >= settings.max_openclaw_api_calls:
        raise RuntimeError(
            f"OpenClaw API上限（{settings.max_openclaw_api_calls}回/項目）に到達しました。"
        )

    prompt = OPENCLAW_DRAFT_PROMPT.format(
        item_id=item_id,
        title=title,
        references="\n".join(f"- {r}" for r in references) or "- （なし）",
    )
    raw = llm_client.generate(prompt, role="openclaw")
    return _ensure_reviewable_form(raw, item_id=item_id, title=title)
