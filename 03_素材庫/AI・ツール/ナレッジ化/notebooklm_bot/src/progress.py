from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

Status = Literal["pending", "done", "failed", "skipped"]


class ProgressStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._data: dict[str, dict] = self._load()

    def _load(self) -> dict[str, dict]:
        if not self.path.exists():
            return {"videos": {}, "sources_added": [], "updated_at": None}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self) -> None:
        self._data["updated_at"] = datetime.now(timezone.utc).isoformat()
        self.path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def get_status(self, video_no: str) -> Status:
        entry = self._data.get("videos", {}).get(video_no, {})
        return entry.get("status", "pending")

    def mark(self, video_no: str, status: Status, **extra: str) -> None:
        videos = self._data.setdefault("videos", {})
        entry = videos.setdefault(video_no, {})
        entry["status"] = status
        entry["updated_at"] = datetime.now(timezone.utc).isoformat()
        for key, value in extra.items():
            entry[key] = value
        self.save()

    def sources_added(self) -> list[str]:
        return list(self._data.get("sources_added", []))

    def add_source_url(self, url: str) -> None:
        sources = self._data.setdefault("sources_added", [])
        if url not in sources:
            sources.append(url)
            self.save()

    def is_source_added(self, url: str) -> bool:
        return url in self.sources_added()
