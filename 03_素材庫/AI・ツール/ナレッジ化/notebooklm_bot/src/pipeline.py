from __future__ import annotations

import time
from dataclasses import replace

from .auth import with_browser
from .config_loader import AppConfig
from .daily_tracker import DailyChatTracker
from .exceptions import RateLimitError
from .md_writer import VideoEntry, build_md_filename, parse_urls_file, save_video_md, sanitize_filename, update_index
from .notebooklm import NotebookLMClient
from .progress import ProgressStore


def load_prompt(config: AppConfig, title: str) -> str:
    template = config.prompt_file.read_text(encoding="utf-8")
    return template.format(title=title)


def is_rate_limit_error(exc: BaseException) -> bool:
    if isinstance(exc, RateLimitError):
        return True
    return "1日のチャット上限" in str(exc)


def config_for_video(base: AppConfig, video: VideoEntry) -> AppConfig:
    """1動画1ノートブックモード用に設定を差し替える。"""
    if not base.notebook_per_video:
        return base
    short_title = sanitize_filename(video.title, max_len=25)
    notebook_name = f"Sura {video.no} {short_title}"
    return replace(base, notebook_name=notebook_name)


def reset_notebook_url(config: AppConfig) -> None:
    """保存済みURLを消し、次の動画で新規ノートブックを作る。"""
    if config.notebook_url_file.exists():
        config.notebook_url_file.unlink()
        print("  ノートブックURLをリセット（新規作成）")


def filter_videos(
    videos: list[VideoEntry],
    *,
    video_no: str | None = None,
    from_no: str | None = None,
    to_no: str | None = None,
    all_pending: bool = False,
    progress: ProgressStore | None = None,
) -> list[VideoEntry]:
    result = videos
    if video_no:
        result = [v for v in result if v.no == video_no.zfill(3)]
    if from_no:
        result = [v for v in result if v.no >= from_no.zfill(3)]
    if to_no:
        result = [v for v in result if v.no <= to_no.zfill(3)]
    if all_pending and progress:
        result = [v for v in result if progress.get_status(v.no) != "done"]
    return result


def run_add_sources(config: AppConfig, batch: str | None = None) -> None:
    videos = parse_urls_file(config.urls_file)
    progress = ProgressStore(config.progress_file)

    if batch:
        batch_num = int(batch)
        start = (batch_num - 1) * config.batch_size
        end = start + config.batch_size
        videos = videos[start:end]

    urls = [v.url for v in videos if not progress.is_source_added(v.url)]
    if not urls:
        print("追加するソースはありません（すべて登録済み）")
        return

    print(f"ソース {len(urls)} 件を NotebookLM に追加します ...")
    with with_browser(config) as (_, __, page):
        client = NotebookLMClient(page, config)
        client.ensure_notebook(config.notebook_name)
        for url in urls:
            try:
                client.add_youtube_urls([url])
                progress.add_source_url(url)
                print(f"  追加: {url}")
            except Exception as exc:
                client.screenshot(f"add_source_fail_{urls.index(url)}")
                print(f"  失敗: {url} ({exc})")
                raise


def process_video(
    config: AppConfig,
    video: VideoEntry,
    progress: ProgressStore,
    daily: DailyChatTracker,
) -> None:
    if not daily.can_chat(config.daily_max_chats):
        limit = config.daily_max_chats
        raise RateLimitError(
            f"本日のチャット上限（設定値 {limit} 本）に達しました。明日以降に再開してください。"
        )

    video_config = config_for_video(config, video)
    if config.notebook_per_video:
        reset_notebook_url(video_config)

    prompt = load_prompt(video_config, video.title)
    last_error: Exception | None = None
    max_retries = video_config.max_retries

    for attempt in range(1, max_retries + 1):
        try:
            print(
                f"[{video.no}] 処理中 (試行 {attempt}/{max_retries}): {video.title}"
            )
            if video_config.notebook_per_video:
                print(f"  ノートブック: {video_config.notebook_name}")

            with with_browser(video_config) as (_, __, page):
                client = NotebookLMClient(page, video_config)
                try:
                    client.add_youtube_urls([video.url])
                    if not progress.is_source_added(video.url):
                        progress.add_source_url(video.url)
                    response = client.ask(
                        prompt,
                        source_title=video.title,
                        source_url=video.url,
                    )
                except Exception:
                    client.screenshot(f"fail_{video.no}_attempt{attempt}")
                    raise

            md_path = save_video_md(video_config, video, response)
            update_index(video_config, video, md_path)
            progress.mark(video.no, "done", md_file=str(md_path.name))
            daily.record_chat()
            print(f"[{video.no}] 完了 -> {md_path.name}")
            if config.daily_max_chats:
                print(
                    f"  本日のチャット: {daily.count()}/{config.daily_max_chats}"
                )
            return
        except Exception as exc:
            last_error = exc
            progress.mark(video.no, "failed", error=str(exc), attempt=str(attempt))
            print(f"[{video.no}] 失敗: {exc}")

            if is_rate_limit_error(exc):
                print("  上限検知 → リトライせず停止")
                raise RateLimitError(str(exc)) from exc

            if attempt < max_retries:
                time.sleep(3)

    raise RuntimeError(f"[{video.no}] 最大リトライ回数を超えました: {last_error}")


def run_pipeline(
    config: AppConfig,
    *,
    video_no: str | None = None,
    from_no: str | None = None,
    to_no: str | None = None,
    run_all: bool = False,
) -> None:
    videos = parse_urls_file(config.urls_file)
    progress = ProgressStore(config.progress_file)
    daily = DailyChatTracker(config.state_dir / "daily_chats.json")
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

    if config.daily_max_chats:
        print(
            f"本日のチャット: {daily.count()}/{config.daily_max_chats} "
            f"（太平洋時間の日付でカウント）"
        )

    print(f"処理対象: {len(targets)} 本")
    if config.notebook_per_video:
        print("モード: 1動画1ノートブック")

    failed: list[str] = []
    for i, video in enumerate(targets):
        if progress.get_status(video.no) == "done" and not video_no:
            md_path = config.output_dir / build_md_filename(video)
            if md_path.exists() and md_path.stat().st_size > 0:
                print(f"[{video.no}] スキップ（完了済み）")
                continue
            print(f"[{video.no}] 再取得（mdが空または欠落）")

        try:
            process_video(config, video, progress, daily)
        except RateLimitError as exc:
            failed.append(video.no)
            print(f"\n⚠ 上限でパイプライン停止: {exc}")
            print("  明日以降に run-one で再開してください。")
            break
        except Exception as exc:
            failed.append(video.no)
            print(f"[{video.no}] バッチ継続（失敗）: {exc}")

        if i < len(targets) - 1:
            time.sleep(config.delay_between_videos_sec)

    if failed:
        print(f"パイプライン完了（失敗: {', '.join(failed)}）")
    else:
        print("パイプライン完了")
