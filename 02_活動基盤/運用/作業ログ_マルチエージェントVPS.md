# 作業ログ：マルチエージェント × VPS

## このファイルの目的

LangGraph系マルチエージェントアプリと、Xserver VPSへの設置・公開・Vault連携の**経緯・現状・次の手**を残す。

チャットが切れても、このファイルで再開できる。

**更新ルール：** 区切りのよい作業が終わったら、このファイルの「現状サマリー」と「年表」を追記する（ユーザーのOKなしに新規ログファイルは増やさない。本ファイルを正本にする）。

---

## 現状サマリー（2026-08-07）

| 項目 | 内容 |
|------|------|
| **アプリ置き場（Mac）** | `/Users/miyawakidaisuke/Desktop/自分のマルチエージェント構築/` |
| **Vault（Mac／正本）** | `/Volumes/MultiPurpose_SSD/DigitalGarden`（旧名 AI関連） |
| **VPS** | Xserver VPS / Ubuntu 24.04 / IP `162.43.4.234` |
| **VPSアプリ** | `/opt/multiagent`（Docker Compose・コンテナ名 multiagent） |
| **VPS Vault** | `/opt/multiagent/vault`（**Git化済み**。GitHub `obsidian-vault` を5分ごと pull） |
| **同期スクリプト** | `/opt/multiagent/bin/vault-pull.sh`（cron `*/5`） |
| **Deploy key** | VPS `/root/.ssh/obsidian-vault-deploy`（GitHubは読取専用） |
| **API** | `/health`・`/invoke` 稼働確認済み |
| **チャットUI** | `http://162.43.4.234:8000/chat`（Jarvis風。**API_KEY欄なし** → `/chat/send`。`/invoke` はキー必須のまま） |
| **外公開** | `https://aix.sunnysh.net`（Caddy・Let's Encrypt）。旧 `:8000` も可。TCP 80/443 は全て許可 |
| **SSH** | 鍵：`~/.ssh/xserver-vps.pem` |
| **Vault同期テスト** | `04_Inbox/VPS同期テスト_2026-08-07.md` が VPS に反映確認（`7a55d394`） |
| **まだやっていない** | ドメイン／HTTPS／Webhook |

---

## いまの更新の流れ（実態）

```text
[Mac] DigitalGarden
  ├─ Obsidian Git → GitHub（非公開：obsidian-vault）※Geminiキー等はGit対象外
  └─ （過去）rsync 1回 → VPS /opt/multiagent/vault

[VPS] /opt/multiagent
  ├─ Docker でアプリ起動（Vaultを /app/vault:ro でマウント）
  └─ vault は Git未接続のため、GitHub更新は自動では入らない
```

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
- 最小UI → Jarvis風デザイン（暗背景・青系）
- `/invoke` 接続は維持。ブラウザで送受信確認済み

### 2026-08-07（KnowledgeRetriever：顧客ノートを拾えない不具合）

- **原因1**: 固定 ENTRY_CANDIDATES のみ参照（検索なし）
- **原因2**: Supervisorが knowledge を飛ばすことがあった → 未取得時は必ず knowledge 先行
- **原因3**: 検索が顧客会社概要を安定して返せないことがあった → 既知顧客の会社概要を優先ヒット
- **確認**: 「PRIZMの住所は？」で `〒498-0006 愛知県弥富市佐古木3丁目373-5` が返ることを確認

---

## 再開時に読む／触る場所

| 用途 | 場所 |
|------|------|
| アプリコード | `Desktop/自分のマルチエージェント構築/` |
| 仕様 | 同フォルダの `system_spec.md` |
| VPS設定 | `/opt/multiagent/docker-compose.yml`・`.env` |
| この記録 | 本ファイル |
| 説明の深さ | [[説明レベル表]]（VPS／GitはC） |

---

## 注意（秘密情報）

- API_KEY・Geminiキー・SSH秘密鍵の**中身は本ファイルに書かない**
- 鍵の置き場だけメモ：`~/.ssh/xserver-vps.pem`、VPSの `.env`、Vault内の `GEMINI_API_KEY.env`（Git対象外）

---

## 次にやること（バックログ）

1. （任意）Webhookで即時反映  
2. （任意）ドメイン／HTTPS  
3. （任意）自宅IP変更時のパケットフィルター更新手順  
4. Core変更後にアプリへ即反映したい場合は、コンテナ再起動の要否を確認
