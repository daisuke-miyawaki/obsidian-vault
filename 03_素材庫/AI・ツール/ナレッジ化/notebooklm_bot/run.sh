#!/usr/bin/env bash
# NotebookLM 自動化 — よく使うコマンド
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -q -r requirements.txt

CONFIG="${CONFIG:-config.yaml}"

case "${1:-help}" in
  setup)
    playwright install chromium
    echo "セットアップ完了"
    ;;
  login)
    python -m src.main login
    ;;
  add-sources)
    python -m src.main add-sources --batch "${2:-01}"
    ;;
  run-one)
    python -m src.main run --no "${2:-001}"
    ;;
  run-all)
    python -m src.main run --all
    ;;
  fetch-transcript)
    python -m src.main fetch-transcript --url "${2:?URLを指定してください}"
    ;;
  transcript-one)
    python -m src.main --config "$CONFIG" transcript-run --no "${2:-001}"
    ;;
  transcript-all)
    python -m src.main --config "$CONFIG" transcript-run --all
    ;;
  *)
    echo "使い方:"
    echo "  ./run.sh setup       # 初回: Playwright Chromium インストール"
    echo "  ./run.sh login       # Googleログイン（初回のみ）"
    echo "  ./run.sh add-sources # 全URLをNotebookLMに追加"
    echo "  ./run.sh run-one 001 # 1本試作"
    echo "  ./run.sh run-all     # 未処理をすべて"
    echo "  ./run.sh fetch-transcript URL  # 文字起こし取得テスト"
    echo "  ./run.sh transcript-one 001  # 文字起こし+Gemini→md（1本）"
    echo "  ./run.sh transcript-all      # 未処理をすべて（文字起こしルート）"
    echo ""
    echo "  カテゴリ別 config 例:"
    echo "    CONFIG=config.未分類.yaml ./run.sh transcript-one 001"
    echo "    CONFIG=config.AIエージェント.yaml ./run.sh transcript-one 001"
    echo "    CONFIG=config.自己観察さん.yaml ./run.sh transcript-one 001"
    echo "    CONFIG=config.桑田さん.yaml ./run.sh transcript-one 001"
    echo ""
    echo "  ※ transcript-* は GEMINI_API_KEY が必要（.env または環境変数）"
    ;;
esac
