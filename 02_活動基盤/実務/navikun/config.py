"""ナビくん設定（環境変数から読み込み）。"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    slack_bot_token: str = Field(default="", validation_alias="SLACK_BOT_TOKEN")
    slack_app_token: str = Field(default="", validation_alias="SLACK_APP_TOKEN")

    gemini_api_key: str = Field(default="", validation_alias="GEMINI_API_KEY")
    gemini_model: str = Field(default="gemini-flash-lite-latest", validation_alias="GEMINI_MODEL")

    mem0_api_key: str = Field(default="", validation_alias="MEM0_API_KEY")
    # 顧客カルテ用の Mem0 user_id（例: customer_raifu）
    customer_memory_id: str = Field(default="customer_raifu", validation_alias="CUSTOMER_MEMORY_ID")

    # SQLite の保存先（Railway Volume を /data にマウント想定）
    db_path: str = Field(default="/data/navikun.db", validation_alias="DB_PATH")

    # 時計係の間隔（秒）
    silence_check_interval: int = Field(default=1800, validation_alias="SILENCE_CHECK_INTERVAL")

    # 沈黙促しの静かな時間帯（JST）。例: 21〜翌9時は送らない
    quiet_hours_start: int = Field(default=21, validation_alias="QUIET_HOURS_START")
    quiet_hours_end: int = Field(default=9, validation_alias="QUIET_HOURS_END")
    timezone: str = Field(default="Asia/Tokyo", validation_alias="TZ_NAME")


settings = Settings()
