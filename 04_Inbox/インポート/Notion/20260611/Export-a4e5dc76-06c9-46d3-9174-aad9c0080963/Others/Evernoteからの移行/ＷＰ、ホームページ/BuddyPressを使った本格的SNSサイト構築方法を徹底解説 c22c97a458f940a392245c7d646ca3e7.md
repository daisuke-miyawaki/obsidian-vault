# BuddyPressを使った本格的SNSサイト構築方法を徹底解説

タグ: SNS, WordPress, ワードプレス
作成日時: 2018年6月17日 14:12
更新されました: 2018年6月17日 14:12
URL: https://41y.me/how-to-set-up-buddypress/#Statement

[**ヨンイチワイ**](https://41y.me/)

- [ ]  [ホーム](https://41y.me/)
- [ ]  [Webアプリ](https://41y.me/category/web%e3%82%a2%e3%83%97%e3%83%aa/)

# **BuddyPressを使った本格的SNSサイト構築方法を徹底解説**

2016/08/11
	       		       		2016/08/16

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled)

# **

WordPressを利用して本格的なSNSサイトが作れてしまう”BuddyPress”。

今回はそのBuddyPressを利用した本格的なSNSサイトの構築方法を詳細に説明します。

さらに、ただBuddyPressを設定するだけではなく、標準ではできない写真の投稿もできるようにプラグインを使って構築していきます。

この手順に従ってサイトを構築すれば、あなたも直ぐにSNSサイトのオーナーになれちゃいます！

**目次 [[非表示](https://41y.me/how-to-set-up-buddypress/#)]**

- [ ]  [**目次**](https://41y.me/how-to-set-up-buddypress/#i)
- [ ]  [**今回作成するサイトについて**](https://41y.me/how-to-set-up-buddypress/#i-2)
- [ ]  [**WordPressの初期設定](https://41y.me/how-to-set-up-buddypress/#WordPress)[「サイトのタイトル」と「キャッチフレーズ」の設定](https://41y.me/how-to-set-up-buddypress/#i-3)[「パーマリンク」の設定](https://41y.me/how-to-set-up-buddypress/#i-4)**
- [ ]  [**BuddyPressのインストールと設定](https://41y.me/how-to-set-up-buddypress/#BuddyPress)[BuddyPressプラグインのインストール](https://41y.me/how-to-set-up-buddypress/#BuddyPress-2)[BuddyPressの初期設定](https://41y.me/how-to-set-up-buddypress/#BuddyPress-3)**
- [ ]  [**テーマの設定](https://41y.me/how-to-set-up-buddypress/#i-5)[Statementテーマの設定①](https://41y.me/how-to-set-up-buddypress/#Statement)[Statementテーマの設定②](https://41y.me/how-to-set-up-buddypress/#Statement-2)[サイトを表示し確認する](https://41y.me/how-to-set-up-buddypress/#i-6)**
- [ ]  [**ウィジェットの追加](https://41y.me/how-to-set-up-buddypress/#i-7)[ウィジェットの追加①](https://41y.me/how-to-set-up-buddypress/#i-8)[ウィジェットの追加②](https://41y.me/how-to-set-up-buddypress/#i-9)[サイトを表示し確認する](https://41y.me/how-to-set-up-buddypress/#i-10)**
- [ ]  [**写真を投稿できるようにする](https://41y.me/how-to-set-up-buddypress/#i-11)[BuddyPress Activity Plusプラグインのインストール](https://41y.me/how-to-set-up-buddypress/#BuddyPress_Activity_Plus)[サイトを表示し確認する](https://41y.me/how-to-set-up-buddypress/#i-12)**
- [ ]  [**ユーザー登録できるようにする](https://41y.me/how-to-set-up-buddypress/#i-13)[登録用の固定ページの作成](https://41y.me/how-to-set-up-buddypress/#i-14)[ユーザー登録の設定](https://41y.me/how-to-set-up-buddypress/#i-15)[BuddyPressの設定](https://41y.me/how-to-set-up-buddypress/#BuddyPress-4)[サイトを表示し確認する](https://41y.me/how-to-set-up-buddypress/#i-16)**
- [ ]  [**まとめ**](https://41y.me/how-to-set-up-buddypress/#i-17)

## **目次**

- [ ]  **1**今回作成するサイトについて
- [ ]  **2**WordPressの初期設定
- [ ]  **3**BuddyPressのインストールと設定
- [ ]  **4**テーマの設定
- [ ]  **5**ウィジェットの追加
- [ ]  **6**写真を投稿できるようにする
- [ ]  **7**ユーザー登録できるようにする
- [ ]  **8**まとめ

## **今回作成するサイトについて**

今回はBuddyPressを使って下の画面のようなサイトを作ります。

タイムラインでは、写真や動画の投稿もできるようにします。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%201)

グループを作成することもできます。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%202)

## **WordPressの初期設定**

最初にWordPressの初期設定を行います。

### **「サイトのタイトル」と「キャッチフレーズ」の設定**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%203)

- [ ]  **9**「設定」メニューの「一般」をクリック
- [ ]  **10**「サイトのタイトル」と「キャッチフレーズ」を入力（それぞれ自由に決めてください）
- [ ]  **11**「変更を保存」をクリック

### **「パーマリンク」の設定**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%204)

- [ ]  **12**「設定」メニューの「パーマリンク設定」をクリック
- [ ]  **13**「投稿名」にチェック(お好きなパーマリンク構造を選択してください)
- [ ]  **14**「変更を保存」をクリック

## **BuddyPressのインストールと設定**

WordPressの設定が完了したら、BuddyPressのインストールと設定をします。

### **BuddyPressプラグインのインストール**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%205)

- [ ]  **15**「プラグイン」メニューをクリック
- [ ]  **16**「新規追加」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%206)

BuddyPressの「今すぐインストール」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%207)

「プラグインを有効化」をクリック

### **BuddyPressの初期設定**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%208)

- [ ]  **17**「設定」メニューをクリック
- [ ]  **18**「BuddyPress」をクリック
- [ ]  **19**「サイトトラッキング」を除くすべてにチェック
- [ ]  **20**「設定を保存」をクリック

## **テーマの設定**

BuddyPressの初期設定が完了したらテーマを設定します。

今回はStatementというテーマを利用します。Statement以外のテーマでも大丈夫ですので、好みに合わせて変更してくださいね。

### **Statementテーマの設定①**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%209)

- [ ]  **21**「外観」メニューをクリック
- [ ]  **22**「新規追加」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2010)

「statement」と入力

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2011)

Statementの「インストール」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2012)

「有効化」をクリック

### **Statementテーマの設定②**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2013)

Statementの「カスタマイズ」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2014)

- [ ]  **23**Set Front Pageをクリックし以下のように設定する

フロントページの表示： 固定ページ

フロントページ： アクティビティ

- [ ]  **24**Layoutをクリックし以下のように設定する

Container Width: 1200px

Footer Widget: 0

- [ ]  **25**「保存して公開」をクリック

### **サイトを表示し確認する**

ここまでできたら一旦サイトを表示して確認してみましょう。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2015)

ヘッダーのサイト名をマウスでホバーし「サイトを表示」をクリックする

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2016)

このような画面が表示されているれば大丈夫です。

ここでアクティビティを投稿し、登録されることを確認しておきましょう。

## **ウィジェットの追加**

BuddyPressを使いやすくするために、ページの右側に表示されるサイドバーにウィジェットを設定します。

今回は以下の3つのウィジェットを追加します

・(BuddyPress)ログイン

・(BuddyPress)グループ

・(BuddyPress)メンバー

### **ウィジェットの追加①**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2017)

- [ ]  **26**「外観」メニューをクリック
- [ ]  **27**「ウィジェット」をクリック
- [ ]  **28**Right Sidebarの「検索」を開き「削除」をクリック
- [ ]  **29**下の図のようにRight Sidebarが空になるまで、同様に他のウィジェットを削除する

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2018)

### **ウィジェットの追加②**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2019)

利用できるウィジェットにある以下のウィジェットをRight Sidebarへドラッグアンドドロップする

・(BuddyPress)ログイン

・(BuddyPress)グループ

・(BuddyPress)メンバー

### **サイトを表示し確認する**

サイトを表示してウィジェットを確認してみましょう。

下の図のように、右側にユーザー情報、グループ、メンバーが表示されていると思います。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2020)

ここまででBuddyPressの標準的な設定は完了です。

ただ、このままだと写真が投稿できないので、追加のプラグインを使って写真を投稿できるようにしていきます。

## **写真を投稿できるようにする**

写真の投稿にはBuddyPress Activity Plusというプラグインを利用します。

### **BuddyPress Activity Plusプラグインのインストール**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%205)

- [ ]  **30**「プラグイン」メニューをクリック
- [ ]  **31**「新規追加」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2021)

プラグインの検索と書かれたところに「BuddyPress Activity Plus」を入力しエンター

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2022)

BuddyPress Activity Plusの「今すぐインストール」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2023)

「プラグインを有効化」をクリック

### **サイトを表示し確認する**

サイトを表示して写真の投稿ができることを確認してみましょう。

下のような画面が表示されているのを確認したら、アクティビティから画像を投稿してみてください。

画面をリフレッシュしてみると、投稿した画像が表示されていると思います。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2024)

## **ユーザー登録できるようにする**

今の状態では、投稿できるのはあらかじめサイトに登録されているユーザーだけになってしまいます。

多くの人にサービスを使ってもらうために、ユーザー登録をできるようにしましょう。

### **登録用の固定ページの作成**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2025)

- [ ]  **32**「固定ページ」メニューをクリック
- [ ]  **33**「新規追加」をクリック

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2026)

- [ ]  **34**タイトルに「登録」と入力
- [ ]  **35**パーマリンクの「登録」を「register」に変更する
- [ ]  **36**「公開」ボタンをクリック

上記と同じ方法で以下のページを作成してください。

タイトル：有効化

パーマリンク：activation

### **ユーザー登録の設定**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2027)

- [ ]  **37**「設定」メニューの「一般」をクリック
- [ ]  **38**「だれでもユーザー登録ができるようにする」にチェックを入れる
- [ ]  **39**「変更を保存」をクリック

### **BuddyPressの設定**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2028)

- [ ]  **40**「設定」メニューをクリック
- [ ]  **41**「BuddyPress」をクリック
- [ ]  **42**「固定ページ」タブを開く
- [ ]  **43**「登録」ドロップダウンで「登録」を選ぶ
- [ ]  **44**「有効化」ドロップダウンで「有効化」を選ぶ
- [ ]  **45**「設定を保存」をクリックする

### **サイトを表示し確認する**

サイトを表示して、ユーザー登録ができることを確認してみましょう。

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2029)

- [ ]  **46**ログアウトする
- [ ]  **47**右側のウィジェットに「登録」リンクがあることを確認する
- [ ]  **48**「登録」リンクをクリックしてユーザーを登録してみてください

## **まとめ**

以上でBuddyPressを利用したSNSサイトの構築は完了です。

このようにWordPressにBuddyPressを追加すると、単にブログサイトを作るだけではなく、SNSなどWebサービスも作ることができます。

また今回インストールしたBuddyPress Activity Plusのように、BuddyPress用のプラグインも多数公開されていますから、色々なプラグインをインストールしてサイトを拡張していくのも面白いので、ぜひ挑戦してみてください。

**SHARE      
          
          
• [ ] [ツイート](http://twitter.com/share?url=https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F&text=BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BD%9C%E3%83%A8%E3%83%B3%E3%82%A4%E3%83%81%E3%83%AF%E3%82%A4)
              

          
          
• [ ] [シェア](http://www.facebook.com/share.php?u=https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F&t=BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BD%9C%E3%83%A8%E3%83%B3%E3%82%A4%E3%83%81%E3%83%AF%E3%82%A4)
              

          
          
• [ ] [B!はてブ](http://b.hatena.ne.jp/add?mode=confirm&url=https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F)
              

          
                        
• [ ] [Google+](https://plus.google.com/share?url=https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F)
                  
          
          
          
• [ ] [Pocket](http://getpocket.com/edit?url=https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F&title=BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BD%9C%E3%83%A8%E3%83%B3%E3%82%A4%E3%83%81%E3%83%AF%E3%82%A4)
              

          
          
• [ ] [LINE](http://line.me/R/msg/text/?https%3A%2F%2F41y.me%2Fhow-to-set-up-buddypress%2F%0D%0ABuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BD%9C%E3%83%A8%E3%83%B3%E3%82%A4%E3%83%81%E3%83%AF%E3%82%A4)**

**CATEGORY :
• [ ] [Webアプリ](https://41y.me/category/web%e3%82%a2%e3%83%97%e3%83%aa/)               	               		
TAGS :
• [ ] [#BuddyPress](https://41y.me/tag/buddypress/)/
• [ ] [#SNS](https://41y.me/tag/sns/)/
• [ ] [#Webサービス](https://41y.me/tag/web%e3%82%b5%e3%83%bc%e3%83%93%e3%82%b9/)**

- [ ]  [**WordPressでWebサービス作ったよ！のまとめ**](https://41y.me/web-service-based-on-wordpress/)
    
    ![](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/background051.gif)
    
- [ ]  [**WP-MembersでBootstrapを使う方法**](https://41y.me/bootstrap-with-wp-members/)
    
    [](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2030)
    
- [ ]  [**WP-Members：ユーザー登録時のエラーメッセージを日本語にする方法**](https://41y.me/wp-members-error-message-in-japanese/)
    
    [](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2031)
    
- [ ]  [**無料でここまで！お勧めのWordPressテーマOnePressの設定方法を徹底解説**](https://41y.me/how-to-set-up-onepress/)
    
    [](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2032)
    
- [ ]  [**WordPressのナビゲーションメニューを権限で変えるプラグイン**](https://41y.me/nav-menu-roles/)
    
    [](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2033)
    
- [ ]  [**WordPressで投稿時にバリデーションを行う方法**](https://41y.me/validate-post/)
    
    [](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2034)
    

### **1 Comment**

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/bc48d51277569b3407377645d3b3bd43)

**jinrikisha164**           [*2017年8月7日*](https://41y.me/how-to-set-up-buddypress/#comment-184)

いろいろなところをぐぐりましたが解決されず、このサイトのおかげで構築できました。ココまで細かく説明されているところはありません。ありがとうございます。

[**返信する**](https://41y.me/how-to-set-up-buddypress/?replytocom=184#respond)

**コメントを残す** 			メールアドレスが公開されることはありません。 * が付いている欄は必須項目です
コメント 
名前 * 
メールアドレス * 
ウェブサイト 
次回のコメントで使用するためブラウザーに自分の名前、メールアドレス、サイトを保存する。

[**** 前の記事**
					
				リーンスタートアップで起業の成功率を高める方法を徹底解説](https://41y.me/about-lean-startup/)
			
		
		[**次の記事 ****WordPressでWebサービスを作るならテーマはOnePr…](https://41y.me/recommend-onepress/)
												    
				
			
				
**プロフィール**

**深谷正人**

こんにちは。

「マッチングサービス構築アドバイザー」の深谷です。

私はもともと起業前はマイクロソフトで10年にわたり正社員のエンジニアとしてポータルサイトであるmsnの開発を行っていました。

そして起業後は「企業と全国のライターをマッチングするPVモンスター」と「転職希望者と転職エージェントをマッチングするエントリーモンスター」という二つのマッチングサービスの開発と運営をしています。

この二つのサイトを立ち上げるときや、立ち上げた後にも様々な困難を経験し、乗り越えてきましたので、ただサイトを作る方法を教えるだけではなく、サービスの企画や、集客、運営ノウハウなど、マッチングサービスを始めるために必要な全ての知識を幅広くお教えしています。

ご興味のある方はぜひお気軽にご質問・ご相談ください。

お問い合わせは[こちら](https://41y.me/contact)        
**人気記事**                          
• **[ ] 1                        [WordPressでWebサービス作ったよ！のまとめ](https://41y.me/web-service-based-on-wordpress/)**
• **[ ] 2                        [マッチングサービスのビジネスモデルとは。それぞれの特徴をまとめてみた。](https://41y.me/business-model-of-matching-service/)**
• **[ ] 3                        [無料でここまで！お勧めのWordPressテーマOnePressの設定方法を徹底解説](https://41y.me/how-to-set-up-onepress/)**
• **[ ] 4                        [BuddyPressを使った本格的SNSサイト構築方法を徹底解説](https://41y.me/how-to-set-up-buddypress/)**
• **[ ] 5                        [WordPressでWebサービスを作るならテーマはOnePressがお勧め！](https://41y.me/recommend-onepress/)**
• **[ ] 6                        [BuddyPressと相性のいいWordPressのシンプルな無料テーマ7選（スクリーンショット付き）](https://41y.me/free-theme-for-buddypress/)**
• **[ ] 7                        [起業や副業の参考に！空きリソースを使ったマッチングサービスをまとめて紹介](https://41y.me/free-resource-matching-service/)**
• **[ ] 8                        [WordPressで簡単にフロントエンドからデータを入力できるようにする方法](https://41y.me/edit-article-on-front-end-ui/)**
• **[ ] 9                        [スキルを持った人に依頼できるマッチングサービスをまとめました](https://41y.me/domestic-skill-share-service-selection/)**
• **[ ] 10                        [WordPressで投稿時にバリデーションを行う方法](https://41y.me/validate-post/)
WordPressのサポートやってます**			
WordPressで困ったことや相談したいことがあれば、ぜひご活用ください。

全力で解決いたします。

**カテゴリー**		
• **[ ] [Webアプリ](https://41y.me/category/web%e3%82%a2%e3%83%97%e3%83%aa/)**
• **[ ] [コラム](https://41y.me/category/%e3%82%b3%e3%83%a9%e3%83%a0/)**
• **[ ] [プロダクト](https://41y.me/category/%e3%83%97%e3%83%ad%e3%83%80%e3%82%af%e3%83%88/)**
• **[ ] [マッチングサービス](https://41y.me/category/%e3%83%9e%e3%83%83%e3%83%81%e3%83%b3%e3%82%b0%e3%82%b5%e3%83%bc%e3%83%93%e3%82%b9/)**
• **[ ] [複業の始め方](https://41y.me/category/small-business/)**
        
        
    

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2035)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2036)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2037)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2038)

![](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/background051.gif)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2039)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2040)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2041)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2040)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2042)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2043)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2044)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2045)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2046)

[](BuddyPress%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E6%9C%AC%E6%A0%BC%E7%9A%84SNS%E3%82%B5%E3%82%A4%E3%83%88%E6%A7%8B%E7%AF%89%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC/untitled%2047)

[** HOME](https://41y.me/)

						© 2018						ヨンイチワイ						All rights reserved.

[プライバシーポリシー](https://41y.me/privacy)[特定商取引法に関する表示](https://41y.me/tokushou)