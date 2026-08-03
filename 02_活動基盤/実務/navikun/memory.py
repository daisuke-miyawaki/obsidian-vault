"""Mem0連携 — 顧客/チャンネルごとの長期記憶。"""

from __future__ import annotations

from config import settings

_client = None


def _get_client():
    global _client
    if _client is None:
        from mem0 import MemoryClient
        _client = MemoryClient(api_key=settings.mem0_api_key)
    return _client


def add_memory(user_id: str, text: str, metadata: dict | None = None) -> None:
    """記憶を追加する。user_id はチャンネルID or 顧客IDを渡す。"""
    _get_client().add(text, user_id=user_id, metadata=metadata or {})


def search_memory(user_id: str, query: str, limit: int = 5) -> list[dict]:
    """関連する記憶を検索して返す。"""
    results = _get_client().search(
        query,
        filters={"user_id": user_id},
        top_k=limit,
    )
    return results.get("results", []) if isinstance(results, dict) else results


def get_all_memories(user_id: str) -> list[dict]:
    """そのユーザー/チャンネルの記憶を全部返す。"""
    results = _get_client().get_all(filters={"user_id": user_id})
    return results.get("results", []) if isinstance(results, dict) else results
