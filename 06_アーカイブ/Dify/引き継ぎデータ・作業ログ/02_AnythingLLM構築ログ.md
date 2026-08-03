02_AnythingLLM構築ログ.md

作成日：2026-06-18

プロジェクト目的

人生戦略OSをAIで運用するためのローカル環境構築。

使用目的

・自分史分析
・価値観分析
・自己観察OS構築
・第二の頭脳構築
・事業支援
・長期ナレッジ蓄積

現在の構成
LLM

Ollama

モデル

hermes3:latest

Vector Database

LanceDB

Embedding

AnythingLLM Embedder

ワークスペース

人生戦略OS

完了済み
Ollama導入

完了

Hermes3導入

インストール済み

確認済み

ollama list

結果

hermes3:latest
API確認

実施済み

curl http://127.0.0.1:11434/api/tags

正常応答

確認済み

自分史投入

ファイル名

00_自分史.md

ワークスペースへアップロード済み

文字数

約17000文字

発生した問題
Agentモード問題

表示

@agent: Swapping over to agent chat
応答失敗

表示

The agent model failed to respond: fetch failed
症状

・こんにちはでも応答しない

・考え中のまま停止

・画面が重くなる

切り分け結果
Ollama

正常

Hermes

正常

確認

ollama run hermes3

起動成功

API

正常

確認

curl http://127.0.0.1:11434/api/tags

正常応答

推定原因

AnythingLLM側

または

Agent機能側

次回最優先作業

1

AnythingLLM応答問題解決

2

人生戦略OS分析開始

3

ナレッジ追加

候補

10_価値観.md
20_強み弱み.md
30_世界観.md
40_社会と未来.md
50_事業と発信.md
将来構想

共通知識層

↓

人生戦略OS

↓

事業別ワークスペース

↓

各プロジェクト

という構成を検討中