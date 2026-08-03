from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .auth import interactive_login
from .config_loader import load_config
from .pipeline import run_add_sources, run_pipeline
from .transcript import extract_video_id, get_youtube_transcript
from .transcript_pipeline import run_transcript_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="NotebookLM 自動化 — YouTube動画をmd化",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="config.yaml のパス（省略時はプロジェクト直下）",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("login", help="Googleログイン（初回のみ）")

    add_src = sub.add_parser("add-sources", help="YouTubeソースをNotebookLMに追加")
    add_src.add_argument("--batch", default="01", help="バッチ番号（01=1〜50本目）")

    run_cmd = sub.add_parser("run", help="プロンプト送信→md保存")
    run_cmd.add_argument("--no", dest="video_no", help="1本指定（例: 001）")
    run_cmd.add_argument("--from", dest="from_no", help="開始番号（例: 002）")
    run_cmd.add_argument("--to", dest="to_no", help="終了番号（例: 010）")
    run_cmd.add_argument("--all", action="store_true", help="未処理をすべて")

    fetch = sub.add_parser("fetch-transcript", help="YouTube文字起こしを取得（テスト用）")
    fetch.add_argument("--url", required=True, help="YouTube URL または動画 ID")

    t_run = sub.add_parser("transcript-run", help="文字起こし+Gemini→md保存")
    t_run.add_argument("--no", dest="video_no", help="1本指定（例: 001）")
    t_run.add_argument("--from", dest="from_no", help="開始番号")
    t_run.add_argument("--to", dest="to_no", help="終了番号")
    t_run.add_argument("--all", action="store_true", help="未処理をすべて")

    return parser


def cmd_fetch_transcript(url: str) -> int:
    video_id = extract_video_id(url)
    print(f"動画ID: {video_id} の文字起こしを取得中...")
    text = get_youtube_transcript(url)
    print("\n--- 取得結果（先頭500文字） ---")
    print(text[:500])
    print("\n-------------------------------------")
    print(f"総文字数: {len(text)} 文字")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "fetch-transcript":
        try:
            return cmd_fetch_transcript(args.url)
        except Exception as exc:
            print(f"失敗: {exc}")
            return 1

    config = load_config(args.config)

    if args.command == "login":
        interactive_login(config)
        return 0

    if args.command == "add-sources":
        run_add_sources(config, batch=args.batch)
        return 0

    if args.command == "run":
        if not any([args.video_no, args.from_no, args.to_no, args.all]):
            parser.error("run には --no, --from/--to, または --all のいずれかが必要です")
        run_pipeline(
            config,
            video_no=args.video_no,
            from_no=args.from_no,
            to_no=args.to_no,
            run_all=args.all,
        )
        return 0

    if args.command == "transcript-run":
        if not any([args.video_no, args.from_no, args.to_no, args.all]):
            parser.error(
                "transcript-run には --no, --from/--to, または --all のいずれかが必要です"
            )
        run_transcript_pipeline(
            config,
            video_no=args.video_no,
            from_no=args.from_no,
            to_no=args.to_no,
            run_all=args.all,
        )
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
