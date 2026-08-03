# 作業記録：Railwayルール作り自動化＋Failure Pattern確認

**日付**: 2026-07-22  
**場所**: `AI思考OS_ルール作り_構築記録/記録/`  
**関連仕様書**: `仕様書_LangGraph×Hermes×OpenClaw_ルール作り自動化_v0.1.md`（v0.3.1）  
**関連実装**: `02_活動基盤/実務/rule-builder/`  
**Railway**: https://rule-builder-production.up.railway.app  

---

## 1. この記録の目的

- 今回の準備〜初回テスト〜Failure Pattern確認を、あとから振り返れるように残す
- 将来、ナレッジ／商品化の素材にも使える「何が起きたか」の正本とする
- Memory Policy の中身評価はまだしない（FP発見が今回の成果）

---

## 2. 何を作ろうとしていたか

LangGraph × Hermes × OpenClaw で、AI組織のルールをゆっくり作る仕組み。

- 人間最終承認（Human-in-the-Loop）
- Railway の無料お試し枠で短時間テスト
- Hermes は Grok **OAuth（月額サブスク）**（APIキー不要）
- Gemini 無料APIは下書き／内部チェック／外部レビュー用（上限時は Hermes へフォールバック）
- Pure OS Town は確定内容として安易に変更しない（参照・適合チェックのみ）
- SSoT順：人生戦略OS → Town憲法 → 成果物 → Railway下書き

---

## 3. 準備でやったこと（時系列要約）

1. Railway アカウント登録（GitHub）
2. 仕様書作成・追記（v0.1 → v0.3.1）
3. `rule-builder/` 設置ファイル作成・デプロイ
4. Gemini キー設定（既存 `GEMINI_API_KEY.env` から）
5. Hermes インストール修正・Grok OAuth ログイン
6. Volume（`/root/.hermes`）追加でログイン永続化
7. 1項目目 `memory-policy` を実行 → `awaiting_human` まで到達

---

## 4. 初回テストの結果（要点）

| 項目 | 結果 |
|------|------|
| 流れ | 動いた（下書き→内部チェック→外部レビュー→人間待ち） |
| 人間待ち停止 | 成功（`awaiting_human`） |
| 成果物の質 | 失敗（ルール文書ではなく AI の迷子ログ） |
| 価値 | Failure Pattern を実測できた |

**認識の合意**（2026-07-22）  
Memory Policy v2 の中身レビュー段階ではない。  
「今回のテストで何が分かったか」を整理する段階。  
v2 は失敗ではなく、AI組織の Failure Pattern 発見の成果物。

---

## 5. Failure Pattern 確認結果（改善案はまだ書かない）

各FPについて「何が起きたか／LangGraphで解けるか／結論」まで確認済み。  
改善方法は全FP確認後に検討する。

### FP-01：参照迷子

- **何が起きたか**: 人生戦略OS等のパスを探すが Railway `/app` に無く、「見つからない」ループ
- **LangGraphで解けるか**: 症状の停止は可能。参照の渡し方（データ注入）は別途必要
- **結論**: **一部のみ**

### FP-02：思考ログ混入

- **何が起きたか**: Hermes 出力の Reasoning／独り言が draft に入り、ルール文書にならなかった
- **LangGraphで解けるか**: 受け取り後の判定・進行停止は可能。Hermesの吐き方自体は別
- **結論**: **一部のみ**

### FP-03：汚染の伝播

- **何が起きたか**: 汚い v0 が収束・内部チェック・外部レビュー・v2 まで連鎖した
- **LangGraphで解けるか**: 工程間の進行制御そのもの
- **結論**: **Yes**

### FP-04：形式チェック不足

- **何が起きたか**: 内部チェック2回でも「ポリシー文書か」を十分見ず、汚いまま通過した
- **LangGraphで解けるか**: PASS条件・判定設計は LangGraph 側の問題
- **結論**: **Yes**

### FP-05：人間レビュー不能

- **何が起きたか**: 人間に渡った成果物が「読むべきルール」ではなく迷子ログで、中身採点できなかった
- **LangGraphで解けるか**: 人間ゲート前に「レビュー可能な形か」を必須にすれば、人間に汚物を渡さない制御は可能。レビューしやすさの最終形は人間側の運用設計も含む
- **結論**: **一部のみ**

### 一覧

| ID | パターン | LangGraphで解けるか |
|----|----------|---------------------|
| FP-01 | 参照迷子 | 一部のみ |
| FP-02 | 思考ログ混入 | 一部のみ |
| FP-03 | 汚染の伝播 | Yes |
| FP-04 | 形式チェック不足 | Yes |
| FP-05 | 人間レビュー不能 | 一部のみ |

---

## 6. インフラ・運用メモ（後で役立つこと）

- Railway URL: `https://rule-builder-production.up.railway.app`
- Health: `GET /health`
- 実行: `POST /run/{item_id}`
- 承認: `POST /approve/{item_id}`
- Hermes: `hermes auth add xai-oauth --no-browser`（Console で実行）
- Volume: Mount Path `/root/.hermes`（OAuth トークン保持）
- Gemini 無料枠は上限に達しうる → Hermes フォールバックあり
- Railway 運用中は PC の Hermes を止める方針

---

## 7. まだ決めていないこと（この記録時点）

- この整理の保存後の改善着手順
- Memory Policy の中身レビュー（まだしない）
- 再実行のタイミング
- Failure Library 正式版への昇格

---

## 8. 次の一手（記録時点の提案・未着手）

1. FP-05 まで確認完了 → 全体の結論を人間と合意
2. その後に改善案をまとめる
3. 改善後に memory-policy 再実行 → きれいな文書が出てから中身レビュー

---

**作成**: Cursor（2026-07-22）  
**ステータス**: FP-01〜05 確認完了。改善案は未着手。
