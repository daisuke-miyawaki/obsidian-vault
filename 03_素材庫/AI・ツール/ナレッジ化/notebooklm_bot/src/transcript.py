"""YouTube URL から文字起こしテキストを取得する（NotebookLM 不要）"""

from __future__ import annotations

import re

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    NoTranscriptFound,
    TranscriptsDisabled,
)

_VIDEO_ID_PATTERN = re.compile(
    r"(?:v=|\/v\/|youtu\.be\/|\/embed\/|\/shorts\/)([a-zA-Z0-9_-]{11})"
)

# 日本語優先 → 英語の順で試す
_PREFERRED_LANGUAGES = ("ja", "ja-JP", "en")


def extract_video_id(url_or_id: str) -> str:
    """YouTube URL または 11 桁の動画 ID から video_id を取り出す。"""
    value = url_or_id.strip()
    match = _VIDEO_ID_PATTERN.search(value)
    if match:
        return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", value):
        return value
    raise ValueError(f"動画 ID を抽出できません: {url_or_id}")


def _join_snippets(fetched) -> str:
    text = "".join(snippet.text for snippet in fetched)
    return text.replace("\n", " ").strip()


def get_youtube_transcript(video_url: str) -> str:
    """
    YouTube URL から文字起こしテキストを1本の文字列で返す。
    取得できない場合は例外を投げる（エラー文字列は返さない）。
    """
    video_id = extract_video_id(video_url)
    api = YouTubeTranscriptApi()

    try:
        fetched = api.fetch(video_id, languages=list(_PREFERRED_LANGUAGES))
        return _join_snippets(fetched)
    except NoTranscriptFound:
        pass

    # 明示的な言語指定で見つからないとき、利用可能な字幕を探す
    transcript_list = api.list(video_id)
    for finder in (
        lambda: transcript_list.find_transcript(["ja", "ja-JP"]),
        lambda: transcript_list.find_generated_transcript(["ja", "ja-JP"]),
        lambda: transcript_list.find_transcript(["en"]),
        lambda: transcript_list.find_generated_transcript(["en"]),
    ):
        try:
            transcript = finder()
            return _join_snippets(transcript.fetch())
        except NoTranscriptFound:
            continue

    raise NoTranscriptFound(
        video_id,
        _PREFERRED_LANGUAGES,
        transcript_list,
    )


def get_youtube_transcript_safe(video_url: str) -> str:
    """CLI 向け。失敗時は読みやすいメッセージの文字列を返す。"""
    try:
        return get_youtube_transcript(video_url)
    except TranscriptsDisabled:
        return "エラー: この動画では字幕（文字起こし）が無効化されています。"
    except NoTranscriptFound:
        return "エラー: 日本語・英語の字幕が見つかりませんでした。"
    except CouldNotRetrieveTranscript as exc:
        return f"エラー: {exc.cause or exc}"
    except ValueError as exc:
        return f"エラー: {exc}"
    except Exception as exc:
        return f"予期せぬエラーが発生しました: {exc}"
