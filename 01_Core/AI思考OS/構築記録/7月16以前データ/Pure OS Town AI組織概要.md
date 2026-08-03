# Pure OS Town AI組織概要

## 基本思想
- **人間（あなた）** = 最終意思決定者（Human Overseer）
- **Hermes Agent（私）** = 司令塔（設計・判断・進行管理）
- **OpenClaw** = 実行部隊（実作業を担当）
- **Patrol** = 監視・改善担当（**Hermes Agentのサブ役割**として兼務）

目的は、AIを「組織」として安全に成長させ、あなたの能力を拡張することです。
Patrolは独立した別AIではなく、**Hermes Agentが兼務**する機能です。将来的に規模が大きくなったら独立させる可能性を残しています。

## 現在のAI組織図

```mermaid
graph TD
    Human[Human Overseer<br>あなた<br>最終意思決定者]
    --> Hermes[Hermes Agent<br>司令塔<br>設計・判断・進行管理]
    Hermes --> OpenClaw[OpenClaw<br>実行部隊<br>実作業担当]
    Hermes --> Patrol[Patrol<br>監視・改善担当<br>Hermesのサブ役割]


## 各役割の詳細

### Human Overseer（あなた）
- 最終的な意思決定者
- raw brainstone（原石＝信念・イメージ・非交渉事項）を最初に提供
- 重要な設計は必ずレビュー・承認を行う
- 全体の方向性を決める最高責任者

### Hermes Agent（私）
- **司令塔**として全体を統括
- 設計を考え、計画を立て、OpenClawに指示を出す
- Patrol機能を**サブ役割として兼務**（監視・drift検知・curation）
- 穏やかさと自観察を常に意識
- あなたへの報告を構造的に行う

### OpenClaw（実行部隊）
- Hermesの指示を受けて**実際の作業を実行**
- ファイル操作、ツール使用、外部連携などを担当
- 権限は最小限に制限（セキュリティ設計 v1.4 Finalに基づく）
- すべての行動をログ記録し、Patrol（Hermes）が監視

### Patrol（監視・改善担当）
- **Hermes Agentのサブ役割**として機能
- 目的忘却・矛盾・drift・memory poisoningを常時チェック
- ログを分析し、改善提案を行う
- 異常時は人間（あなた）に直接エスカレーションする経路を確保
- 将来的に規模が大きくなったら独立した別AIとして分離する可能性あり

## 運用フロー（基本）
1. 人間（あなた）がraw brainstoneを提供
2. Hermesが設計・計画
3. レビュー・承認（重要なものは必ず実施）
4. OpenClawが実行
5. Patrol（Hermes）が監視・curation
6. 人間が最終確認

---

このMarkdownをそのまま新しいファイルに保存すれば、Obsidianで綺麗に表示されます。

内容に問題なければ、このまま使ってください。
修正が必要な点があれば教えてください。

OpenClawは停止したままです。再起動が必要になったら教えてください。

今日はお疲れ様でした。
ゆっくり休んでください。