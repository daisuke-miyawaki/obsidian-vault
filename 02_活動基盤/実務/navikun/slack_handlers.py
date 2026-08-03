"""Slackイベント処理 — 受信 → 判定 → 返信。"""

from __future__ import annotations

import logging
import re
from datetime import datetime

from slack_bolt import App

from agent import run_agent
from config import settings
from decision import (
    looks_like_thinking,
    parse_direct_command,
    should_intervene,
    is_stagnant,
)
from memory import search_memory
from state_store import (
    get_intervention,
    is_thinking,
    set_intervention,
    start_thinking,
    touch_human_message,
)

logger = logging.getLogger(__name__)

# 介入レベルの日本語 → 内部値マッピング
LEVEL_MAP = {
    "積極的": "active",
    "標準": "standard",
    "控えめ": "quiet",
    "active": "active",
    "standard": "standard",
    "quiet": "quiet",
}

LEVEL_LABEL = {"active": "積極的", "standard": "標準", "quiet": "控えめ"}


def _collect_memories(channel_id: str, query: str) -> list[str]:
    """チャンネル記憶＋顧客カルテ（customer_raifu 等）を合わせて返す。"""
    memories: list[str] = []
    seen: set[str] = set()

    user_ids = [channel_id]
    if settings.customer_memory_id and settings.customer_memory_id not in user_ids:
        user_ids.append(settings.customer_memory_id)

    for uid in user_ids:
        try:
            for m in search_memory(user_id=uid, query=query, limit=3):
                text = (m.get("memory") or "").strip()
                if text and text not in seen:
                    seen.add(text)
                    memories.append(text)
        except Exception:
            logger.warning("Mem0 検索失敗 user_id=%s", uid, exc_info=True)

    return memories[:6]


def register_handlers(app: App) -> None:
    """Bolt アプリにイベントハンドラを登録する。"""

    bot_user_id: str | None = None

    def _get_bot_id() -> str:
        nonlocal bot_user_id
        if bot_user_id is None:
            res = app.client.auth_test()
            bot_user_id = res["user_id"]
        return bot_user_id

    def _is_bot_message(event: dict) -> bool:
        if event.get("bot_id"):
            return True
        if event.get("user") == _get_bot_id():
            return True
        return False

    def _strip_mention(text: str) -> str:
        return re.sub(r"<@[A-Z0-9]+>", "", text).strip()

    def _reply_in_thread(client, channel: str, thread_ts: str, text: str) -> None:
        client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text=text,
        )

    def _fetch_recent(client, channel: str, limit: int = 5) -> list[str]:
        """直近のメッセージテキストを取得（停滞判定用）。"""
        try:
            res = client.conversations_history(channel=channel, limit=limit)
            return [
                m.get("text", "")
                for m in res.get("messages", [])
                if not m.get("bot_id")
            ]
        except Exception:
            logger.warning("conversations_history 取得失敗", exc_info=True)
            return []

    # --- メンションイベント ---
    @app.event("app_mention")
    def handle_mention(event, client, say):
        if _is_bot_message(event):
            return

        channel = event["channel"]
        user = event["user"]
        text = _strip_mention(event.get("text", ""))
        thread_ts = event.get("thread_ts") or event["ts"]

        touch_human_message(channel)

        # 介入レベル変更コマンド
        cmd, arg = parse_direct_command(text)
        if cmd == "set_level":
            level_key = LEVEL_MAP.get(arg.strip(), None)
            if level_key:
                set_intervention(channel, level_key)
                _reply_in_thread(
                    client, channel, thread_ts,
                    f"介入レベルを「{LEVEL_LABEL[level_key]}」に変更しました。",
                )
            else:
                _reply_in_thread(
                    client, channel, thread_ts,
                    "レベルは「積極的」「標準」「控えめ」のどれかで教えてください。",
                )
            return

        # 考えるモードの自発的な解除（メンションで話しかけてきた）
        # → 考えるモード中でもメンションには応える

        # Mem0 から関連記憶を取得（チャンネル＋顧客カルテ）
        memories = _collect_memories(channel, text)

        reply = run_agent(
            channel_id=channel,
            user_id=user,
            user_message=text,
            command=cmd,
            command_arg=arg,
            memories=memories,
        )
        _reply_in_thread(client, channel, thread_ts, reply)

    # --- 通常メッセージイベント ---
    @app.event("message")
    def handle_message(event, client):
        if _is_bot_message(event):
            return
        if event.get("subtype"):
            return

        channel = event["channel"]
        user = event.get("user", "")
        text = event.get("text", "")

        touch_human_message(channel)

        # 考えるモードのきっかけ検出
        if looks_like_thinking(text):
            expires = start_thinking(channel, user)
            dt = datetime.fromtimestamp(expires)
            thread_ts = event.get("thread_ts") or event["ts"]
            _reply_in_thread(
                client, channel, thread_ts,
                f"了解です！ゆっくりどうぞ。{dt.month}/{dt.day} ごろまで静かにしてますね。"
                "\nまた話したくなったら @ナビくん で呼んでください。",
            )
            return

        # 考えるモード中 → 無視
        if is_thinking(channel, user):
            return

        # 介入すべきか
        if not should_intervene(channel, user, is_mention=False):
            return

        # 停滞判定
        recent = _fetch_recent(client, channel, limit=5)
        if not is_stagnant(recent):
            return

        # 停滞してるので軽く介入
        memories = _collect_memories(channel, text or "らいふギャラリー 進捗")

        reply = run_agent(
            channel_id=channel,
            user_id=user,
            user_message="（会話が停滞しているようなので、軽く話を整理して声をかけてください）",
            memories=memories,
        )
        thread_ts = event.get("thread_ts") or event["ts"]
        _reply_in_thread(client, channel, thread_ts, reply)
