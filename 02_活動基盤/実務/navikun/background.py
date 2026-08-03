"""時計係 — 定期的に沈黙チャンネルを検知して促しメッセージを送る。"""

from __future__ import annotations

import asyncio
import logging
import threading
from datetime import datetime
from zoneinfo import ZoneInfo

from config import settings
from prompts import SILENCE_NUDGE_TEMPLATE
from state_store import INTERVENTION_HOURS, get_intervention, get_silent_channels, mark_silence_nudge

logger = logging.getLogger(__name__)


def _in_quiet_hours() -> bool:
    """夜21時〜翌朝9時（既定・JST）は促しを送らない。"""
    now = datetime.now(ZoneInfo(settings.timezone))
    start = settings.quiet_hours_start
    end = settings.quiet_hours_end
    if start == end:
        return False
    if start > end:
        # 例: 21〜9
        return now.hour >= start or now.hour < end
    return start <= now.hour < end


def _send_nudge(client, channel_id: str) -> None:
    """沈黙検知の促しメッセージを送る（成功したら送り済みを記録）。"""
    try:
        client.chat_postMessage(
            channel=channel_id,
            text=SILENCE_NUDGE_TEMPLATE.strip(),
        )
        mark_silence_nudge(channel_id)
        logger.info("沈黙促し送信: %s", channel_id)
    except Exception:
        logger.warning("沈黙促し送信失敗: %s", channel_id, exc_info=True)


def _check_once(client) -> None:
    """全介入レベル分の沈黙チャンネルを確認。"""
    if _in_quiet_hours():
        logger.info("静かな時間帯のため沈黙促しをスキップします")
        return

    for level, hours in INTERVENTION_HOURS.items():
        channels = get_silent_channels(threshold_hours=hours)
        for ch in channels:
            ch_level = get_intervention(ch)
            if ch_level == level:
                _send_nudge(client, ch)


def start_background_checker(client) -> None:
    """別スレッドで定期チェックを回す。"""

    async def _loop():
        while True:
            try:
                _check_once(client)
            except Exception:
                logger.error("時計係エラー", exc_info=True)
            await asyncio.sleep(settings.silence_check_interval)

    def _run():
        asyncio.run(_loop())

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    logger.info("時計係を開始しました（間隔: %d秒）", settings.silence_check_interval)
