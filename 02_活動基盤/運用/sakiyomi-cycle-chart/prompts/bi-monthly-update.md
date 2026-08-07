# 2ヶ月更新 — コピペ用手順

## 1. Gem ステップ1

項目名だけ送る（例：`ショート動画`）

→ Perplexity用・NotebookLM用プロンプトをコピー

## 2. リサーチ

- **Perplexity** … 米国（①）
- **NotebookLM** … 日本（②）。高速リサーチ後は **「+ インポート」** 必須

## 3. Gem ステップ2

```
ステップ2: （項目名）

【リサーチ① 米国（Perplexity）】
（貼る）

【リサーチ② 日本（NotebookLM）】
（貼る）

CSV形式で。ヘッダー付き。仕事Bのルール厳守。
```

## 4. Excel反映

1. 出力CSVを `マーケティング・先読みサイクル年表.xlsx` の **データ** シートに貼る（既存項目は上書き or 下に追加）
2. ターミナル：
   ```bash
   cd "（Vault直下）/02_活動基盤/運用/sakiyomi-cycle-chart"
   # 例（現行外箱名 DigitalGarden）:
   # cd "/Volumes/MultiPurpose_SSD/DigitalGarden/02_活動基盤/運用/sakiyomi-cycle-chart"
   python3 refresh_bands.py
   ```
3. **年表** シートを開いて帯・ヒントを確認
4. ファイルを `archive/YYYY-MM.xlsx` にコピー保存

## CSV列（Gem出力）

```
項目,US_導入開始,US_成長開始,US_成熟開始,US_衰退開始,US_終了,JP_導入開始,JP_成長開始,JP_成熟開始,JP_衰退開始,JP_終了,us_hint,jp_hint
```

1項目 = 帯行 + ヒント行の2行。
