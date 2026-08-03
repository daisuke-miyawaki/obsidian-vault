# SiteGuard設定 WordPressセキュリティプラグイン

タグ: BookMark, WebSite, WordPress, プラグイン
URL: https://blog-bootcamp.jp/start/wordpress-siteguardwp/
作成日: 2023年8月3日 12:51

<aside>
🔑 基本的な設定

- **管理ページアクセス制限：ON**
- **ログインページ変更：ON、URL変更、オプションチェック入れる**
- 画像認証：ONのまま
- ログイン詳細エラーメッセージの無効化：ONのまま
- ログインロック：ON（厳→30秒3回失敗で5分アウト）
- ログインアラート：ONのまま
- フェールワンス：ON
- XMLRPC防御：ONのまま、**XMLRPC無効化に変更（投稿でAPP使う場合注意）**
- **更新通知：ON**
- WAFチューニングサポート：初期のまま、**(WAF誤検知が起きたら除外設定でも)**
</aside>