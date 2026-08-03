# Mauticとホームページの連携　トラッキングコードを埋め込む | Webマーケティング

タグ: MA, mautic
作成日時: 2018年4月16日 1:13
更新されました: 2018年4月16日 1:13
URL: https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/

# **Mauticとホームページの連携　トラッキングコードを埋め込む**

[2018年1月25日](https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/) [onepirsu](https://webloco.webolha.com/websuccess/author/onepirsu/) [Mautic導入編](https://webloco.webolha.com/websuccess/category/mautic/mautic-installer/), [Mautic操作マニュアル・設定方法](https://webloco.webolha.com/websuccess/category/mautic/), [Mautic設定](https://webloco.webolha.com/websuccess/category/mautic/mautic-setting/)

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled)

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%201)

【２０１８年３月更新】

皆さんこんにちは。

本日は、Mauticとホームページを連携させる方法をご紹介します。

WordPressとMauticを連携させる場合は、プラグインを使えば簡単にできますが、静的なサイトやプラグインが無い場合は、Googleアナリティクスの様に、トラッキングコードを埋め込む必要があります。

WordPressの場合は、[ワードプレスサイトとの連携](http://webloco.webolha.com/websuccess/2016/07/12/mautic-wp/)をご覧ください。

**Contents [[hide](https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/#)]**

- [ ]  [Mauticトラッキングコードの取得](https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/#Mautic)
- [ ]  [Mauticトラッキングコードの貼り付け](https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/#Mautic-2)
- [ ]  
- [ ]  [アノニマスでも、フィンガープリントで訪問者を特定する設定](https://webloco.webolha.com/websuccess/2018/01/25/mautic-tracking/#i-2)

### Mauticトラッキングコードの取得

Mauticの管理画面の右上にある「歯車」をクリックします。

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%202)

「設定」をクリックします。

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%203)

「Tracking Setting」をクリックすると、トラッキングコードが表示されるので、コードをコピーします。

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%204)

### Mauticトラッキングコードの貼り付け

自身のサイトのヘッダーエリア、もしくはフッターエリアに貼り付けます。

その後、Mauticからログアウトした状態で、トラッキングコードを貼り付けたホームページにアクセスします。

ログインした状態でアクセスしても、トラッキングされない仕様になっている為、ログアウトするか、違うブラウザでアクセスする必要があります。

もう一度、Mauticの管理画面にログインして、見事、「ダッシュボード」の「Contact Create」のグラフにアクセスが表示されていれば、正常にトラッキングがされている事になります。

### 

### アノニマスでも、フィンガープリントで訪問者を特定する設定

まだ見込み客情報を得られていないユーザー（アノニマス、もしくはアンノウン）の場合、IPアドレスしか分かりません。

この時、モバイル（スマホ）、ノートPC、タブレットでのアクセスの場合、WiFi環境では、IPアドレスが定期的に変わったりして、同じユーザーなのに、違うユーザーとして扱われてしまう事があります。

そこで、「フィンガープリント（詳細は割愛）」という技術を使って、IPアドレスが変わっても、同じユーザーだという事を紐づけることが出来ます。

その設定をご紹介します。

### １．Mauticの歯車をクリック

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%202)

### ２．「設定（configuration）」をクリックする

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%205)

### ３．「Tracking Settings」⇒赤枠を全て「はい」に選択⇒「適応」をクリック

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%206)

### ４．設定完了

これで、同じユーザーが分割する可能性が少なくなります。

以上「Mauticとホームページの連携　トラッキングコードを埋め込む」をご紹介しました。

スポンサードリンク

[](Mautic%E3%81%A8%E3%83%9B%E3%83%BC%E3%83%A0%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E9%80%A3%E6%90%BA%20%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E5%9F%8B%E3%82%81%E8%BE%BC%E3%82%80%20Web%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0/untitled%201)

## 投稿ナビゲーション

[«Previous Post:2018年版　Mauticのインストール・導入編　オンプレミス型（XSERVER）](https://webloco.webolha.com/websuccess/2018/01/25/mautic-on-premise-2018/)

[Next Post:２月度Mautic MeetUp Nagoya　Mautic 2.12.1新バージョン情報　脆弱性情報»](https://webloco.webolha.com/websuccess/2018/02/02/mmn-release2_12_1/)