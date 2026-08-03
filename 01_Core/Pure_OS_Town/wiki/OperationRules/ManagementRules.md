# ManagementRules - Pure OS Town Operation Rules

**Bead ID**: OR-Management-001
**Version**: v1.0 (Town仕様に再構築)
**Patrol Review**: PASSED

## 管理台帳の正本性
- 管理台帳は常に `Pure_OS_Town/governance/9999_管理台帳_002.md` を唯一の正本とする（Zero-Base再構築完了）。
- ファイル追加・変更・削除時は必ず最新版を更新。
- 古い管理台帳（001）はraw_legacy/へ凍結済み。最新版（002）のみを参照。

## 4桁番号体系（固定・絶対）
- 番号は4桁（先頭0埋め）で固定。一度付与した番号は変更禁止。
- XX00 = その番台の親（中心ファイル）。
- 同じ上2桁はすべてその親の下位とする。
- 9999番は管理台帳専用で永久予約。

## Patrol監視ルール
- 番号変更や新規ファイル無許可作成は即時driftとして拒否。
- 過去体系への忖度（古い番号体系への回帰）は明確な違反。

**Patrol署名**: このルールはPURE_OS.mdと宇宙の法則に100%準拠。Synthesized Wiki層に登録。
