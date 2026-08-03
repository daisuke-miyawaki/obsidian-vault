"""ナビくん — エントリーポイント（Slack Bolt + Socket Mode）。"""

from __future__ import annotations

import logging
import os
import ssl

import certifi

# Mac の Python でよく起きる証明書エラー対策
os.environ.setdefault("SSL_CERT_FILE", certifi.where())
os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from background import start_background_checker
from config import settings
from slack_handlers import register_handlers
from state_store import backfill_silence_nudge_marks, init_db

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    init_db()
    backfill_silence_nudge_marks()
    logger.info("SQLite 初期化完了: %s", settings.db_path)

    ssl_context = ssl.create_default_context(cafile=certifi.where())
    client = WebClient(token=settings.slack_bot_token, ssl=ssl_context)
    app = App(client=client)
    register_handlers(app)
    logger.info("Slack ハンドラ登録完了")

    start_background_checker(app.client)

    handler = SocketModeHandler(app, settings.slack_app_token)
    logger.info("ナビくん起動します（Socket Mode）")
    handler.start()


if __name__ == "__main__":
    main()
