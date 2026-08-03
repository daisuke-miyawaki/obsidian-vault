"""LLM 生成（Gemini → 失敗時 Hermes/Grok にフォールバック）。"""

from __future__ import annotations

from agents import gemini_client, hermes_client


def generate(prompt: str, *, role: str = "default") -> str:
    """Gemini を優先。失敗したら Hermes（Grok OAuth）へ。"""
    if gemini_client.has_keys():
        try:
            return gemini_client.generate(prompt, role=role)
        except Exception:
            pass

    if hermes_client.is_hermes_available():
        return hermes_client.ask(prompt)

    raise RuntimeError(
        "LLM 利用不可: Gemini キー未設定または上限、かつ Hermes も使えません。"
    )
