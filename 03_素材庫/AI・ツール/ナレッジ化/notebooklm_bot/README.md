# NotebookLM 自動化ボット

YouTube動画のナレッジ化を **NotebookLM（無料）** で行い、結果を **mdファイル** として保存するPythonスクリプトです。  
CursorのAI枠を消費せず、Playwrightがブラウザを操作します。

## 前提

- macOS / Python 3.10+
- Googleアカウント（NotebookLM利用可能）
- **初回だけ** 手動でGoogleログインが必要

## セットアップ

```bash
cd 03_素材庫/AI・ツール/ナレッジ化/notebooklm_bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

または:

```bash
./run.sh setup
```

## 使い方

### 1. ログイン（初回のみ）

```bash
python -m src.main login
# または ./run.sh login
```

ブラウザが開く → Googleログイン → ターミナルで Enter

### 2. ソース一括追加（任意・推奨）

```bash
python -m src.main add-sources --batch 01
```

`_urls_all.txt` のURLを NotebookLM ノートブック `かくじかん_batch01` に追加します。

### 3. 1本試作

```bash
python -m src.main run --no 001
# または ./run.sh run-one 001
```

出力: `../かくじかん/001_*.md`

### 4. 全本処理

```bash
python -m src.main run --all
# または ./run.sh run-all
```

中断しても `state/progress.json` から再開できます。

## 設定

`config.yaml` を編集:

| 項目 | 説明 |
|------|------|
| `channel_slug` | チャンネル名（mdの基本情報に記載） |
| `notebooklm.notebook_name` | NotebookLMのノートブック名 |
| `paths.urls_file` | 動画一覧（タイトル\|URL） |
| `paths.output_dir` | md保存先 |
| `runtime.headless` | `false`=画面表示（安定）、`true`=裏実行 |

**次のYouTuberへ切替:**

1. `config.yaml` の `channel_slug` / `paths` / `notebook_name` を変更
2. `state/progress.json` と `state/notebook_url.txt` を削除（または state フォルダを空に）
3. 上記手順を繰り返す

## トラブル時

- **「ソースを追加」が見つからない** → `state/notebook_url.txt` を空にして再実行（ホームURLが保存されている場合）
- UIが変わって動かない → `src/selectors.py` のテキスト・セレクタを更新
- 失敗時の画面 → `state/screenshots/` を確認
- 再ログイン → `python -m src.main login`

## ファイル構成

```
notebooklm_bot/
├── config.yaml
├── prompts/video_note.txt
├── src/
│   ├── main.py          # CLI
│   ├── auth.py          # ログイン
│   ├── notebooklm.py    # NotebookLM操作
│   ├── pipeline.py      # バッチ処理
│   ├── md_writer.py     # md保存
│   └── selectors.py     # UIセレクタ（ここを直す）
└── state/               # 進捗・ブラウザプロファイル（gitignore）
```
