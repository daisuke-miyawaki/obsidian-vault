# 作業ログ：マルチエージェント × VPS

## このファイルの目的

LangGraph系マルチエージェントアプリと、Xserver VPSへの設置・公開・Vault連携の**経緯・現状・次の手**を残す。

チャットが切れても、このファイルで再開できる。

**更新ルール：** 区切りのよい作業が終わったら、このファイルの「現状サマリー」と「年表」を追記する（ユーザーのOKなしに新規ログファイルは増やさない。本ファイルを正本にする）。

---

## 現状サマリー（2026-08-09）

| 項目 | 内容 |
|------|------|
| **アプリ置き場（Mac）** | `/Users/miyawakidaisuke/Desktop/自分のマルチエージェント構築/` |
| **使い方メモ（短い）** | 同フォルダの `使い方.md` |
| **Vault（Mac／正本）** | `/Volumes/MultiPurpose_SSD/DigitalGarden`（旧名 AI関連） |
| **VPS** | Xserver VPS / Ubuntu 24.04 / IP `162.43.4.234` |
| **VPSアプリ** | `/opt/multiagent`（Docker Compose・コンテナ名 multiagent） |
| **VPS Vault** | `/opt/multiagent/vault`（**Git化済み**。GitHub `obsidian-vault` を5分ごと pull） |
| **同期スクリプト** | `/opt/multiagent/bin/vault-pull.sh`（cron `*/5`）。Mac写し: `scripts/vault-pull.sh` |
| **Deploy key** | VPS `/root/.ssh/obsidian-vault-deploy`（GitHubは読取専用） |
| **API** | `/health`・`/invoke`（キー必須）・`/chat/send`（共有パスワード） |
| **チャットUI** | `https://aix.sunnysh.net/chat`（**AIX**。Jarvis表記なし。プレビューURLは削除済み） |
| **認証** | `CHAT_PASSWORD` + `X-Chat-Password`。Unlockゲートあり |
| **外公開** | `https://aix.sunnysh.net`（Caddy・Let's Encrypt） |
| **SSH（手動）** | ユーザー `root`／鍵 `~/.ssh/xserver-vps.pem`／IP `162.43.4.234` |
| **Cursor Remote SSH** | **完了**（2026-08-09）。Host `xserver-vps` → `/opt/multiagent`。画面に `SSH: xserver-vps`／`multiagent` |
| **Aider（VPS）** | **導入済み**（2026-08-09）。`aider 0.86.2`／モデル `gemini/gemini-2.5-flash-lite`／起動 `bin/aider-start.sh`。常時稼働しない |
| **取得まわり** | 顧客名→フォルダ／MOC＋wikilink 1〜2ホップ。住所3社OK |
| **Core** | **毎回の invoke でディスク再読込**（起動時固定を廃止） |
| **リサーチ** | `RESEARCH_BACKEND=open_deep_research` + `TAVILY_API_KEY` |
| **提案** | `single_shot`。顧客ノート優先。内部「仮実装」文言は出さない |
| **コード反映** | `/opt/multiagent/app` を `/app/app:ro`。再起動で反映（deps変更時のみ build） |
| **総合確認** | `scripts/smoke_vps_core.sh` → **ALL_OK**（2026-08-09） |
| **まだやっていない** | Aiderの短い半自動ループ実運用／Webhook即時反映／分野キーワードの追加整備 |

---

## いまの更新の流れ（実態）

```text
[Mac] DigitalGarden
  └─ Obsidian Git → GitHub（非公開：obsidian-vault）※キー類はGit対象外

[VPS] /opt/multiagent
  ├─ Docker でアプリ起動（Vault=/app/vault:ro、app=/app/app:ro）
  ├─ cron */5：vault-pull.sh（git fetch + reset --hard origin/main）
  └─ チャット https://aix.sunnysh.net/chat（AIX UI）
```

**メモ:** pull 中の半端読みは理論上ありうるが、利用量・reset短時間のため**経過観察**（flock等は未導入）。

---

## Cursor Remote SSH（接続メモ・2026-08-09）

**目的：** PCのCursorからVPS上の作業フォルダを開き、Cursor内ターミナルもVPS側で動くようにする。  
**この節の範囲：** Remote SSH の初回セットアップのみ。  
**次の一手（リサーチ合意）：** Aider（短い半自動ループ）。OpenHands・Cron 24h・常時稼働は後回し。別チャットで進めてよい。

### 接続に使うもの（確定済み）

| 項目 | 値 | 根拠 |
|------|-----|------|
| VPSのIP | `162.43.4.234` | 現状サマリー／手動SSH履歴 |
| OS | Ubuntu 24.04 | 現状サマリー |
| ログインユーザー | `root` | Macの `~/.zsh_history` で一貫して `root@162.43.4.234` |
| 秘密鍵（Mac） | `~/.ssh/xserver-vps.pem` | 存在確認済み（権限 `-rw-------`） |
| 手動SSHの例 | `ssh -i ~/.ssh/xserver-vps.pem -o IdentitiesOnly=yes root@162.43.4.234` | 履歴どおり |
| Macの `~/.ssh/config` | **作成済み**（2026-08-09）。Host名 `xserver-vps` | 接続確認OK（`ssh xserver-vps`） |
| 接続確認（同日） | 成功。`whoami=root`／ホスト名 `x162-43-4-234` | `BatchMode` で確認 |

### Cursorで開くフォルダ（推奨）

| 候補 | パス | いつ使うか |
|------|------|------------|
| **推奨（今回）** | `/opt/multiagent` | アプリ・compose・`.env`・`bin`・`vault` がまとまっている |
| 狭い範囲だけ | `/opt/multiagent/vault` | Vault写しだけ見たいとき（今回の主目的ではない） |

### 成功条件（全部できたら完了）

1. CursorからVPSに接続できる  
2. ワークスペースが `/opt/multiagent` になっている  
3. Cursor内ターミナルがVPS側である  
4. `hostname` や `pwd` など簡単な確認がVPSで通る  

### いまの進捗

| 段階 | 状態 |
|------|------|
| 接続情報の特定（ユーザー・鍵・フォルダ） | **完了** |
| `~/.ssh/config` 作成 | **完了**（Host `xserver-vps`。手動 `ssh xserver-vps` 成功） |
| Cursor Remote SSH で接続 | **完了**（2026-08-09） |
| `/opt/multiagent` を開く | **完了**（画面タイトル `multiagent [SSH: xserver-vps]`） |
| ターミナルで `hostname`／`pwd` 確認 | **完了相当**（Macから `ssh xserver-vps` で `x162-43-4-234`／`root`／`/opt/multiagent` 確認。Cursor内ターミナルも同接続） |

### `~/.ssh/config` の内容（秘密鍵の中身は書かない）

```text
Host xserver-vps
  HostName 162.43.4.234
  User root
  IdentityFile ~/.ssh/xserver-vps.pem
  IdentitiesOnly yes
```

- 置き場：`~/.ssh/config`（権限 `600`）
- 短縮接続：ターミナルで `ssh xserver-vps`
- Cursor Remote SSH でも、接続先一覧に `xserver-vps` が出る想定

### 再開時の一言（接続済み）

もう一度開くとき：Macのターミナルで  
`/Applications/Cursor.app/Contents/Resources/app/bin/cursor --folder-uri "vscode-remote://ssh-remote+xserver-vps/opt/multiagent"`  
または Cursor 左下の `SSH: xserver-vps` から再接続。

---

## 年表（要点）

### 2026-08頃（Macローカル）

- 仕様書 `system_spec.md` に沿って最小グラフ（supervisor／knowledge／general／proposal／idea／research stub）
- Gemini（複数キー切替）でCLI・FastAPI `/invoke` を確認
- Docker／compose をMacで動作確認（VaultはSSDパスをマウント）

### 2026-08-06（VPS設置）

- SSH接続（タイムアウト→パケットフィルターSSH確認→接続成功）
- Docker Engine 29.7.1／Compose v5.4.0 導入
- アプリを `rsync` で `/opt/multiagent` へ配置
- Vaultを `rsync` で `/opt/multiagent/vault` へ配置（`.git` は除外）
- VPS用 `.env`（API_KEYは乱数。チャットに出した鍵は作り直し済み）
- `docker compose` で起動。VPS内で `/health`・`/invoke` 成功

### 2026-08-06〜07（外から利用）

- API_KEY再発行（チャット露出対策）
- パケットフィルター：TCP 8000・送信元 `60.153.211.62/32`（※自宅IPは変わりうる）
- 外から `/health`・`/invoke` 成功

### 2026-08-07（チャットUI）

- FastAPIに `/chat` 追加（`app/static/chat.html`）
- 最小UI → 当時は Jarvis風デザイン（暗背景・青系）※後に AIX へ改名・再設計
- `/invoke` 接続は維持。ブラウザで送受信確認済み

### 2026-08-07（KnowledgeRetriever：顧客ノートを拾えない不具合）

- **原因1**: 固定 ENTRY_CANDIDATES のみ参照（検索なし）
- **原因2**: Supervisorが knowledge を飛ばすことがあった → 未取得時は必ず knowledge 先行
- **原因3**: 検索が顧客会社概要を安定して返せないことがあった → 既知顧客の会社概要を優先ヒット
- **確認**: 「PRIZMの住所は？」で `〒498-0006 愛知県弥富市佐古木3丁目373-5` が返ることを確認

### 2026-08-08（第一歩：顧客MOC＋リンクたどり）

- **狙い**: Cursor並みではなく「顧客名 → 顧客フォルダ／MOC → リンク先を1〜2回開く」
- **実装（Mac）**: `app/tools/vault.py` に `resolve_wikilink`／`expand_notes_via_wikilinks`。顧客フォルダでは MOC を優先。クリエイト／PINTO の既知代表ノートも追加
- **反映の注意（当時）**: 当初はアプリがイメージ焼き込みのため `build` が必要だった → 同日中にマウント化（下記）
- **確認（VPSチャット）**:
  - PINTO → 津島市の住所を返却（`pinto_tennis_club_knowledge.md`）
  - クリエイト → 名古屋市北区の住所を返却（`株式会社クリエイト.md`）
  - PRIZM → 弥富市の住所を返却（`会社概要.md`）

### 2026-08-08（効率：アプリコードをマウント）

- **原因**: Dockerfile が `COPY app`、compose は Vault のみマウント
- **対応**: VPS `/opt/multiagent/app:/app/app:ro`、Mac `./app:/app/app:ro`
- **確認**: ホスト編集 → `docker compose restart` のみで反映。住所3社チャットOK
- **例外**: `requirements.txt` 変更時のみ `docker compose build`

### 2026-08-08（取得パターンを Core／運用／技術へ）

- **型**: 分野キーワード → 入口MOC／目次 → `[[リンク]]` 1〜2ホップ（顧客100点優先）
- **入口**: Core=`MOC_Core`／運用=`設計ログ_目次`+`プレイブック一覧`／技術=`MOC_素材庫`
- **確認**: User Model／VPS作業ログ／素材庫AIエージェント／PINTO住所

### 2026-08-08（チャット会話継続・最小）

- **変更**: `/chat/send`・`/invoke` に `history`（直近6メッセージ≒3往復）。`user_query` は今回の文のまま
- **画面**: 会話ログ表示・Clear・履歴付き送信
- **確認**: 「PINTOについて」→「住所は？」で住所OK。一問の住所取得もOK。簡単な続き計算もOK

### 2026-08-08（Open Deep Research・第一歩）

- **導入**: `vendor/open_deep_research` clone + editable install。`get_research_backend` 接続
- **単体**: `scripts/run_deep_research.py`（Supervisor／チャット非経由）
- **注意**: 現行公式は検索が **Tavily 必須**。呼び出しは `ainvoke`
- **追記**: `.env` に Tavily 追加。単体1回完走OK

### 2026-08-08（ResearchAgent から ODR 接続）

- **変更**: `RESEARCH_BACKEND=open_deep_research`。Supervisor で住所等は research に回さない旨を明記
- **research_agent**: `user_query` 優先。チャット待ち文言に「数分」を追記
- **Docker**: Dockerfile に vendor の editable install を追加（VPS反映時は build 必要）
- **確認用**: `scripts/verify_research_routing.py`（住所／リサーチ）
- **ローカル確認OK**: 住所=`knowledge→general`／リサーチ=`knowledge→research`・`error=None`・レポート生成
- **VPS反映OK**（`scripts/deploy_odr_to_vps.sh`）: health OK、backend=`OpenDeepResearchBackend`、住所 postal OK、リサーチ `research_agent`・`error=None`
- **待ち時間**: リサーチは数分。チャットは「Processing…（数分）」表示。Caddy／ブラウザのタイムアウトに注意

### 2026-08-08（リサーチ待ち切れ対策）

- **画面**: 経過秒表示＋最大10分で打ち切り（AbortController）
- **Caddy**: reverse_proxy の read/write/response_header を10分（`deploy_research_timeouts.sh`）
- **確認**: 住所 OK／短いリサーチ OK（VPS）

### 2026-08-08（チャット共有パスワード）

- **方式A**: `CHAT_PASSWORD` + ヘッダ `X-Chat-Password`
- **画面**: Unlock ゲート／`/chat/unlock` で確認／`/chat/send` 保護
- **反映**: `scripts/deploy_chat_password.sh`（先に `.env` の `CHAT_PASSWORD` を自分で設定）
- **注意**: `docker compose restart` だけでは `env_file` が再読込されないことがある → パスワード変更時は `up -d --force-recreate`
- **VPS確認OK**: wrong=401／ok=200／no_pw=401／住所送信 postal OK（knowledge→general）

### 2026-08-08（秘密情報・バックアップ最小方針）

**置き場所**
| もの | 置き場 | Git |
|------|--------|-----|
| Mac `.env` | アプリ直下 | 禁止（`.gitignore`） |
| VPS `.env` | `/opt/multiagent/.env` | 禁止 |
| Geminiキー | Vault内 `GEMINI_API_KEY.env`（Git対象外）＋VPSに `/root/GEMINI_API_KEY.env.bak` | 禁止 |
| SSH鍵 | `~/.ssh/xserver-vps.pem` | 禁止 |
| Caddy | `/etc/caddy/Caddyfile`（秘密ほぼなし） | 任意でコピー可 |
| compose/Dockerfile | アプリ／VPS両方 | コミット可（秘密なし） |
| `.env.example` | キー名だけのひな形 | コミット可 |

**バックアップ（最小）**
1. Mac の `.env` を、パスワード管理（または暗号化コピー）に月1で控えを取る  
2. VPS の `.env` も同様（中身をチャットに出さない）  
3. SSH鍵は Mac バックアップ／パスワード管理に1通  
4. Caddyfile は変更したら `/etc/caddy/Caddyfile` をテキスト控え（秘密ほぼなし）  
5. Vault（DigitalGarden）は既存の Obsidian Git。**キーファイルは Git に入れない**

### 2026-08-08（リサーチ結果の読みやすさ）

- **画面**: 最小Markdown表示（見出し・箇条書き・リンク）、長文は折りたたみ、スクロール拡大
- **VPS確認**: 住所 OK／短いリサーチ OK（`deploy_chat_readable.sh`）

### 2026-08-08（再起動後の自動復帰・確認手順）

- compose: `restart: unless-stopped`（アプリコンテナ）
- 確認スクリプト: `scripts/check_vps_autostart.sh`（docker/caddy の `is-enabled` を見て不足なら enable。実再起動はしない）
- **確認OK**: app=`unless-stopped`／docker=`enabled`／caddy=`enabled`／health OK（実再起動は未実施）

### 2026-08-08（総合確認・当時）

- `scripts/smoke_vps_core.sh` → **ALL OK**（当時の項目）

### 2026-08-08（リサーチ連打防止）

- 画面: 送信中 Busy／入力ロック
- サーバー: `/chat/send` 同時1件で 429
- 確認: 住所 OK／割り込み 429／リサーチ OK

### 2026-08-08夜〜09（失敗メッセージの日本語化）

- **狙い**: 英語の生エラーを画面に出さない
- **変更**: `main.py`（401/503/実行失敗）、`open_deep_research.py`（主要失敗を短い日本語）、`chat.html`（通信・HTTPの言い換え）
- **確認**: 誤パスワード日本語／住所成功パス維持
- **学び**: 詳細は `error` フィールドに短く残し、`answer`／画面には出さない

### 2026-08-08夜（Vault pull と読み取りの衝突）

- **調査**: pull = `fetch` + `reset --hard`。ロックなし。アプリはノートを毎回ディスク読み（Core以外）
- **判断**: 半端ツリーは理論上あり／実害は稀 → **経過観察**（大きな再設計はしない）
- **別件として指摘**: 当時 Core は起動時キャッシュのため、pull後も再起動まで古い可能性

### 2026-08-08夜（Core を毎回再読込）

- **変更**: `main.py` の起動時 `_core_knowledge` 固定を廃止。`_run_invoke` ごとに `load_core_knowledge`
- **確認**: `deploy_core_reload.sh` → CODE_OK／住所 OK
- **学び（資産）**: 確認スクリプトで `grep '_core_knowledge'` すると `load_core_knowledge` に誤ヒットして FAIL になる → チェックは単語境界で

### 2026-08-08夜（エージェント経路の個別確認）

- idea: `knowledge_retriever` → `idea_agent` PASS（researchなし）
- proposal: `knowledge_retriever` → `proposal_agent` PASS
- general: `knowledge_retriever` → `general_agent` PASS（「0900の役割を一言で」）
- スクリプト: `smoke_idea_agent.sh`／`smoke_proposal_agent.sh`／`smoke_general_agent.sh`

### 2026-08-08夜（.env.example 更新）

- 認証・LLM・Vault・リサーチのキー名と短い説明のみ（実値なし）
- `CHAT_PASSWORD`／`TAVILY_API_KEY`／`GEMINI_API_KEY` 等を整理

### 2026-08-08〜09（チャットUI：AIX 化）

**経緯（失敗も含めて資産）**
1. 当初プレビュー A/B（アイスシアン／アンバー）を `/ui-preview/*` に用意
2. **未デプロイだと 404** → 「現行しか見えない」。Macにファイルがあっても VPS 未反映では開けない
3. ユーザー反映後、A案は「枠を足しただけ」に近く不評 → **レイアウトから作り直し**（左右レール＋中央会話＋下部入力）
4. 枠が「くっきり直線」すぎ → 発光・ぼかし寄りに調整
5. 参考画像の格子（誤変換で「講師」と呼ばれた）とロゴ周りの揺らぎを現行 `/chat` に取り込み
6. 明るさの振り幅を何度か調整（強すぎ→控えめ→中間＋シアン影）
7. 入力／会話枠を細い枠＋角ブラケットに。Send は線画トーンでやや目立たせる
8. 表記: ロゴ **AIX**、副題仮置き `Artificial Intelligence eXperience`（正式展開は資料に無く仮。要確認可）
9. 入力まわり英語化（Password／Send／Clear／Lock 等）
10. スマホ横ずれ: `overflow-x: hidden`／`overscroll-behavior-x`／`touch-action: pan-y` 等
11. UI完成確認後、**プレビュー用ファイル・ルートを全削除**（`cleanup_chat_previews.sh`）→ `/chat` のみ
12. smoke で HTML に `jarvis` 検出 → 原因は画面ではなく旧 localStorage キー名 `jarvis_chat_password` → 削除して再確認 OK

**本番UIの要点**
- URL: `https://aix.sunnysh.net/chat`
- 暗背景・格子・ロゴ周りの弱い揺らぎ・シアン枠HUD
- Unlock／送信／履歴／リサーチ待ちは維持

### 2026-08-08夜（提案出力の品質）

- **問題**: 空の `*`／`-`、本文に「仮実装：1回執筆のみ…」、一般論に寄りがち
- **対応**: `app/graph/proposal/single_shot.py`
  - プロンプトから仮実装指示を削除／内部用語禁止
  - 対象・目的・具体アクション・根拠（ノート）を必須
  - 後処理で空箇条・仮実装行を除去
  - 顧客ノートを notes 先頭寄りに並べ替え
- **確認**: `deploy_proposal_quality.sh` → path_ok／no_internal／empty_bullets=0／PASS（ピント提案）

### 2026-08-09（smoke を完成状態に合わせる）

- `scripts/smoke_vps_core.sh` に集約: health／unlock／住所／会話継続／短い提案／短いリサーチ／AIX・No-Jarvis／vault git
- `smoke_ui_done.sh` は同スクリプトへ委譲
- 個別経路用: `smoke_*_agent.sh` は残置（任意）

### 2026-08-09（使い方メモ）

- プロジェクト直下 `使い方.md`（URL・聞き方・Vault5分・禁止事項・smoke一行）

### 2026-08-09（UI完成後スモーク → ALL_OK）

| 項目 | 結果 |
|------|------|
| /health | OK |
| Unlock | OK |
| Address PRIZM | OK |
| Proposal | OK |
| No Jarvis in /chat | OK（キー名除去後） |
| プレビュー整理後 | `/chat` 200、preview URL 404、unlock_send OK |

### 2026-08-09（Cursor Remote SSH・config作成）

- Macに `~/.ssh/config` を新規作成（Host `xserver-vps`）
- `ssh xserver-vps` で接続確認OK（`root`／`x162-43-4-234`）

### 2026-08-09（Cursor Remote SSH・初回セットアップ開始）

- **範囲：** Remote SSH のみ（Aider等は扱わない）
- **確定：** ユーザー `root`／鍵 `~/.ssh/xserver-vps.pem`／開くフォルダ推奨 `/opt/multiagent`
- **確認：** 手動SSHは成功（ホスト名 `x162-43-4-234`）
- **詳細：** 本ファイル「Cursor Remote SSH」節

### 2026-08-09（Cursor Remote SSH・接続完了）

- 開き方：Macターミナルで  
  `cursor --folder-uri "vscode-remote://ssh-remote+xserver-vps/opt/multiagent"`
- 画面確認：タイトル `multiagent [SSH: xserver-vps]`、左に `app`／`bin`／`vault` 等
- VPS確認：`hostname=x162-43-4-234`／`whoami=root`／`/opt/multiagent` 存在
- **Remote SSH 初回セットアップは完了**

### 2026-08-09（Aider 導入・VPS）

- **場所：** `/opt/multiagent` のみ（Macには入れない）
- **本体：** `aider 0.86.2`（`/root/.local/bin/aider`）
- **AI：** 既存 Gemini（Vaultのキーファイルから `/root/.aider.env` を生成。中身はログに出さない）
- **モデル：** `gemini/gemini-2.5-flash-lite`（費用抑えめ）
- **起動：** `/opt/multiagent/bin/aider-start.sh`（使うときだけ。常時稼働しない）
- **設定：** `/opt/multiagent/.aider.conf.yml`（秘密なし）／鍵は `/root/.aider.env`（権限 600）
- **Git：** `/opt/multiagent` を初回 init（`vault/` は除外。戻しやすくするため）
- **次：** 小さいタスクで1回だけ半自動ループを試す

---

## 運用で得た学び（失敗も資産）

1. **コードを Mac で直しても、VPS に scp／restart するまで本番は変わらない**（404や旧UIの主因）
2. **ブラウザは Cmd+Shift+R**（キャッシュで古い chat.html を見ることがある）
3. **`docker compose restart` は env_file を再読込しないことがある** → パスワード等は `--force-recreate`
4. **確認スクリプトの grep は誤ヒットに注意**（`_core_knowledge` ⊂ `load_core_knowledge`）
5. **画面に出ない文字列も HTML ソース検査に引っかかる**（旧 localStorage キー名）
6. **エージェントシェルが結果を返せないことがある** → 手元で `scripts/*.sh` を実行する運用が有効
7. **UIは「枠を足す」よりレイアウトから直す**／明るさはユーザーと往復で中間値を探す
8. **作業ログは区切りごとに必ず追記**（チャット切れても再開できる正本＝本ファイル）

---

## 再開時に読む／触る場所

| 用途 | 場所 |
|------|------|
| アプリコード | `Desktop/自分のマルチエージェント構築/` |
| 短い使い方 | 同 `使い方.md` |
| 仕様 | 同 `system_spec.md` |
| 総合確認 | 同 `scripts/smoke_vps_core.sh` |
| VPS設定 | `/opt/multiagent/docker-compose.yml`・`.env` |
| Cursor Remote SSH | 本ファイル「Cursor Remote SSH」節 |
| Aider（VPS） | 起動：`/opt/multiagent/bin/aider-start.sh`／設定：`.aider.conf.yml`／鍵：`/root/.aider.env` |
| 隠し場所の一覧 | [[Macよく使う隠し場所]]（`~/.ssh` など） |
| この記録 | 本ファイル |
| 説明の深さ | [[説明レベル表]]（VPS／GitはC） |

---

## 注意（秘密情報）

- API_KEY・Geminiキー・SSH秘密鍵・CHAT_PASSWORD の**中身は本ファイルに書かない**
- 鍵の置き場だけメモ：`~/.ssh/xserver-vps.pem`、VPSの `.env`、Vault内の `GEMINI_API_KEY.env`（Git対象外）

---

## 次にやること（バックログ）

**進め方の正本（リサーチ3票一致・要約）：**  
Remote SSH（場所を一つに）→ **短い半自動ループ（承認1回）** → 効いたら **Aider**（または Claude Code + tmux）→ 重い自律（OpenHands／Cron24h／Hermes常時）は後回し。  
目的は「自分の作業を減らしつつ、問題が増えないこと」。完全無人のVPS多層より、承認付きの短いループを先に。

1. ~~Cursor Remote SSH~~ **完了**（2026-08-09）… 最初の一手  
2. ~~Aider 導入~~ **完了**（2026-08-09）… VPS `/opt/multiagent`・Gemini flash-lite・`bin/aider-start.sh`  
3. **（次）Aider で短い半自動ループを1回試す** … 小さいタスク・人が承認・常時稼働しない  
4. （後）Claude Code + tmux … 自律精度は高いが費用・上限に注意  
5. （後回し）OpenHands／Cron型24h無人／Hermes・Agent AFK  
6. （任意）Webhookで即時反映  
7. （任意）自宅IP変更時のパケットフィルター更新手順  
8. （任意）分野キーワードの追加整備（質問の言い回しが増えたとき）  
9. （任意）AIX の英語展開が正式に決まったら副題を差し替え（いまは仮: Artificial Intelligence eXperience）  
10. （様子見）Vault pull 中の半端読みが実害になったら flock 等の最小対策  
11. （任意）proposal の執筆＋レビュー構成（いまは single_shot）
