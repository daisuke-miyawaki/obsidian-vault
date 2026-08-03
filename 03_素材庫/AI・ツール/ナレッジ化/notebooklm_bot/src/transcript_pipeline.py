from __future__ import annotations

import time
from pathlib import Path

from .config_loader import AppConfig
from .daily_tracker import DailyChatTracker
from .gemini_client import (
    GeminiRateLimitError,
    check_daily_quota,
    generate_markdown,
)
from .md_writer import (
    VideoEntry,
    build_md_filename,
    parse_urls_file,
    save_video_md,
    update_index,
)
from .pipeline import filter_videos
from .progress import ProgressStore
from .transcript import get_youtube_transcript


def transcript_progress_file(config: AppConfig) -> Path:
    """チャンネルフォルダ内の progress.json（Sura の state/ と分離）。"""
    return config.output_dir / "progress.json"


def build_transcript_prompt(config: AppConfig, video: VideoEntry, transcript: str) -> str:
    template = config.prompt_file.read_text(encoding="utf-8")
    instruction = template.format(title=video.title)
    return (
        f"{instruction}\n\n"
        "【文字起こしテキスト（YouTube自動字幕・誤字・脱字あり）】\n"
        f"{transcript}\n\n"
        "上記の文字起こしを根拠に、誤字・脱字・[音楽]などのノイズを補正しながら、"
        "指定フォーマットの Markdown のみを出力してください。"
    )


def process_video_transcript(
    config: AppConfig,
    video: VideoEntry,
    progress: ProgressStore,
    gemini_daily: DailyChatTracker,
) -> None:
    check_daily_quota(config, gemini_daily)

    print(f"[{video.no}] 文字起こし取得中: {video.title}")
    transcript = get_youtube_transcript(video.url)
    print(f"  文字数: {len(transcript)}")

    prompt = build_transcript_prompt(config, video, transcript)
    print(f"[{video.no}] Gemini で Markdown 生成中（{config.gemini_model}）...")
    body = generate_markdown(config, prompt)

    md_path = save_video_md(config, video, body)
    update_index(config, video, md_path)
    progress.mark(video.no, "done", md_file=str(md_path.name))
    gemini_daily.record_chat()

    print(f"[{video.no}] 完了 -> {md_path.name}")
    if config.gemini_daily_max_requests:
        from .gemini_client import effective_daily_max

        limit = effective_daily_max(config)
        print(
            f"  本日の Gemini: {gemini_daily.count()}/{limit}"
        )


def run_transcript_pipeline(
    config: AppConfig,
    *,
    video_no: str | None = None,
    from_no: str | None = None,
    to_no: str | None = None,
    run_all: bool = False,
) -> None:
    videos = parse_urls_file(config.urls_file)
    progress = ProgressStore(transcript_progress_file(config))
    gemini_daily = DailyChatTracker(config.state_dir / "gemini_daily.json")

    targets = filter_videos(
        videos,
        video_no=video_no,
        from_no=from_no,
        to_no=to_no,
        all_pending=run_all,
        progress=progress,
    )

    if not targets:
        print("処理対象の動画がありません")
        return

    if config.gemini_daily_max_requests:
        from .gemini_client import collect_api_keys, effective_daily_max

        key_count = len(collect_api_keys(config))
        limit = effective_daily_max(config)
        print(
            f"本日の Gemini: {gemini_daily.count()}/{limit} "
            f"（{key_count}キー × {config.gemini_daily_max_requests}本/日）"
        )

    print(f"処理対象: {len(targets)} 本（文字起こし + Gemini）")
    failed: list[str] = []

    for i, video in enumerate(targets):
        if progress.get_status(video.no) == "done" and not video_no:
            md_path = config.output_dir / build_md_filename(video)
            if md_path.exists() and md_path.stat().st_size > 0:
                print(f"[{video.no}] スキップ（完了済み）")
                continue
            print(f"[{video.no}] 再取得（mdが空または欠落）")

        try:
            process_video_transcript(config, video, progress, gemini_daily)
        except GeminiRateLimitError as exc:
            failed.append(video.no)
            progress.mark(video.no, "failed", error=str(exc))
            print(f"\n⚠ Gemini 上限で停止: {exc}")
            break
        except Exception as exc:
            failed.append(video.no)
            progress.mark(video.no, "failed", error=str(exc))
            print(f"[{video.no}] 失敗: {exc}")

        if i < len(targets) - 1:
            time.sleep(config.gemini_delay_sec)

    if failed:
        print(f"パイプライン完了（失敗: {', '.join(failed)}）")
    else:
        print("パイプライン完了")
