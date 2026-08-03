# AI Governance 目次

## 目的

AI会社構築における「監査・意思決定・レビュー」の土台を、Version1として一元管理する入口。

## 役割

- Governance配下の全ファイルへのリンクを提供する
- 各ファイルの役割とVersionを一覧する
- 更新ルールを定める
- [AI Governance Constitution](00_AI_Governance_Constitution.md) の下位目次として機能する

## Version

**Version 1.0**（2026-07-09 運用開始）

---

## ファイル一覧

| ファイル | 役割 | Version |
|----------|------|---------|
| [00_AI_Governance_Constitution](00_AI_Governance_Constitution.md) | 最高原則（憲法） | V1 |
| [01_AI_Proposal_Policy_V1](01_AI_Proposal_Policy_V1.md) | AI提案の制限ルール | V1 |
| [02_Decision_OS_V1](02_Decision_OS_V1.md) | 提案の採用・保留・却下を判断するOS | V1 |
| [03_AI_Review_Process_V1](03_AI_Review_Process_V1.md) | レビュー工程の標準化 | V1 |
| [04_Change_Log](04_Change_Log.md) | Version変更履歴 | — |
| [05_Session_Notes_2026-07-09](05_Session_Notes_2026-07-09.md) | AI監査OS誕生までの経緯記録 | — |

---

## 役割一覧

| レイヤー | 役割 | 担当ファイル |
|----------|------|--------------|
| **憲法** | 最高原則・禁止事項・凍結ルール | Constitution |
| **提案制限** | 設計の膨張を防ぐ | Proposal Policy |
| **意思決定** | 採用・保留・却下を判定する | Decision OS |
| **レビュー** | 見落とし・反証・証拠を追加する（採決ではない） | Review Process |
| **履歴** | 変更を追跡する | Change Log |
| **記録** | なぜこの仕組みが生まれたかを残す | Session Notes |

---

## Hermes運用前提

本ガバナンスは **Hermes** が遵守する運営ルールである。

Hermesの役割は「提案を増やすAI」ではなく、**「設計を収束させるAI」** である。

複数案が存在する場合は、新規提案より **既存案の統合・整理・簡素化** を優先する。

---

## Version1ルール

- 完成度100%を目指さない。運用可能な状態を優先する
- 改善点は各ファイルの「Version2候補」または [Change Log](04_Change_Log.md) へ記録する
- 不要な新機能・新フォルダ・新ルールは追加しない
- シンプルさと運用性を最優先とする

---

## 更新ルール

1. **内容変更** → 該当ファイルを更新し、[Change Log](04_Change_Log.md) に1行追記する
2. **Version昇格** → ファイル名の `_V1` を `_V2` に変更し、旧版は `98_Archive/` へ移す（将来対応）
3. **新規ルール追加** → Version2候補として記録し、Version1では採用しない（重大リスクを除く）
4. **Index更新** → ファイル追加・Version変更時に本ファイルの一覧表を更新する
5. **管理台帳** → `01_人生戦略OS/9999_管理台帳_001.md` への登録は、構造が安定してから行う

---

## 関連

- [AI Governance Constitution](00_AI_Governance_Constitution.md)
- [AI Proposal Policy](01_AI_Proposal_Policy_V1.md)
- [Decision OS](02_Decision_OS_V1.md)
- [AI Review Process](03_AI_Review_Process_V1.md)
- [Change Log](04_Change_Log.md)
- [Session Notes](05_Session_Notes_2026-07-09.md)
