"""アプリ設定（環境変数）。"""

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# このファイル: 02_活動基盤/実務/rule-builder/config.py → Vault直下は parents[3]
_DEFAULT_VAULT_ROOT = str(Path(__file__).resolve().parents[3])


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True,
    )

    hermes_llm: str = "xai-oauth"
    gemini_api_keys: str = Field(default="", validation_alias="GEMINI_API_KEYS")
    external_review_provider: str = "gemini"

    draft_only: bool = True
    max_internal_checks: int = 2
    max_external_reviews: int = 1
    max_human_revisions: int = 1
    human_approval_required: bool = True
    max_openclaw_api_calls: int = 3

    port: int = 8080
    # 外箱フォルダ名が変わっても追従する。上書きするときだけ WORKSPACE_ROOT を使う。
    workspace_root: str = Field(default=_DEFAULT_VAULT_ROOT, validation_alias="WORKSPACE_ROOT")

    @property
    def gemini_keys(self) -> list[str]:
        raw = self.gemini_api_keys.strip() or os.getenv("GEMINI_API_KEYS", "").strip()
        if not raw:
            return []
        return [k.strip() for k in raw.split(",") if k.strip()]


settings = Settings()
