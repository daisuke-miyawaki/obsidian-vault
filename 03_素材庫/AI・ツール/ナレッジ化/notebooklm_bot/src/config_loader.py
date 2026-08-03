from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class AppConfig:
    channel_slug: str
    taxonomy: str | None
    base_url: str
    notebook_name: str
    urls_file: Path
    output_dir: Path
    index_file: Path
    prompt_file: Path
    headless: bool
    reply_timeout_sec: int
    source_index_timeout_sec: int
    delay_between_videos_sec: int
    max_retries: int
    batch_size: int
    daily_max_chats: int | None
    notebook_per_video: bool
    stop_on_rate_limit: bool
    gemini_model: str
    gemini_api_key_env: str
    gemini_api_keys_env: str
    gemini_env_file: Path | None
    gemini_daily_max_requests: int | None
    gemini_delay_sec: int
    gemini_max_retries: int
    gemini_retry_wait_sec: int
    project_root: Path
    state_dir: Path
    profile_dir: Path
    progress_file: Path
    notebook_url_file: Path
    screenshots_dir: Path


def load_config(config_path: Path | None = None) -> AppConfig:
    project_root = Path(__file__).resolve().parent.parent
    config_path = config_path or (project_root / "config.yaml")
    raw: dict[str, Any] = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    paths = raw["paths"]
    runtime = raw["runtime"]
    notebooklm = raw["notebooklm"]
    gemini = raw.get("gemini", {})
    state_dir = project_root / "state"

    def resolve(p: str) -> Path:
        path = Path(p)
        return path if path.is_absolute() else (project_root / path).resolve()

    return AppConfig(
        channel_slug=raw.get("channel_slug", "default"),
        taxonomy=raw.get("taxonomy"),
        base_url=notebooklm["base_url"],
        notebook_name=notebooklm["notebook_name"],
        urls_file=resolve(paths["urls_file"]),
        output_dir=resolve(paths["output_dir"]),
        index_file=resolve(paths["index_file"]),
        prompt_file=resolve(paths["prompt_file"]),
        headless=bool(runtime.get("headless", False)),
        reply_timeout_sec=int(runtime.get("reply_timeout_sec", 300)),
        source_index_timeout_sec=int(runtime.get("source_index_timeout_sec", 120)),
        delay_between_videos_sec=int(runtime.get("delay_between_videos_sec", 10)),
        max_retries=int(runtime.get("max_retries", 3)),
        batch_size=int(runtime.get("batch_size", 50)),
        daily_max_chats=(
            int(runtime["daily_max_chats"])
            if runtime.get("daily_max_chats") is not None
            else None
        ),
        notebook_per_video=bool(notebooklm.get("notebook_per_video", False)),
        stop_on_rate_limit=bool(runtime.get("stop_on_rate_limit", True)),
        gemini_model=str(gemini.get("model", "gemini-2.5-flash")),
        gemini_api_key_env=str(gemini.get("api_key_env", "GEMINI_API_KEY")),
        gemini_api_keys_env=str(gemini.get("api_keys_env", "GEMINI_API_KEYS")),
        gemini_env_file=(
            resolve(gemini["env_file"]) if gemini.get("env_file") else None
        ),
        gemini_daily_max_requests=(
            int(gemini["daily_max_requests"])
            if gemini.get("daily_max_requests") is not None
            else None
        ),
        gemini_delay_sec=int(gemini.get("delay_sec", 5)),
        gemini_max_retries=int(gemini.get("max_retries", 2)),
        gemini_retry_wait_sec=int(gemini.get("retry_wait_sec", 15)),
        project_root=project_root,
        state_dir=state_dir,
        profile_dir=state_dir / "browser_profile",
        progress_file=state_dir / "progress.json",
        notebook_url_file=state_dir / "notebook_url.txt",
        screenshots_dir=state_dir / "screenshots",
    )
