"""LangGraph 状態定義。"""

from __future__ import annotations

from typing import TypedDict


class RuleItemState(TypedDict, total=False):
    item_id: str
    title: str
    references: list[str]
    status: str

    draft_v0: str | None
    draft_v1: str | None
    draft_v2: str | None

    draft_v0_gate_passed: bool
    draft_v0_gate_result: str | None

    internal_check_result: str | None
    internal_check_count: int
    external_review: str | None
    external_review_done: bool

    human_decision: str | None
    human_notes: str | None
    revision_count: int

    error: str | None
