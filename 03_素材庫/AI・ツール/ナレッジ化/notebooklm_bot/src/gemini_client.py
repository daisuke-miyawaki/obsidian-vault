"""Gemini API で文字起こしから Markdown を生成する（REST / requests）"""

from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

import requests

from .config_loader import AppConfig
from .daily_tracker import DailyChatTracker


class GeminiRateLimitError(RuntimeError):
    """Gemini API のレート制限・日次上限（全キー使い切り）"""


_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
_FREE_TIER_DAILY_PER_KEY = 20


def load_env_file(path: Path, *, overwrite: bool = False) -> None:
    """env ファイルを読み込む。overwrite=True ならファイルの値を優先する。"""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, _, value = stripped.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            continue
        if overwrite or key not in os.environ:
            os.environ[key] = value


def _load_env_for_config(config: AppConfig) -> None:
    if config.gemini_env_file:
        load_env_file(config.gemini_env_file, overwrite=True)
    load_env_file(config.project_root / ".env")


def collect_api_keys(config: AppConfig) -> list[str]:
    """
    APIキーを収集する（重複除去・順序維持）。

    対応形式（GEMINI_API_KEY.env 等）:
      1. GEMINI_API_KEYS=key1,key2,key3   … 複数キー（おすすめ）
      2. GEMINI_API_KEY=key1              … 単一キー（従来互換）
      3. GEMINI_API_KEY_2=key2, _3=...    … 番号付き追加分
    """
    _load_env_for_config(config)
    keys: list[str] = []
    seen: set[str] = set()

    def add(key: str) -> None:
        key = key.strip()
        if key and key not in seen:
            seen.add(key)
            keys.append(key)

    multi = os.environ.get(config.gemini_api_keys_env, "").strip()
    if multi:
        for part in multi.split(","):
            add(part)

    add(os.environ.get(config.gemini_api_key_env, ""))

    base = config.gemini_api_key_env
    for i in range(2, 100):
        add(os.environ.get(f"{base}_{i}", ""))

    if not keys:
        hint = config.gemini_env_file or (config.project_root / ".env")
        raise RuntimeError(
            f"Gemini API キーがありません。"
            f"{hint} に GEMINI_API_KEY または GEMINI_API_KEYS を設定してください。"
        )
    return keys


def effective_daily_max(config: AppConfig) -> int | None:
    """複数キー時はキー数 × 1日上限で計算する。"""
    if config.gemini_daily_max_requests is None:
        return None
    try:
        key_count = len(collect_api_keys(config))
    except RuntimeError:
        key_count = 1
    per_key = config.gemini_daily_max_requests
    return per_key * max(1, key_count)


def check_daily_quota(config: AppConfig, tracker: DailyChatTracker) -> None:
    limit = effective_daily_max(config)
    if not tracker.can_chat(limit):
        raise GeminiRateLimitError(
            f"本日の Gemini リクエスト上限（設定値 {limit} 回）に達しました。"
            "明日以降に再開するか、APIキーを追加してください。"
        )


def _extract_text(payload: dict) -> str:
    candidates = payload.get("candidates") or []
    if not candidates:
        raise RuntimeError(f"Gemini 応答に candidates がありません: {payload}")
    parts = candidates[0].get("content", {}).get("parts") or []
    texts = [p.get("text", "") for p in parts if p.get("text")]
    text = "\n".join(texts).strip()
    if not text:
        raise RuntimeError("Gemini から空の回答が返りました")
    return text


def _is_daily_quota_exhausted(response: requests.Response) -> bool:
    """1日の無料枠使い切り（キー切替対象）かどうか。"""
    if response.status_code != 429:
        return False
    body = response.text.lower()
    markers = (
        "free_tier",
        "quota exceeded",
        "perday",
        "generate_content_free_tier",
        "resource_exhausted",
    )
    return any(m in body for m in markers)


def _retry_after_sec(response: requests.Response) -> float | None:
    """短時間レート制限の待機秒数（あれば）。"""
    try:
        payload = response.json()
        msg = payload.get("error", {}).get("message", "")
    except json.JSONDecodeError:
        msg = response.text
    match = re.search(r"retry in ([0-9.]+)s", msg, re.I)
    if match:
        return float(match.group(1))
    return None


def _call_gemini(
    *,
    url: str,
    api_key: str,
    prompt: str,
    max_retries: int,
    retry_wait_sec: int,
) -> str:
    """1つのAPIキーで呼び出し（短時間429は同キーでリトライ）。"""
    last_error: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(
                url,
                params={"key": api_key},
                json={"contents": [{"parts": [{"text": prompt}]}]},
                timeout=600,
            )

            if response.status_code == 429 and _is_daily_quota_exhausted(response):
                raise GeminiRateLimitError(response.text)

            if response.status_code in (429, 503):
                if attempt >= max_retries:
                    raise GeminiRateLimitError(response.text)
                wait = _retry_after_sec(response) or (retry_wait_sec * attempt)
                print(
                    f"  Gemini 短時間制限 → {wait:.0f}秒待機 "
                    f"({attempt}/{max_retries})"
                )
                time.sleep(wait)
                continue

            if response.status_code >= 400:
                raise RuntimeError(
                    f"Gemini API エラー ({response.status_code}): {response.text[:500]}"
                )
            return _extract_text(response.json())

        except GeminiRateLimitError:
            raise
        except requests.RequestException as exc:
            last_error = exc
            if attempt < max_retries:
                time.sleep(retry_wait_sec)
                continue
            raise RuntimeError(f"Gemini API 通信失敗: {exc}") from exc

    raise RuntimeError(f"Gemini API 最大リトライ超過: {last_error}")


def generate_markdown(config: AppConfig, prompt: str) -> str:
    """複数APIキーを順に試し、日次上限時は自動ローテーションする。"""
    api_keys = collect_api_keys(config)
    url = f"{_API_BASE}/{config.gemini_model}:generateContent"
    exhausted = 0

    for index, api_key in enumerate(api_keys, start=1):
        mask = f"...{api_key[-6:]}" if len(api_key) > 6 else "(短いキー)"
        if len(api_keys) > 1:
            print(f"  APIキー {index}/{len(api_keys)} を使用 ({mask})")
        try:
            return _call_gemini(
                url=url,
                api_key=api_key,
                prompt=prompt,
                max_retries=config.gemini_max_retries,
                retry_wait_sec=config.gemini_retry_wait_sec,
            )
        except GeminiRateLimitError as exc:
            exhausted += 1
            if index < len(api_keys):
                print(
                    f"  キー {index}/{len(api_keys)} が日次上限 → "
                    f"次のキーに切替"
                )
                continue
            raise GeminiRateLimitError(
                f"登録済みの全 {len(api_keys)} キーが上限に達しました。"
            ) from exc

    raise GeminiRateLimitError(
        f"登録済みの全 {exhausted} キーが上限に達しました。"
    )
