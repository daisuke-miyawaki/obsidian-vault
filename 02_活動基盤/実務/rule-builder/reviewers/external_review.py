"""外部AIレビュー（Gemini・1項目1回）。"""

from __future__ import annotations

from agents import llm_client

EXTERNAL_REVIEW_PROMPT = """あなたは監査役です。採決（OK/NG）はしません。

【下書き v1】
{draft}

【項目】{title}（id: {item_id}）

以下のみ指摘してください:
- 見落とし
- 反証・矛盾
- 「本当に今必要か」（不要なら理由）

提案を増やさない。設計を膨らませない。
"""


def run_external_review(draft: str, *, item_id: str, title: str) -> str:
    prompt = EXTERNAL_REVIEW_PROMPT.format(draft=draft, item_id=item_id, title=title)
    return llm_client.generate(prompt, role="external_review")
