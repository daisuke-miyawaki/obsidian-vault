# 引き継ぎ：Sura×Asura For AI Agent｜NotebookLM上限対策と再開

**作成日：2026-07-03**  
**目的：** 新チャットで上限改善を検討し、残り動画のナレッジ化を再開するための正本。

**新チャットで最初に読むファイル（この順）：**
1. 本ファイル
2. `02_活動基盤/運用/プレイブック_YouTube動画ナレッジ化.md`
3. `02_活動基盤/運用/作業ログ_YouTubeナレッジ化.md`

---

## 1. いま何をしているか（一言）

YouTubeチャンネル **「Sura×Asura For AI Agent」** の厳選12本を、**NotebookLM＋自動スクリプト**で「厚いAI向けMarkdown」に変換中。  
**12本中、実質完了は9本。残り4本（002再取得含む）が未完了。** ボトルネックは **NotebookLMの1日チャット上限**。

---

## 2. 進捗一覧（2026-07-03時点）

| No | タイトル（短縮） | progress.json | mdファイル | 備考 |
|----|------------------|---------------|------------|------|
| 001 | Codex新機能・スマホ監督 | done | あり（24KB） | OK |
| 002 | AI会社運営 #0・Asura-AI始動 | done | **0バイト（空ファイル）** | **要再取得** |
| 003 | Grok×Hermes常駐エージェント | done | あり（24KB） | OK |
| 004 | Open Design×Codex | done | あり（29KB） | OK |
| 005 | Grok Build CLI | done | あり（25KB） | OK |
| 006 | Codex Sites | done | あり（29KB） | OK |
| 007 | Hermes×MCPリサーチャー | done | あり（28KB） | OK |
| 008 | Hermes Desktop GUI | **failed** | なし | 上限で失敗 |
| 009 | HermesのMCP | done | あり（17KB） | OK |
| 010 | Claude Codeサブエージェント | done | あり（17KB） | OK |
| 011 | Loop Engineering | **failed** | なし | 上限で失敗 |
| 012 | Codex Record & Replay | **failed** | なし | 上限で失敗 |

**再開の優先順位（推奨）：**
1. `002`（空ファイルのため再取得）
2. `008` → `011` → `012`（上限失敗分）

---

## 3. ファイル・パス（全部ここ）

```
ワークスペースルート: /Volumes/MultiPurpose_SSD/AI関連/

【成果物】
03_素材庫/YouTube/Sura×Asura_For_AI_Agent/
├── 001_〜010_*.md          … 完了分（002のみ空）
├── _urls_all.txt           … 12本の タイトル|URL 一覧
└── _index.md               … 進捗表（mdリンクは未更新の行あり）

【自動化スクリプト】
03_素材庫/YouTube/notebooklm_bot/
├── config.yaml             … チャンネル設定（現在Sura向け）
├── run.sh                  … 実行入口
├── prompts/video_note_ai.txt … AI向け厚いプロンプト（正本）
├── src/
│   ├── notebooklm.py       … NotebookLM操作・上限検知
│   ├── md_writer.py        … 保存時整形（H3章・太字小項目）
│   ├── pipeline.py
│   └── selectors.py
└── state/
    ├── progress.json       … 進捗（再開の正本）
    ├── notebook_url.txt    … 使用中ノートブックURL
    ├── screenshots/        … 失敗時スクショ
    └── sura_run_*.log      … 実行ログ

【運用ドキュメント】
02_活動基盤/運用/
├── プレイブック_YouTube動画ナレッジ化.md
├── 作業ログ_YouTubeナレッジ化.md
└── 引き継ぎ_Sura×Asura_上限対策_2026-07-03.md  … 本ファイル
```

---

## 4. config.yaml（現在の設定・変更不要）

```yaml
channel_slug: Sura×Asura For AI Agent
taxonomy: AI / エージェント開発 / Sura×Asura
notebooklm:
  notebook_name: Sura×Asura AI 12本
paths:
  urls_file: ../Sura×Asura_For_AI_Agent/_urls_all.txt
  output_dir: ../Sura×Asura_For_AI_Agent
  index_file: ../Sura×Asura_For_AI_Agent/_index.md
  prompt_file: prompts/video_note_ai.txt
runtime:
  headless: false
  reply_timeout_sec: 1200
  delay_between_videos_sec: 60
  max_retries: 3
```

---

## 5. NotebookLMの状態

| 項目 | 値 |
|------|-----|
| ノートブック名 | `Sura×Asura AI 12本` |
| URL | `https://notebooklm.google.com/notebook/893f7f8d-c240-45ca-8696-b65c028db642` |
| ソース | 12本すべて追加済み（`progress.json` の `sources_added`） |
| ログイン | `state/browser_profile` にCookie保存済み。切れたら `./run.sh login` |

---

## 6. 残り動画のURL（再開用）

```
008|https://www.youtube.com/watch?v=jVtNl6-XxLQ
011|https://www.youtube.com/watch?v=aiQJ98bYoYM
012|https://www.youtube.com/watch?v=E6kbf6tnDOg
002|https://www.youtube.com/watch?v=umw_8X7zSro
```

---

## 7. 成果物の形式（ユーザー確定済み・変えない）

### 7-1. 中身の濃さ（isaより厚い・AI向け）
- 目安 **8,000字以上**（短くても5,000字）
- 章 **10〜15個**
- ツール名・コマンド・手順・比較表を残す
- プロンプト正本：`prompts/video_note_ai.txt`

### 7-2. 見た目のルール（2026-07-02確定）
| 要素 | 書き方 | 空行 |
|------|--------|------|
| **章** | `### 1. タイトル`（H3） | **章の前に1行空ける** |
| **小項目** | `**ポイント**` `**注意点**` `**手順**` `**例**`（太字） | **空けない**（本文のすぐ下） |
| 目次 | `### 目次` ＋ `-` 箇条書き | — |
| 用語一覧・トピック一覧 | `###` 見出し | 章扱いで前に空行 |

### 7-3. 自動整形（NotebookLM後処理）
- `src/md_writer.py` の `format_structured_ai_note()` が保存時に適用
- `prompt_file` 名に `video_note_ai` を含むとき自動ON
- **見た目の修正はNotebookLM再取得不要**（ローカル整形で足りる）

---

## 8. 上限問題の経緯と事実

### 8-1. 2026-07-02の一括処理（005〜012）
- 005〜007：成功
- **008：上限で失敗**（3回リトライすべて失敗）
- 009：成功（008直後なのに成功＝上限は「厳しめ」でブレる）
- 010：成功
- **011・012：上限で失敗**

### 8-2. 同様の先例（isaさん案件・2026-06-30）
- 同一ノートブックにチャットが溜まると「答えられません」
- リトライを繰り返すと **1日の上限** に到達
- 対策として実装済み：
  - 質問前のチャット履歴削除（`notebooklm.py` → `_start_new_chat()`）
  - 上限メッセージの即検知（15分待たない）
  - 新ノートブック作成（isa 012で `isaさん17本_v2` に切替して成功）

### 8-3. 上限の見分け方
- エラーメッセージ：`NotebookLM の1日のチャット上限に達しました`
- スクショ：`state/screenshots/response_rate_limit.png`
- **その日は同じアカウントで続行しても無駄**（リトライ3回は枠を消費するだけ）

### 8-4. ざっくり目安（経験則）
- **厚いAIプロンプト**は1日 **5〜7本** 程度で上限に近づく
- 1ノートブックに12ソース＋12回チャットは負荷が高い
- リセットは日付変更後（太平洋時間0時頃＝日本時間 **16〜17時ごろ** のことが多い）

---

## 9. 上限改善の検討案（新チャットの主題）

優先度順。**ユーザーOK後に実装。**

| 案 | 内容 | メリット | デメリット |
|----|------|----------|------------|
| **A. 1動画1ノートブック** | 008/011/012それぞれ新規ノートブック＋ソース1本だけ | チャット履歴の干渉ゼロ。isaで実績あり | ノートブックが増える |
| **B. 上限検知で即停止** | `max_retries`を上限時は0に。パイプライン全体を止める | 無駄なリトライを防ぐ | コード変更が必要 |
| **C. 1日の本数上限** | 設定で `daily_max_chats: 5` 等。超えたら翌日まで待つ | 運用が安定 | 完了が遅れる |
| **D. プロンプト2段階** | ①要約のみ ②詳細のみの2チャットに分割 | 1回あたりの負荷軽減 | 実装・手順が複雑 |
| **E. NotebookLM有料プラン** | Google側の上限引き上げ | 根本解決の可能性 | コスト |
| **F. 間隔延長** | `delay_between_videos_sec` を 120〜300 に | 簡単 | 効果は限定的 |

**推奨コンボ：** A（残りは1本1ノートブック）＋ B（上限時リトライしない）＋ 1日最大5本

### 9-1. 案Aの実装イメージ（008の例）
1. `config.yaml` の `notebook_name` を `Sura 008 Hermes Desktop` に変更
2. `state/notebook_url.txt` を削除（新規ノートブック作成を促す）
3. `progress.json` は**消さない**（008だけ failed のまま再実行）
4. `./run.sh run-one 008` … ソースはノートブック内に無ければ自動追加

---

## 10. 再開手順（そのまま実行可）

```bash
cd "/Volumes/MultiPurpose_SSD/AI関連/03_素材庫/YouTube/notebooklm_bot"
source .venv/bin/activate

# 古いブラウザが残っていたら
pkill -f "notebooklm_bot/state/browser_profile" 2>/dev/null

# Playwright未インストール時（Cursor新環境では毎回必要なことがある）
playwright install chromium

# 1本ずつ（forループ一括は上限時に無駄が多い）
./run.sh run-one 002   # 空ファイルの再取得
sleep 90
./run.sh run-one 008
sleep 90
./run.sh run-one 011
sleep 90
./run.sh run-one 012
```

**002を再取得する場合：** `progress.json` の 002 を `done` のままだと上書き保存はされるが、問題なければそのまま実行可。気になる場合は002の status を手動で `pending` に戻す。

**上限メッセージが出たら：** その日は打ち切り。翌日まで待つ。

---

## 11. 新チャットへの貼り付け用プロンプト

以下を新チャットの最初のメッセージにコピペ：

```
【作業再開：Sura×Asura YouTubeナレッジ化＋NotebookLM上限対策】

読んでほしいファイル：
1. 02_活動基盤/運用/引き継ぎ_Sura×Asura_上限対策_2026-07-03.md
2. 02_活動基盤/運用/プレイブック_YouTube動画ナレッジ化.md

目的：
- NotebookLMの1日チャット上限で止まっている問題を改善する
- 残り動画のナレッジ化を完了する（002再取得、008、011、012）

現状：
- 12本中9本相当完了。002のmdが0バイトで要再取得
- 上限改善案は引き継ぎファイル第9章を参照
- 成果物形式（H3章＋太字小項目）は変えない

まず上限対策（案A+B推奨）を実装してから、002→008→011→012を1本ずつ処理してください。
```

---

## 12. 触ってはいけないもの

- `01_人生戦略OS/` 配下（OSコア）に成果物を入れない
- 4桁番号の勝手な変更
- 上限中の `for` ループ一括＋3回リトライ（枠の無駄遣い）
- isa・かくじかんの `config.yaml` / `progress.json` を上書きしない（Sura作業中はSura用のまま）

---

## 13. 過去チャンネル実績（参考）

| チャンネル | 本数 | 状態 | プロンプト |
|------------|------|------|------------|
| かくじかん | 38 | 完了 | `video_note.txt` |
| isaさん | 17 | 完了 | `video_note_isa.txt`（抽象・引き寄せ） |
| Sura×Asura | 12 | **進行中** | `video_note_ai.txt`（厚い・AI向け） |

---

## 14. 更新履歴

| 日付 | 内容 |
|------|------|
| 2026-07-03 | 初版。002空ファイル発見。上限対策案を整理 |
| 2026-07-03 | **案A+B実装完了**：`notebook_per_video: true`、`daily_max_chats: 5`、上限時リトライなし即停止 |
