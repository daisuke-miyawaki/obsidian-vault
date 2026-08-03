"""Hermes Agent 呼び出し（Grok OAuth・APIキー不要）。

収束（converge）の出口で draft_v1 / draft_v2 の形式保証を行う。
汎用 ask() は加工しない（internal_check／external_review／OpenClawフォールバック用）。
"""

from __future__ import annotations

import re
import shutil
import subprocess

from config import settings
from reviewers.draft_v0_gate import run_draft_v0_gate

_FORMAT_RULES = """
【出力形式・必須（形式保証）】
- 出力は Markdown のルール文書のみとする
- 先頭は # 見出し（項目名）
- Reasoning／思考過程／探索ログ／ツール実行ログ／「ファイルが見つからない」等は一切含めない
- ファイル探索はしない。入力の下書きだけを整理して文書にする
- 説明の前書きや後書きも不要。文書本文だけを出力する
"""

HERMES_CONVERGE_PROMPT = """あなたは Hermes Agent（設計を収束させるAI）です。
提案を増やさず、統合・整理・簡素化を優先してください。
""" + _FORMAT_RULES + """
【タスク】
以下の下書きを読み、収束させたルール文書を Markdown で出力してください。

【チェック（探索せず、入力本文と項目名だけで判断）】
- 重複概念の統合
- 1項目1目的の維持

【下書き】
{draft_v0}

【項目】{title}（id: {item_id}）
"""

_HEADING_RE = re.compile(r"(?m)^#{1,3}\s+\S+")

_DROP_SUBSTRINGS = (
    "┌─ Reasoning",
    "Reasoning ─",
    "No files found",
    "search_files",
    "Reached maximum iterations",
    "maximum iterations",
    "tool_choice",
    "ファイルが見つかり",
    "The files aren't found",
    "The find also returned nothing",
    "The search returned no results",
    "The workspace has files",
)


def is_hermes_available() -> bool:
    return shutil.which("hermes") is not None


def ask(prompt: str, *, timeout: int = 300) -> str:
    """Hermes（Grok OAuth）で汎用生成。stdout をそのまま返す。"""
    if not is_hermes_available():
        raise RuntimeError("Hermes CLI が見つかりません。")

    result = subprocess.run(
        [
            "hermes",
            "chat",
            "-q",
            prompt,
            "-Q",
            "--provider",
            "xai-oauth",
            "--max-turns",
            "3",
        ],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )

    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        raise RuntimeError(f"Hermes 実行失敗: {stderr or result.stdout}")

    return (result.stdout or "").strip()


def _extract_markdown_body(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    match = _HEADING_RE.search(text)
    if match:
        return text[match.start() :].strip()
    return text


def _strip_log_lines(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if any(s in line for s in _DROP_SUBSTRINGS):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _minimal_document(*, item_id: str, title: str) -> str:
    return f"""# {title}

## 目的
本項目（id: {item_id}）のルール文書。人間が中身を判断できる最小構成とする。

## 定義
- 本文書は Hermes 収束出口の形式保証用に整えた Markdown である。
- 参照ファイルの探索結果や思考ログは含めない。

## 内容メモ
- 項目名: {title}
- 識別子: {item_id}
- 入力下書きを収束できなかった場合の最小文書である。
"""


def _ensure_reviewable_form(raw: str, *, item_id: str, title: str) -> str:
    """収束出口（draft_v1 / draft_v2 共通）の形式保証。

    再生成はしない（ask→Hermes の再帰を避ける）。掃除＋最終最小文書で保証する。
    """
    candidate = _strip_log_lines(_extract_markdown_body(raw))
    passed, _ = run_draft_v0_gate(candidate, item_id=item_id, title=title)
    if passed:
        return candidate
    return _minimal_document(item_id=item_id, title=title)


def converge(draft_v0: str, *, item_id: str, title: str) -> str:
    """Hermes CLI で収束。出口でレビュー可能な Markdown を保証する。"""
    if not is_hermes_available():
        raise RuntimeError(
            "Hermes CLI が見つかりません。"
            "Railway 上で Hermes をインストールし、"
            "hermes auth add xai-oauth --no-browser で Grok にログインしてください。"
            f"（設定: HERMES_LLM={settings.hermes_llm}）"
        )

    prompt = HERMES_CONVERGE_PROMPT.format(
        draft_v0=draft_v0, item_id=item_id, title=title
    )
    raw = ask(prompt)
    return _ensure_reviewable_form(raw, item_id=item_id, title=title)
