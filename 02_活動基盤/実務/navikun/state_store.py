"""簡易DB（SQLite）— 介入レベル・考えるモード・最終メッセージ時刻を管理。"""

from __future__ import annotations

import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

from config import settings

# --- 定数 ---
DEFAULT_INTERVENTION_LEVEL = "standard"
THINKING_MODE_DURATION = 3 * 24 * 3600  # 3日（秒）

INTERVENTION_HOURS = {
    "active": 24,
    "standard": 24,
    "quiet": 48,
}


def _ensure_dir() -> None:
    Path(settings.db_path).parent.mkdir(parents=True, exist_ok=True)


@contextmanager
def _conn() -> Iterator[sqlite3.Connection]:
    _ensure_dir()
    con = sqlite3.connect(settings.db_path)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def init_db() -> None:
    """テーブルがなければ作る。起動時に1回呼ぶ。"""
    with _conn() as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS channel_settings (
                channel_id    TEXT PRIMARY KEY,
                intervention  TEXT NOT NULL DEFAULT 'standard',
                updated_at    REAL NOT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS thinking_mode (
                channel_id    TEXT NOT NULL,
                user_id       TEXT NOT NULL,
                expires_at    REAL NOT NULL,
                PRIMARY KEY (channel_id, user_id)
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS last_human_message (
                channel_id    TEXT PRIMARY KEY,
                ts            REAL NOT NULL
            )
        """)
        con.execute("""
            CREATE TABLE IF NOT EXISTS last_silence_nudge (
                channel_id    TEXT PRIMARY KEY,
                ts            REAL NOT NULL
            )
        """)


# --- 介入レベル ---

def get_intervention(channel_id: str) -> str:
    with _conn() as con:
        row = con.execute(
            "SELECT intervention FROM channel_settings WHERE channel_id = ?",
            (channel_id,),
        ).fetchone()
    return row["intervention"] if row else DEFAULT_INTERVENTION_LEVEL


def set_intervention(channel_id: str, level: str) -> None:
    level = level.strip()
    valid = {"active", "standard", "quiet"}
    if level not in valid:
        raise ValueError(f"レベルは {valid} のどれかです")
    with _conn() as con:
        con.execute(
            """INSERT INTO channel_settings (channel_id, intervention, updated_at)
               VALUES (?, ?, ?)
               ON CONFLICT(channel_id) DO UPDATE SET intervention=?, updated_at=?""",
            (channel_id, level, time.time(), level, time.time()),
        )


# --- 考えるモード ---

def start_thinking(channel_id: str, user_id: str) -> float:
    """考えるモード開始。解除予定時刻（UNIX秒）を返す。"""
    expires = time.time() + THINKING_MODE_DURATION
    with _conn() as con:
        con.execute(
            """INSERT INTO thinking_mode (channel_id, user_id, expires_at)
               VALUES (?, ?, ?)
               ON CONFLICT(channel_id, user_id) DO UPDATE SET expires_at=?""",
            (channel_id, user_id, expires, expires),
        )
    return expires


def is_thinking(channel_id: str, user_id: str) -> bool:
    with _conn() as con:
        row = con.execute(
            "SELECT expires_at FROM thinking_mode WHERE channel_id=? AND user_id=?",
            (channel_id, user_id),
        ).fetchone()
    if not row:
        return False
    if row["expires_at"] < time.time():
        clear_thinking(channel_id, user_id)
        return False
    return True


def clear_thinking(channel_id: str, user_id: str) -> None:
    with _conn() as con:
        con.execute(
            "DELETE FROM thinking_mode WHERE channel_id=? AND user_id=?",
            (channel_id, user_id),
        )


# --- 最終人間メッセージ時刻（ナビくん自身の発言は記録しない） ---

def touch_human_message(channel_id: str) -> None:
    """人間がメッセージを送ったときだけ呼ぶ。"""
    now = time.time()
    with _conn() as con:
        con.execute(
            """INSERT INTO last_human_message (channel_id, ts)
               VALUES (?, ?)
               ON CONFLICT(channel_id) DO UPDATE SET ts=?""",
            (channel_id, now, now),
        )


def get_silent_channels(threshold_hours: int = 24) -> list[str]:
    """指定時間以上人間の発言がなく、かつその沈黙に対してまだ促していないチャンネル。"""
    cutoff = time.time() - threshold_hours * 3600
    with _conn() as con:
        rows = con.execute(
            """
            SELECT h.channel_id
            FROM last_human_message h
            LEFT JOIN last_silence_nudge n ON n.channel_id = h.channel_id
            WHERE h.ts < ?
              AND (n.ts IS NULL OR n.ts < h.ts)
            """,
            (cutoff,),
        ).fetchall()
    return [r["channel_id"] for r in rows]


def mark_silence_nudge(channel_id: str) -> None:
    """沈黙促しを送ったことを記録（同じ沈黙では再送しない）。"""
    now = time.time()
    with _conn() as con:
        con.execute(
            """INSERT INTO last_silence_nudge (channel_id, ts)
               VALUES (?, ?)
               ON CONFLICT(channel_id) DO UPDATE SET ts=?""",
            (channel_id, now, now),
        )


def backfill_silence_nudge_marks() -> None:
    """再デプロイ直後に既存チャンネルへ送り済みを付け、同じ沈黙での即再送を防ぐ。"""
    now = time.time()
    with _conn() as con:
        con.execute(
            """
            INSERT INTO last_silence_nudge (channel_id, ts)
            SELECT channel_id, ?
            FROM last_human_message
            WHERE channel_id NOT IN (SELECT channel_id FROM last_silence_nudge)
            """,
            (now,),
        )
