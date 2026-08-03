# 仕様書：LangGraph × Hermes × OpenClaw ルール作り自動化 v0.3.1

**作成日**: 2026-07-22  
**最終更新**: 2026-07-22  
**ステータス**: Draft（人間承認待ち）  
**対象読者**: 宮脇氏、Cursor、Hermes、将来の実装担当AI

---

## 0. この仕様書の目的

AI組織の「ルール（憲法・判断原則・運用ルール）」を、**3日程度かけてゆっくり**作り上げる仕組みの設計図である。

- 急がない（24時間フル稼働は不要）
- 人間が最終OKする（Human-in-the-Loop）
- 項目ごとに外部AIレビューも入れる
- Railwayの無料お試し枠で「動くか」を短時間テストする

**この仕様書は「構築記録」ではなく「これから作るものの設計図」** である。  
既存の構築記録・成果物は `AI思考OS_ルール作り_構築記録/` を参照する。

### 0.1 最重要前提：Pure OS Town は確定内容（安易に変更しない）

| 区分 | 内容 |
|------|------|
| **Pure OS Town** | 確定済みの憲法・組織・監視の仕組み。**しっかりした理由がない限り変更しない** |
| **本システム** | AI思考OS の「未整備ルール」を作るための**作業ライン**（Railway上の一時的な実行環境） |
| **関係** | 本システムは Pure OS Town を**参照・適合チェック**する。Townの役割を置き換えない |

**方針（エコシステム保護）**
- Pure_OS_Town/ 配下を**本システムから自動更新しない**
- Townの内容を変える必要がある場合は、**理由を明記したうえで人間が判断**する（安易な書き換えはしない）
- Townの Schema（4桁番号・Bead・WorkPersona 等）を本システム側で再定義しない
- 「LangGraph＝Mayor」「Hermes＝Patrol」など、**役割の混同・上書きをしない**

**許可**
- 新ルール下書きを `AI思考OS_ルール作り_構築記録/成果物/` に追加（人間OK後）
- Pure OS Town との矛盾がないかを**読み取り専用で検証**する
- 矛盾がある場合は**人間へエスカレーション**（自動修正しない）

---

## 1. 背景（いまどこまでできているか）

### 1.1 すでにある成果物

| 資料 | 場所 | 状態 |
|------|------|------|
| User Model v0.1 | `成果物/User Model v0.1.md` | **正式採用済み** |
| AI思考OS v0.1 | `成果物/AI思考OS_v0.1.md` | **運用開始可能** |
| 構築記録・設計判断 | `記録/` 配下 | 参照用 |
| Grok外部記憶運用ノート | `記録/20260719_Grok外部記憶運用ノート v0.1.md` | 運用知見 |
| AI Governance 目次 | `SecondBrain/03_AI_Systems/Governance/00_Index.md` | Hermes運用前提あり |
| Pure OS Town 管理台帳002 | `Pure_OS_Town/governance/9999_管理台帳_002.md` | **完成済み・参照のみ** |
| Pure OS Town 憲法 | `PURE_OS.md` | **完成済み・参照のみ** |
| Pure OS Town Wiki | `Pure_OS_Town/wiki/` 配下 | **完成済み・参照のみ** |
| 第二の脳構築日記 | `第二の脳構築日記/` | 設計判断の背景・教訓 |

### 1.1.1 正本（SSoT）の優先順位（ねじれ防止）

複数の「正本」が存在するが、**領域ごとに分離**する。上書きしない。

**人生戦略OSの場所**：`01_人生戦略OS/` 配下（中心ファイルは `0000_人生戦略OS.md`）。  
※ `0000_人生戦略OS/` というフォルダではなく、**ファイル**である。

| 優先 | 正本 | 場所 | 本システムとの関係 |
|------|------|------|-------------------|
| **1** | **人生戦略OS** | `01_人生戦略OS/`（0000が中心） | **一次情報源**。本システムから直接書き込まない |
| **2** | **Town憲法** | `PURE_OS.md` + `Pure_OS_Town/` | 確定内容。安易に変更しない。適合チェック用 |
| **3** | **成果物** | `AI思考OS_ルール作り_構築記録/成果物/` | 本システムの出力先（人間OK後） |
| **4** | **Railway下書き** | `data/drafts/` | 一時作業場。正本ではない |

**User Model の位置づけ**（構築記録より）：  
人生戦略OSの**参照用要約**。User Model単体が正本ではない。

**適合チェックの順序**（新ルール保存前に必ず実行）：
1. 人生戦略OS・User Model v0.1・AI思考OS v0.1 と矛盾しないか
2. Pure OS Town（穏やかさ・Eco・HallucinationPrevention）と矛盾しないか
3. 上記に問題があれば保存せず、人間へエスカレーション

### 1.2 まだこれから作るもの（優先度付き）

**優先度A**（3日ルール作りの主対象）
- 人生戦略OS本体の整備（`01_人生戦略OS/`）
- User Model の正本保存（人生戦略OS配下へ）
- AI思考OS の正本保存
- Memory Policy v0.1

**優先度B**
- MOC（索引ファイル）作成
- Failure Library 初版
- Decision Log 初版

**優先度C**（実運用後に再評価）
- KnowledgeOS統合
- Hermes同期設計
- 自動化の本格検討

**Memory Policy v0.1（Tier構造・確定案）**

| Tier | 扱い | 中身 |
|------|------|------|
| Tier1 | 常時参照 | AI思考OS、User Model、Core Values、Long-term Goals、重要ルール |
| Tier2 | 要約保存 | Failure Library、Decision Log、レビュー結果 |
| Tier3 | 長期保管 | 会話ログ、リサーチ、実験記録、日誌 |

**まだ未確定（実運用後に再評価）**
- Failure Library の最終構造
- Decision Log の最終構造
- MOC の最終構造
- Grok外部記憶の運用限界
- Hermes自動同期方法

### 1.3 解決したい問題

構築記録（20260719）で整理済みの構造問題：

- 理解不足のまま提案する
- わかったふり
- 同じ確認のループ
- 車輪の再発明（決まったことを忘れる）
- 概念の重複（User Modelが肥大化する）

**本仕様の狙い**：上記を「人間＋AI組織の型」で防ぎ、ルールを資産として残す。

### 1.4 設計思想（第二の脳構築日記より）

`第二の脳構築日記/ハルシネーション問題.md` の核心：

> AIを設計者にすると、設計は終わらない。  
> 必要なのは「AIを信頼できる状態まで育てる監査の仕組み」である。

本システムはこの思想に従い、**監査と設計を分離**する（詳細は §3.4）。

---

## 2. ゴール（成功の定義）

### 2.1 短期ゴール（Phase 1：Railwayテスト）

- LangGraphで「1ルール項目」の流れが動く
  - 下書き → 外部レビュー → 人間確認 → 保存
- Hermesが記憶・収束（設計を増やしすぎない）を担う
- OpenClawが調べもの・下書き作成を担う（**正式保存はしない**）
- Railway上で短時間起動テストが成功する

### 2.2 中期ゴール（Phase 2：3日ルール作り）

- ルール項目リスト（10〜30項目想定）を3日で順番に処理
- 各項目が「下書き → レビュー → 人間OK → 正本保存」のサイクルを完了
- 最終成果物が `AI思考OS_ルール作り_構築記録/成果物/` に残る（Pure_OS_Town/ には書かない）

### 2.3 非ゴール（今回やらないこと）

- 24時間フル常駐運用
- OpenClawによる本番フォルダへの直接書き込み
- ルールの完全自動採用（人間承認なし）
- チャットUIの本格開発（Phase 1ではCLI/APIで十分）

---

## 3. 全体構成（役割分担）

### 3.0 2つの世界の関係（混同禁止）

**Pure OS Town（完成済み）** と **本システム（これから作る作業ライン）** は別物。

```
【確定済み・安易に変更しない】Pure OS Town
  PURE_OS.md（憲法）
  Mayor（統括・Bead分解）  Patrol（監視・drift拒否）
  Hermes（Town内司令塔）  OpenClaw（Town内実行部隊）
  9999_管理台帳_002 / wiki / beads

【これから作る】ルール作り作業ライン（Railway）
  LangGraph（作業進行）  Hermes（収束・記憶）  OpenClaw（調査・下書き）
  → 出力先：AI思考OS_ルール作り_構築記録/成果物/ のみ
  → Town適合チェック：読み取り専用
```

| Pure OS Town の役割 | 本システムでの対応 | 関係 |
|--------------------|-------------------|------|
| Mayor（統括・分解） | LangGraph（項目進行） | **似ているが別物**。TownのMayorを置き換えない |
| Patrol（監視・drift拒否） | 適合チェックノード | **Patrolの代わりではない**。Townルールを読んで照合するだけ |
| Hermes（Town司令塔） | Hermes（収束・記憶） | **同じHermesだが文脈が違う**。Town運用と混ぜない |
| OpenClaw（Town実行部隊） | OpenClaw（下書き作成） | **権限を絞った限定版**。TownのWorkPersonaはそのまま |
| Human Overseer | あなた | 両方で最終承認 |

### 3.1 本システムの構成図

```
Human Overseer（あなた）
    │  最終承認・方針修正（Decision OS）
    ▼
LangGraph（作業進行・状態管理）
    │  ※ TownのMayorではない。ルール作り専用の進行役
    │  項目ごとのループ管理・承認待ちで停止
    ├──► Hermes Agent（収束・記憶・整合）
    │       ・提案を増やさず統合・整理
    │       ・Pure OS Town / AI思考OS との矛盾検出
    ├──► OpenClaw（調査・下書き）
    │       ・drafts/ のみ出力（Eco原則：API 3回/項目上限）
    └──► 適合チェック（読み取り専用）
            ・Pure OS Town 原則との照合
            ・Patrolの代行ではない。矛盾時は人間へ
```

### 3.2 LangGraph の役割

| 担当 | 内容 |
|------|------|
| 進行管理 | 3日間の項目リストを順番に処理 |
| 状態管理 | 各項目の状態（未着手/下書き/レビュー中/承認待ち/完了） |
| 承認ゲート | 人間OKが出るまで次へ進まない |
| 外部連携 | 外部AIレビューAPI呼び出しのタイミング制御 |

### 3.3 Hermes Agent の役割

Governance（`00_Index.md`）および Pure OS Town の Hermes 前提に従う：

- **「提案を増やすAI」ではなく「設計を収束させるAI」**
- User Model v0.1・AI思考OS v0.1・人生戦略OSとの矛盾を検出
- **Pure OS Town（PURE_OS.md、wiki/Principles/）との矛盾も検出**
- 複数案があるときは新規追加より統合・簡素化を優先
- セッションをまたいだ記憶（Tier1情報の参照）

**注意**：Town内のHermes（司令塔+Patrol兼務）の運用ルールを本システム側で上書きしない。

### 3.4 OpenClaw の役割

OpenClaw遊撃軍プロトコルおよび `Executor_OpenClaw.md` の思想に従うが、**Railwayテストでは権限を絞る**：

| やる | やらない |
|------|----------|
| Webリサーチ | 本番ルールファイルの直接更新 |
| 下書きMarkdown生成 | Pure_OS_Town/ への書き込み |
| 既存資料の読み取り（許可範囲内） | 無限ループ・大量API消費 |
| | Town WorkPersona の再定義 |

**Eco原則**（Town準拠）：1項目あたり tool/API call **3回上限**。超えたら自己停止→人間へ。

### 3.5 監査と設計の分離（Governance Constitution 準拠）

`raw_legacy/Grok_Cursor_Era/00_AI_Governance_Constitution.md` の第2条・第4条に従う。

| レイヤー | 担当 | やること | やらないこと |
|----------|------|----------|--------------|
| **設計（下書き）** | OpenClaw + Hermes | 調査・下書き・統合・収束 | 最終決定・正式保存 |
| **監査（レビュー）** | 外部AI（Grok等） | 見落とし・反証・「本当に必要か」確認 | **採用・却下の判定** |
| **意思決定** | あなた（Human Overseer） | OK / 修正 / 却下 | — |

外部AIレビューは **Review Process**（採決しない）。  
最終の採用・保留・却下は **Decision OS**（= あなたの判断）のみ。

---

## 4. ルール作りの1項目フロー（核心）

1項目 = 例「Memory Policy の保存先ルール」など。

```
[開始]
  │
  ▼
① 既存資料読み込み（PreWorkReading 相当）
   - 人生戦略OS（01_人生戦略OS/）
   - Pure OS Town：PURE_OS.md、該当wiki（読み取り専用）
   - User Model v0.1 / AI思考OS v0.1
   - 該当する構築記録・第二の脳構築日記
   - ファイル場所を確認してから読む（場所間違い防止）
  │
  ▼
② OpenClaw：調査・下書き v0
   - LLM：Gemini無料API（ローテーション）
   - 出力先：drafts/{項目ID}_v0.md のみ
   - API上限：3回/項目
  │
  ▼
③ Hermes：収束・矛盾チェック → 下書き v1
   - LLM：Grok（Hermes・**xAI Grok OAuth**／APIキー不要）
   - 重複概念の統合
   - 人生戦略OS / AI思考OS / User Model との整合
   - Pure OS Town 原則（穏やかさ・HallucinationPrevention）との整合
  │
  ▼
④ LangGraph 内部チェック（最大2回・ここで精度を上げる）
   - LLM：Gemini無料API（軽量・低コスト）
   - チェック項目：§4.2 参照
   - FAIL → ③へ戻る（内部ループ、外部レビューはまだ呼ばない）
   - PASS → 次へ
  │
  ▼
⑤ 外部AIレビュー（1項目1回のみ）
   - LLM：Gemini無料API（基本）／効果が大きい場合は事前相談
   - 見落とし・反証・「本当に今必要か」
   - 採決はしない（Review Process）
  │
  ▼
⑥ Hermes：レビュー反映 → 下書き v2
  │
  ▼
⑦ 【停止】人間確認ゲート（Decision OS・1回＋修正最大1回）
   - あなたが OK / 修正指示 / 却下
   - 修正指示 → ③へ（最大1回。原則外部レビュー再実行しない）
   - 大幅変更（30%超）の場合のみ ⑤ を再実行（要相談）
  │
  ▼
⑧ 正式保存（人間OK後のみ）
   - 保存先：AI思考OS_ルール作り_構築記録/成果物/ のみ
   - Pure_OS_Town/ には書き込まない
   - 進行ログに1行追記（§5.2）
  │
  ▼
[次の項目へ] ※同時進行しない。1項目完走してから次へ
```

### 4.2 LangGraph 内部チェック（レビュー回数の設計）

**方針**：外部レビューと人間レビューの前に、LangGraph内で精度を上げる。  
**目的**：外部・人間のやり直しを減らす（ハルシネーション問題.md の教訓）。

| 段階 | 担当 | 回数上限 | LLM |
|------|------|----------|-----|
| 内部チェック | LangGraph | **2回/項目** | Gemini無料API |
| 外部レビュー | 外部AI | **1回/項目** | Gemini無料API（基本） |
| 人間確認 | あなた | **1回＋修正1回** | — |

**内部チェック項目**（④で自動判定）：
1. 人生戦略OS（01_人生戦略OS/）との矛盾
2. User Model v0.1 / AI思考OS v0.1 との矛盾
3. Pure OS Town 原則（穏やかさ・Eco・HallucinationPrevention）との矛盾
4. 既存ルールとの重複
5. 1行で目的が説明できるか（粒度チェック）

**PASS条件**：上記5項目すべてクリア、または軽微な指摘のみ（自動修正可能）。

### 4.1 人間確認ゲートで見る項目（Decision OS）

各項目、あなたは以下を確認する：

1. **目的**：このルールは何のためか（1行で理解できるか）
2. **SSoT整合**：人生戦略OS・AI思考OS v0.1 と矛盾していないか
3. **Town適合**：Pure OS Town（穏やかさ・Eco・HallucinationPrevention）と矛盾していないか
4. **重複**：既存ルールと被っていないか
5. **運用**：実際に使える粒度か（大きすぎ/小さすぎないか）
6. **穏やかさ**：このルールは摩擦・焦り・再作業を増やさないか（CalmnessAsTopPriority）

---

## 5. 進め方（9項目・1項目ずつ完走）

**方針**：速度用の優先度A/B/Cは使わない。9項目すべて対象。  
**進行**：1項目を下書き→内部チェック→外部レビュー→人間OK→保存まで**完走**してから次へ（同時進行しない）。

急がない前提。流れ作業にしない（第二の脳構築日記 Phase 6 より）。

| 順 | 項目ID | テーマ |
|----|--------|--------|
| 1 | memory-policy | 記憶の保存ルール（Tier構造含む） |
| 2 | grok-sync-rule | Grok同期ルール |
| 3 | failure-library | 失敗パターン集 |
| 4 | decision-log | 意思決定の記録 |
| 5 | review-process-draft | レビュー工程 |
| 6 | governance-index | Governance索引 |
| 7 | change-log-rule | 変更履歴の型 |
| 8 | rule-builder-moc | ルール一覧MOC |

**統合**：`tier-structure` は `memory-policy` に含める（8項目に整理）。

**起動の仕方（Phase 1）**  
- 手動トリガー：CLIコマンド1回 or Railway手動デプロイ
- 項目が承認待ちで止まる → あなたが都合のよい時間にOK
- 1日1回、進行ログ（§5.2）を Markdown で出力

### 5.1 項目リスト詳細（items.json 確定案・8項目）

| id | title | 参照ファイル | 備考 |
|----|-------|-------------|------|
| memory-policy | Memory Policy v0.1 | Grok外部記憶運用ノート、構築記録 | **Tier1/2/3を含む** |
| grok-sync-rule | Grok同期ルール | Grok外部記憶運用ノート | attachments/artifacts |
| failure-library | Failure Library v0.1 | 構築記録、ハルシネーション問題 | 失敗パターン集 |
| decision-log | Decision Log 運用ルール | Governance Constitution | 採用理由の記録 |
| review-process-draft | Review Process 下書き | Governance Constitution | Town既存と重複しない範囲 |
| governance-index | AI Governance 索引 | 00_Index.md | MOC的索引 |
| change-log-rule | Change Log 運用ルール | Governance Change Log | 変更履歴の型 |
| rule-builder-moc | ルール作りMOC | 本仕様書 | 完成ルールへの索引 |

**Town保護ルール**：上記の保存先はすべて `AI思考OS_ルール作り_構築記録/成果物/`。Pure_OS_Town/ への書き込みは禁止。

### 5.2 進行ログの型（Phase 4 エコシステム運用ルールより）

毎日1回、`記録/progress_YYYYMMDD.md` に以下を記録：

```markdown
# 進行ログ YYYY-MM-DD

## 全体像
（今日何を進めたか、1〜3行）

## 完了項目
- [項目ID] タイトル → 成果物パス

## 承認待ち
- [項目ID] タイトル → drafts/ のパス

## 判断理由
（なぜ採用/却下/保留したか）

## Town適合チェック
- 矛盾なし / エスカレーション内容

## 次の一手
（明日やる項目ID）
```

### 5.3 MOC（索引ファイル）

3日完了後、`成果物/00_MOC_ルール一覧.md` を作成する。

- 完成したルールへのリンク一覧
- Pure OS Town との関係（参照のみ・変更なし）を明記
- AIが次回作業時に「どこに何があるか」を把握する入口

（第二の脳構築日記 Phase 5：索引がないとAIは迷子になる、の教訓を反映）

---

## 6. データ設計

### 6.1 フォルダ構成（Railwayデプロイ用）

```
rule-builder/
├── main.py                 # エントリポイント（FastAPI or LangGraph runner）
├── graph/
│   ├── workflow.py         # LangGraph定義
│   ├── nodes/              # 各ステップの処理
│   └── state.py            # 状態の型定義
├── agents/
│   ├── hermes_client.py    # Hermes呼び出し
│   └── openclaw_client.py  # OpenClaw呼び出し
├── reviewers/
│   ├── internal_check.py   # LangGraph内部チェック（Gemini）
│   └── external_review.py  # 外部AIレビュー（Gemini基本）
├── data/
│   ├── items.json          # 処理する項目リスト
│   ├── drafts/             # 下書きのみ（OpenClaw/Hermes出力）
│   └── approved/           # 人間OK後の正式版
├── requirements.txt
├── Dockerfile
├── railway.toml            # Railway設定（任意）
└── .env.example            # 環境変数テンプレート
```

### 6.1.1 ローカル正本との関係

| 場所 | 役割 |
|------|------|
| `AI思考OS_ルール作り_構築記録/` | **人間が読む正本・履歴** |
| Railway `data/` | **実行中の作業場（下書き・状態）** |
| 人間OK後 | ローカル正本へ手動 or スクリプトで反映 |

**原則**：Railway上の `approved/` は作業コピー。最終正本はローカルの構築記録フォルダ。

### 6.2 項目リスト（items.json）の例

```json
{
  "project": "AI思考OS ルール作り Phase2",
  "items": [
    {
      "id": "memory-policy",
      "title": "Memory Policy v0.1",
      "priority": 1,
      "references": [
        "記録/20260719_Grok外部記憶運用ノート v0.1.md",
        "成果物/User Model v0.1.md"
      ],
      "existing_draft": null,
      "status": "pending"
    }
  ]
}
```

### 6.3 状態（LangGraph State）

```python
# 概念のみ（実装時に具体化）
class RuleItemState(TypedDict):
    item_id: str
    status: str  # pending | drafting | internal_check | external_review | awaiting_human | approved | rejected
    draft_v0: str | None
    draft_v1: str | None
    draft_v2: str | None
    internal_check_result: str | None
    internal_check_count: int  # 最大2
    external_review: str | None
    external_review_done: bool  # 1項目1回
    human_decision: str | None  # approve | revise | reject
    human_notes: str | None
    revision_count: int
```

---

## 7. Railway 設置方針

### 7.1 コスト方針（確定）

**基本方針**：費用を抑える。API選びは実装側に任せる。  
**例外**：費用以上の効果が見込める場合は、**事前に相談**してから有料APIを追加する。

| 項目 | 方針 |
|------|------|
| Railway | 無料お試し（$5/約30日）でPhase 1テスト |
| 常駐 | 24時間常駐しない。手動起動 or 短時間実行 |
| VPS | 本格常駐が必要になったら移行を検討（その時Hermes配置も再検討） |
| 有料API追加 | 効果が十分大きい場合のみ、事前相談 |

### 7.2 LLM・API の使い分け（確定）

| 用途 | 実行場所 | 接続方式 | 備考 |
|------|----------|----------|------|
| **Hermes（司令塔・収束）** | Railway | **xAI Grok OAuth** | 月額サブスク連携。**APIキー不要** |
| **OpenClaw（下書き）** | Railway | **Gemini無料API** | 5キーローテーション（必要時にユーザー提供） |
| **LangGraph内部チェック** | Railway | **Gemini無料API** | 最大2回/項目・低コスト |
| **外部レビュー** | Railway | **Gemini無料API** | 1回/項目 |
| **Cursor（設置・調整）** | 手元PC | — | 開発支援 |

#### Hermes × Grok の接続（APIキーではない）

正式名称：**xAI Grok OAuth**（SuperGrok / X Premium+ 月額プラン）

- Hermes インストール後、**Grok へのログイン作業**が必要（1回）
- コマンド例：`hermes auth add xai-oauth`
- ブラウザで accounts.x.ai にログイン → 承認 → トークン保存
- Railway 等リモート環境：`--no-browser` でURLとコードを表示し、手元ブラウザで承認
- **XAI_API_KEY / Grok API キーは不要**（月額利用枠内で使用）
- トークン保存先：`~/.hermes/auth.json`（Railwayでは永続ボリューム等で保持）

**Hermes の二重運用禁止**  
Railway で Hermes を動かす期間は、**手元PCの Hermes Agent は停止**する。  
VPS移行時に、Railway vs VPS vs PC の配置を再検討する。

**ユーザーが用意するもの**
- **Grok 月額サブスク**（SuperGrok または X Premium+）→ Hermes OAuth 用
- **Gemini無料APIキー**（1〜5個）→ 必要になった時点で案内する

### 7.3 Railway で動かす最小構成

| コンポーネント | Phase 1 | 備考 |
|----------------|---------|------|
| Python + LangGraph | ✅ | メイン |
| Hermes Agent | ✅ | Railway上・Grok OAuth（月額サブスク） |
| OpenClaw | △ 限定版 | リサーチ・下書きのみ |
| データベース | ❌ | JSONファイルで十分 |
| ブラウザ常駐 | ❌ | OpenClawの重い機能は使わない |

### 7.4 必要な環境変数（.env.example）

```env
# Hermes（Railway上・Grok OAuth。APIキー不要）
# 初回セットアップ時：hermes auth add xai-oauth [--no-browser]
HERMES_LLM=xai-oauth

# Gemini無料API（内部チェック・OpenClaw・外部レビュー共通）
# 必要時にユーザーが提供
GEMINI_API_KEYS=

# 外部レビュー（基本はGemini。Grokは事前相談時のみ）
EXTERNAL_REVIEW_PROVIDER=gemini

# Railway / Hermes接続
HERMES_API_URL=          # Railway内なら localhost or 内部URL

# 安全・回数制限
DRAFT_ONLY=true
MAX_INTERNAL_CHECKS=2    # LangGraph内部チェック上限
MAX_EXTERNAL_REVIEWS=1   # 外部レビュー上限（1項目1回）
MAX_HUMAN_REVISIONS=1    # 人間修正指示上限
HUMAN_APPROVAL_REQUIRED=true
```

---

## 8. 安全ルール（必須）

### 8.1 書き込み権限

| エージェント | drafts/ | approved/ | ローカル正本 |
|--------------|---------|-----------|--------------|
| OpenClaw | ✅ 可 | ❌ 不可 | ❌ 不可 |
| Hermes | ✅ 可 | ❌ 不可 | ❌ 不可 |
| LangGraph（自動） | ✅ 可 | ⚠️ 人間OK後のみ | ❌ 不可 |
| Human | ✅ 可 | ✅ 可 | ✅ 可 |

### 8.2 禁止事項

- 4桁番号の勝手な変更
- ユーザーのOKなしの新規フォルダ・ファイル作成（本番領域）
- **Pure_OS_Town/ 配下への書き込み・上書き**
- **PURE_OS.md・9999_管理台帳_002 の変更**
- ルールの自動採用（人間承認バイパス）
- OpenClawによる無制限APIループ（3回/項目超過）
- Patrol/Mayor の役割を本システム側で再定義・置き換え

### 8.3 エスカレーション

以下は即人間へ（Pure OS Town の Human Direct Escalation 思想に準拠）：

- Pure OS Town 原則との矛盾を解消できない
- AI思考OS / User Model / 人生戦略OS との矛盾を解消できない
- 同一項目で修正が3回を超える
- 外部レビューとHermesの結論が真逆
- OpenClaw API上限（3回/項目）到達

---

## 9. 実装フェーズ

### Phase 0：仕様確認（今ここ）

- [ ] 本仕様書を人間がレビュー
- [ ] 項目リスト（items.json）の中身を確定
- [ ] Railwayアカウント（登録済み）確認

### Phase 1：最小動作（1〜2日）

- [ ] `rule-builder/` フォルダと最小ファイル作成
- [ ] LangGraphで1項目フローをローカル実行
- [ ] 人間確認ゲート（CLIで simulate）が動く
- [ ] Railwayへデプロイ・短時間起動テスト

### Phase 2：3日ルール作り本番

- [ ] 全項目リスト投入
- [ ] Hermes本格連携
- [ ] OpenClaw下書き連携
- [ ] 外部AIレビュー連携
- [ ] 1日1回進捗サマリ

### Phase 3：移行判断

- [ ] Railway vs VPS のコスト・運用負荷を比較
- [ ] 継続 or 移行を Decision Log に記録

---

## 10. 参照ファイル一覧

### AI思考OS ルール作り

| ファイル | 用途 |
|----------|------|
| `成果物/User Model v0.1.md` | AI判断の圧縮モデル（Tier1） |
| `成果物/AI思考OS_v0.1.md` | AI自身の判断原則（Tier1） |
| `記録/20260719_AI思考OS v0.1 構築記録.md` | 設計判断の背景 |
| `記録/20260719_Grok外部記憶運用ノート v0.1.md` | Grok運用・Tier構造 |

### Pure OS Town（完成済み・参照のみ）

| ファイル | 用途 |
|----------|------|
| `PURE_OS.md` | Town憲法（最上位・変更禁止） |
| `Pure_OS_Town/governance/9999_管理台帳_002.md` | Town管理台帳 |
| `Pure_OS_Town/wiki/Principles/CalmnessAsTopPriority.md` | 穏やかさ原則 |
| `Pure_OS_Town/wiki/Principles/HallucinationPrevention.md` | ハルシネーション防止 |
| `Pure_OS_Town/wiki/WorkPersona/Executor_OpenClaw.md` | OpenClaw Town内定義 |
| `Pure_OS_Town/wiki/OperationRules/PreWorkReading.md` | 作業前必読ルール |
| `Pure_OS_Town/governance/UPDATE_RULES.md` | Schema変更ルール |

### 第二の脳構築日記（教訓）

| ファイル | 用途 |
|----------|------|
| `第二の脳構築日記/ハルシネーション問題.md` | 監査と設計の分離（最重要） |
| `第二の脳構築日記/Gemini-Grok 移行直後/Phase 4｜エコシステム運用ルール作成.md` | 複数AIレビュー・穏やかさ |
| `第二の脳構築日記/Gemini-Grok 移行直後/Phase 5｜ナレッジ索引ファイルの設計.md` | MOC設計 |
| `第二の脳構築日記/Gemini-Grok 移行直後/Phase 6｜プロセス自体のメタ議論.md` | 急がない・流れ作業禁止 |

### Governance（raw_legacy 参照）

| ファイル | 用途 |
|----------|------|
| `Pure_OS_Town/raw_legacy/Grok_Cursor_Era/00_AI_Governance_Constitution.md` | 監査憲法 |
| `SecondBrain/03_AI_Systems/Governance/00_Index.md` | Hermes運用前提 |
| `SecondBrain/03_AI_Systems/Agents/OpenClaw遊撃軍 導入・運用戦略プロトコル（Ver.1.0）.md` | OpenClaw概要 |

---

## 11. 未決定事項（人間確認が必要）

1. **進捗通知**：メール / Telegram / ファイル確認のみ

**確定済み（v0.3）**
- 正式保存先：`AI思考OS_ルール作り_構築記録/成果物/` のみ
- Pure_OS_Town/：安易に変更しない。本システムから書き込まない
- Town役割の置き換え：禁止
- SSoT順序：人生戦略OS → Town憲法 → 成果物 → Railway下書き
- 進行：9項目→8項目（tier統合）、1項目ずつ完走、速度優先度なし
- Hermes：Railway上・**Grok OAuth（月額サブスク・APIキー不要）**。PC HermesはRailway運用中は停止
- 内部チェック：LangGraph・Gemini・最大2回
- 外部レビュー：Gemini・1項目1回
- コスト：基本抑える。効果が大きい有料APIは事前相談

---

## 12. 変更履歴

| 日付 | 版 | 内容 |
|------|-----|------|
| 2026-07-22 | v0.1 Draft | 初版作成 |
| 2026-07-22 | v0.2 Draft | Pure OS Town保護・役割分離・監査/設計分離・SSoT整理・MOC/進行ログ・項目リスト追記 |
| 2026-07-22 | v0.2.1 Draft | Town「変更禁止」→「安易に変更しない」、SSoT順序修正、Memory Policy Tier・優先度A/B/C追記 |
| 2026-07-22 | v0.3 Draft | 内部チェック2回→外部1回→人1回、1項目完走、Hermes=Railway+Grok OAuth/PC停止、Gemini API使い分け、コスト方針 |
| 2026-07-22 | v0.3.1 Draft | HermesのGrok接続をAPI→**xAI Grok OAuth（月額サブスク）**に修正 |

---

**次の一手**：本仕様書のレビュー → 項目リスト確定 → Phase 1 の設置ファイル作成
