"""Rule Builder API（Railway / ローカル共通）。"""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from config import settings
from graph.state import RuleItemState
from graph.workflow import workflow

app = FastAPI(title="AI思考OS Rule Builder", version="0.4.3")

ITEMS_PATH = Path("data/items.json")
DRAFTS_DIR = Path("data/drafts")
APPROVED_DIR = Path("data/approved")
STATE_DIR = Path("data/state")

# thread_id = item_id で1項目1スレッド
_run_ids: dict[str, str] = {}


class HumanDecision(BaseModel):
    decision: str = Field(description="approve | revise | reject")
    notes: str = ""


class HumanDraftBody(BaseModel):
    """人間が直した draft_v2 を Human Review 待ちに載せる。"""

    draft_v2: str = Field(description="レビュー対象の Markdown")
    note: str = ""


def _load_items() -> dict[str, Any]:
    return json.loads(ITEMS_PATH.read_text(encoding="utf-8"))


def _find_item(item_id: str) -> dict[str, Any]:
    data = _load_items()
    for item in data.get("items", []):
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"項目が見つかりません: {item_id}")


def _update_item_status(item_id: str, status: str) -> None:
    data = _load_items()
    for item in data.get("items", []):
        if item["id"] == item_id:
            item["status"] = status
            break
    ITEMS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _config(thread_id: str) -> dict[str, Any]:
    return {"configurable": {"thread_id": thread_id}}


@app.get("/health")
def health() -> dict[str, Any]:
    from agents.hermes_client import is_hermes_available

    return {
        "status": "ok",
        "version": "0.4.3",
        "gemini_configured": bool(settings.gemini_keys),
        "gemini_key_count": len(settings.gemini_keys),
        "hermes_cli": is_hermes_available(),
        "hermes_llm": settings.hermes_llm,
        "draft_v0_gate": True,
        "draft_v0_form_guarantee": True,
        "hermes_converge_form_guarantee": True,
        "human_draft_submit": True,
    }


@app.get("/items")
def list_items() -> dict[str, Any]:
    return _load_items()


@app.get("/status/{item_id}")
def get_status(item_id: str) -> dict[str, Any]:
    _find_item(item_id)
    thread_id = item_id
    snapshot = workflow.get_state(_config(thread_id))
    if not snapshot or not snapshot.values:
        return {"item_id": item_id, "status": "not_started"}
    return {"item_id": item_id, **snapshot.values}


@app.post("/run/{item_id}")
def run_item(item_id: str) -> dict[str, Any]:
    """1項目の処理を開始（人間確認前で停止）。"""
    item = _find_item(item_id)
    if item.get("status") == "approved":
        raise HTTPException(status_code=400, detail="すでに承認済みです")

    if not settings.gemini_keys:
        raise HTTPException(
            status_code=400,
            detail="GEMINI_API_KEYS が未設定です。Railway の Variables または .env に設定してください。",
        )

    initial: RuleItemState = {
        "item_id": item_id,
        "title": item["title"],
        "references": item.get("references", []),
        "status": "pending",
        "internal_check_count": 0,
        "external_review_done": False,
        "revision_count": 0,
    }

    thread_id = item_id
    _update_item_status(item_id, "running")

    try:
        for _ in workflow.stream(initial, _config(thread_id), stream_mode="values"):
            pass
    except Exception as exc:  # noqa: BLE001
        _update_item_status(item_id, "error")
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    snapshot = workflow.get_state(_config(thread_id))
    _update_item_status(item_id, snapshot.values.get("status", "awaiting_human"))
    return {"item_id": item_id, "message": "人間確認待ちで停止しました", **snapshot.values}


@app.post("/human-draft/{item_id}")
def submit_human_draft(item_id: str, body: HumanDraftBody) -> dict[str, Any]:
    """人間修正版 draft_v2 を載せ、Human Review 待ちにする。"""
    item = _find_item(item_id)
    if not (body.draft_v2 or "").strip():
        raise HTTPException(status_code=400, detail="draft_v2 が空です")

    thread_id = item_id
    snapshot = workflow.get_state(_config(thread_id))
    if snapshot and snapshot.values:
        state: dict[str, Any] = dict(snapshot.values)
    else:
        state = {
            "item_id": item_id,
            "title": item["title"],
            "references": item.get("references", []),
            "revision_count": 0,
            "internal_check_count": 0,
            "external_review_done": False,
        }

    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    out = DRAFTS_DIR / f"{item_id}_v2.md"
    out.write_text(body.draft_v2, encoding="utf-8")

    state["draft_v2"] = body.draft_v2
    state["status"] = "awaiting_human"
    state["human_decision"] = None
    state["human_notes"] = body.note or state.get("human_notes")
    state["error"] = None

    # チェックポイントが無い場合でも Human Review 用に状態を載せる
    try:
        workflow.update_state(_config(thread_id), state)
    except Exception:
        # 初回はノード経由でチェックポイントを作る
        workflow.update_state(
            _config(thread_id),
            state,
            as_node="hermes_apply_review",
        )

    _update_item_status(item_id, "awaiting_human")
    return {
        "item_id": item_id,
        "status": "awaiting_human",
        "message": "修正版 draft_v2 を Human Review 待ちに載せました",
        "draft_v2_chars": len(body.draft_v2),
        "saved_to": str(out),
    }


@app.post("/approve/{item_id}")
def approve_item(item_id: str, body: HumanDecision) -> dict[str, Any]:
    """人間の OK / 修正 / 却下。"""
    _find_item(item_id)
    thread_id = item_id
    snapshot = workflow.get_state(_config(thread_id))

    if not snapshot or not snapshot.values:
        raise HTTPException(
            status_code=400,
            detail="先に /run/{item_id} または /human-draft/{item_id} を実行してください",
        )

    decision = body.decision.lower()
    if decision not in {"approve", "revise", "reject"}:
        raise HTTPException(status_code=400, detail="decision は approve / revise / reject")

    state = dict(snapshot.values)
    state["human_decision"] = decision
    state["human_notes"] = body.notes

    if decision == "approve":
        draft = state.get("draft_v2") or state.get("draft_v1") or ""
        APPROVED_DIR.mkdir(parents=True, exist_ok=True)
        out = APPROVED_DIR / f"{item_id}.md"
        out.write_text(draft, encoding="utf-8")
        state["status"] = "approved"
        _update_item_status(item_id, "approved")
        workflow.update_state(_config(thread_id), state)
        return {
            "item_id": item_id,
            "status": "approved",
            "saved_to": str(out),
            "note": "ローカル正本（AI思考OS_ルール作り_構築記録/成果物/）へ手動で反映してください",
        }

    if decision == "reject":
        state["status"] = "rejected"
        _update_item_status(item_id, "rejected")
        workflow.update_state(_config(thread_id), state)
        return {"item_id": item_id, "status": "rejected"}

    # revise
    rev = state.get("revision_count", 0) + 1
    if rev > settings.max_human_revisions:
        raise HTTPException(status_code=400, detail="人間修正回数の上限に達しました")

    state["revision_count"] = rev
    state["status"] = "revising"
    _update_item_status(item_id, "revising")
    workflow.update_state(_config(thread_id), state)
    return {
        "item_id": item_id,
        "status": "revising",
        "message": "修正指示を記録しました。再度 /run/{item_id} で処理を再開してください",
        "notes": body.notes,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=settings.port, reload=False)
