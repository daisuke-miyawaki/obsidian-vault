"""Gemini API クライアント（キーローテーション）。"""

from __future__ import annotations

import itertools
from typing import Iterator

import google.generativeai as genai

from config import settings

_key_cycle: Iterator[str] | None = None
_call_counts: dict[str, int] = {}


def _keys() -> list[str]:
    keys = settings.gemini_keys
    if not keys:
        raise RuntimeError(
            "GEMINI_API_KEYS が未設定です。内部チェック・下書き・外部レビューに必要です。"
        )
    return keys


def _next_key() -> str:
    global _key_cycle
    keys = _keys()
    if _key_cycle is None:
        _key_cycle = itertools.cycle(keys)
    return next(_key_cycle)


def generate(prompt: str, *, role: str = "default") -> str:
    """Gemini でテキスト生成。429 時は次のキーへ。"""
    last_error: Exception | None = None
    keys = _keys()

    for _ in range(len(keys)):
        key = _next_key()
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            _call_counts[role] = _call_counts.get(role, 0) + 1
            return (response.text or "").strip()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            continue

    raise RuntimeError(f"Gemini 全キー失敗 ({role}): {last_error}")


def call_count(role: str) -> int:
    return _call_counts.get(role, 0)


def has_keys() -> bool:
    return bool(settings.gemini_keys)
