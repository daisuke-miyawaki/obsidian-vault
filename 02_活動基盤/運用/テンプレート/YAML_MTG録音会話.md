---
type: template
id: yaml-meeting
title: YAMLテンプレ｜MTG・録音・会話ログ
created: 2026-08-01
updated: 2026-08-01
tags: [template, yaml, meeting]
status: active
obsidian: true
---

# YAMLテンプレ：MTG・録音・会話ログ

## 置き場

独自の大フォルダは作らない。

- お客の話 → `02_活動基盤/実務/お客さん情報/{名前}/進行中/` または `過去案件/`
- 地図への追記 → そのお客の `MOC_お客さん.md`
- 発信・学習だけの会話 → 該当の発信／素材側

```yaml
---
type: meeting
title: 
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: []
status: draft
related: []
source: 
client:            # お客フォルダ名。無ければ空
meeting_date: YYYY-MM-DD
participants: []
media: text        # text | audio | transcript | chat
asset_note:        # 資産になる要点が何か（無ければ後で人間が判断）
---
```
