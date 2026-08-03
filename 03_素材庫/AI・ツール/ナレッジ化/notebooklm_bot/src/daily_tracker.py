"""NotebookLM の1日チャット数を追跡（太平洋時間の日付でカウント）"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# NotebookLM の日次リセットは太平洋時間 0時頃
_PACIFIC = ZoneInfo("America/Los_Angeles")


class DailyChatTracker:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._data = self._load()

    def _today(self) -> str:
        return datetime.now(_PACIFIC).strftime("%Y-%m-%d")

    def _load(self) -> dict:
        if not self.path.exists():
            return {"date": self._today(), "count": 0}
        data = json.loads(self.path.read_text(encoding="utf-8"))
        if data.get("date") != self._today():
            return {"date": self._today(), "count": 0}
        return data

    def _save(self) -> None:
        self.path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def count(self) -> int:
        self._data = self._load()
        return int(self._data.get("count", 0))

    def can_chat(self, daily_max: int | None) -> bool:
        if daily_max is None or daily_max <= 0:
            return True
        return self.count() < daily_max

    def record_chat(self) -> int:
        self._data = self._load()
        self._data["count"] = self.count() + 1
        self._save()
        return self._data["count"]
