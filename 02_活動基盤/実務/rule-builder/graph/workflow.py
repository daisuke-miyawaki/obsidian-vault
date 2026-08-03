"""LangGraph ワークフロー定義。"""

from __future__ import annotations

from pathlib import Path

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph

from agents import hermes_client, openclaw_client
from config import settings
from graph.state import RuleItemState
from reviewers.draft_v0_gate import run_draft_v0_gate
from reviewers.external_review import run_external_review
from reviewers.internal_check import run_internal_check

DRAFTS_DIR = Path("data/drafts")
STATE_DIR = Path("data/state")


def _save_draft(item_id: str, suffix: str, content: str) -> None:
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    path = DRAFTS_DIR / f"{item_id}_{suffix}.md"
    path.write_text(content, encoding="utf-8")


def node_openclaw_draft(state: RuleItemState) -> RuleItemState:
    draft = openclaw_client.create_draft_v0(
        item_id=state["item_id"],
        title=state["title"],
        references=state.get("references", []),
    )
    _save_draft(state["item_id"], "v0", draft)
    return {**state, "draft_v0": draft, "status": "drafting", "error": None}


def node_draft_v0_gate(state: RuleItemState) -> RuleItemState:
    """draft_v0 直後の進行制御 Gate（レビュー可能性）。"""
    passed, result = run_draft_v0_gate(
        state.get("draft_v0") or "",
        item_id=state["item_id"],
        title=state["title"],
    )
    return {
        **state,
        "draft_v0_gate_passed": passed,
        "draft_v0_gate_result": result,
        "status": "draft_v0_gate_pass" if passed else "draft_v0_gate_fail",
    }


def _route_after_draft_v0_gate(state: RuleItemState) -> str:
    if state.get("draft_v0_gate_passed"):
        return "hermes_converge"
    return "stop"


def node_hermes_converge(state: RuleItemState) -> RuleItemState:
    draft_v1 = hermes_client.converge(
        state.get("draft_v0") or "",
        item_id=state["item_id"],
        title=state["title"],
    )
    _save_draft(state["item_id"], "v1", draft_v1)
    return {**state, "draft_v1": draft_v1, "status": "converging"}


def node_internal_check(state: RuleItemState) -> RuleItemState:
    count = state.get("internal_check_count", 0) + 1
    passed, result = run_internal_check(
        state.get("draft_v1") or "",
        item_id=state["item_id"],
        title=state["title"],
    )
    updates: RuleItemState = {
        **state,
        "internal_check_count": count,
        "internal_check_result": result,
        "status": "internal_check_pass" if passed else "internal_check_fail",
    }
    return updates


def _route_after_internal(state: RuleItemState) -> str:
    if state.get("status") == "internal_check_pass":
        return "external_review"
    if state.get("internal_check_count", 0) >= settings.max_internal_checks:
        return "await_human"
    return "hermes_converge"


def node_external_review(state: RuleItemState) -> RuleItemState:
    if state.get("external_review_done"):
        return state
    review = run_external_review(
        state.get("draft_v1") or "",
        item_id=state["item_id"],
        title=state["title"],
    )
    return {
        **state,
        "external_review": review,
        "external_review_done": True,
        "status": "external_review_done",
    }


def node_hermes_apply_review(state: RuleItemState) -> RuleItemState:
    prompt_body = f"""外部レビューを反映して v2 を作成してください。

【v1】
{state.get('draft_v1') or ''}

【外部レビュー】
{state.get('external_review') or ''}
"""
    draft_v2 = hermes_client.converge(
        prompt_body,
        item_id=state["item_id"],
        title=state["title"],
    )
    _save_draft(state["item_id"], "v2", draft_v2)
    return {**state, "draft_v2": draft_v2, "status": "awaiting_human"}


def node_await_human(state: RuleItemState) -> RuleItemState:
    return {**state, "status": "awaiting_human"}


def build_workflow():
    graph = StateGraph(RuleItemState)

    graph.add_node("openclaw_draft", node_openclaw_draft)
    graph.add_node("draft_v0_gate", node_draft_v0_gate)
    graph.add_node("hermes_converge", node_hermes_converge)
    graph.add_node("internal_check", node_internal_check)
    graph.add_node("external_review", node_external_review)
    graph.add_node("hermes_apply_review", node_hermes_apply_review)
    graph.add_node("await_human", node_await_human)

    graph.set_entry_point("openclaw_draft")
    graph.add_edge("openclaw_draft", "draft_v0_gate")
    graph.add_conditional_edges(
        "draft_v0_gate",
        _route_after_draft_v0_gate,
        {
            "hermes_converge": "hermes_converge",
            "stop": END,
        },
    )
    graph.add_edge("hermes_converge", "internal_check")
    graph.add_conditional_edges("internal_check", _route_after_internal)
    graph.add_edge("external_review", "hermes_apply_review")
    graph.add_edge("hermes_apply_review", "await_human")
    graph.add_edge("await_human", END)

    memory = MemorySaver()
    return graph.compile(checkpointer=memory, interrupt_before=["await_human"])


workflow = build_workflow()
