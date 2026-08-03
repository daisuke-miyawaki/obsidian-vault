"""LangGraph 内部チェック（Gemini・最大2回）。"""

from __future__ import annotations

from agents import llm_client

INTERNAL_CHECK_PROMPT = """あなたはルール品質の内部チェッカーです。採決はしません。

【下書き v1】
{draft}

【項目】{title}（id: {item_id}）

以下5項目をチェックし、JSON風に回答してください:
PASS または FAIL

1. 人生戦略OSとの矛盾
2. User Model / AI思考OS v0.1 との矛盾
3. Pure OS Town（穏やかさ・Eco・HallucinationPrevention）との矛盾
4. 既存ルールとの重複
5. 1行で目的が説明できる粒度

形式:
RESULT: PASS または FAIL
ISSUES: （FAIL時のみ、箇条書き）
"""


def run_internal_check(draft: str, *, item_id: str, title: str) -> tuple[bool, str]:
    prompt = INTERNAL_CHECK_PROMPT.format(draft=draft, item_id=item_id, title=title)
    result = llm_client.generate(prompt, role="internal_check")
    passed = "RESULT: PASS" in result.upper() or "RESULT:PASS" in result.upper().replace(" ", "")
    return passed, result
