# 古い記事に警告文を表示することができるWordPressプラグイン「WP Posts Date Alert」

タグ: WP, WardPless, プラグイン, ワードプレス, 古い, 古い記事, 記事
作成日時: 2018年6月3日 11:47
更新されました: 2018年6月3日 11:47
URL: http://techmemo.biz/wordpress/wp-posts-date-alert/

## 古い記事に警告文を表示することができるWordPressプラグイン「WP Posts Date Alert」

[himecas](http://techmemo.biz/author/himecas/)

[2015/08/11](http://techmemo.biz/wordpress/wp-posts-date-alert/)

[Wordpress](http://techmemo.biz/wordpress/)

[2 Comments](http://techmemo.biz/wordpress/wp-posts-date-alert/#comments)

[](%E5%8F%A4%E3%81%84%E8%A8%98%E4%BA%8B%E3%81%AB%E8%AD%A6%E5%91%8A%E6%96%87%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8BWordPress%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%80%8CWP%20Posts%20Date%20Al/untitled)

- シェアしてね♪
- 
- 
- 
- 
- 
- [74](http://feedly.com/i/subscription%2Ffeed%2Fhttp%3A%2F%2Ftechmemo.biz%2Ffeed%2F)
    
    ![](%E5%8F%A4%E3%81%84%E8%A8%98%E4%BA%8B%E3%81%AB%E8%AD%A6%E5%91%8A%E6%96%87%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8BWordPress%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%80%8CWP%20Posts%20Date%20Al/feedly-follow-rectangle-flat-small_2x.png)
    

---

- [Youtube動画変換・ダウンロードおｋ！](https://www.fonepaw.jp/video-converter/?rs=techmemo)
    
    [](%E5%8F%A4%E3%81%84%E8%A8%98%E4%BA%8B%E3%81%AB%E8%AD%A6%E5%91%8A%E6%96%87%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8BWordPress%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%80%8CWP%20Posts%20Date%20Al/untitled%201)
    
- 
- 
- 
- 
- 

WP Posts Date Alertは、投稿日から指定した期間を過ぎた記事に警告文を表示させることができるWordPressプラグインです。

技術的な内容を書いているブログでは、何年か前に書いた記事の内容が、今では全く使えなくなっていることなんてザラだと思います。そんなブログでは、古くなった記事に「この記事は投稿から2年以上が経過しています」といった文言を追加しておくとより親切かもしれませんね。

スポンサードリンク

**WP Posts Date Alertのインストール**
WP Posts Date Alertは、WebCakeさんが配布しており、公式ディレクトリには登録されていません。そのため、WebCakeさんの[配布ページ](http://webcake.no003.info/webdesign/wp-posts-date-alert.html)からプラグインをダウンロードする必要があります。
そんなプラグイン配布の記事が、すでに1年以上経過していて、警告メッセージが表示されていますが・・・^^; 現行最新バージョン(2015/08/11時点)であるWordPress4.2.4でも正常に動作しました。
インストール手順は、以下の通りです。
1. WP Posts Date Alertをダウンロードします。
2. ダウンロードしたファイルを展開し wp-content/plugins にアップロードします。
3. 管理画面の[プラグイン]ページで、WP Posts Date Alertプラグインを有効化します。
**WP Posts Date Alertの設定**
プラグインを有効化したら、[設定] – [WP Posts Date Alert]にアクセスして設定を行います。

期間古い記事だと判別するための期間を数字で入力します。年日期間に入力した数字の単位(年or日)を選択します。メッセージ古い記事に表示させたいメッセージを入力します。出力メッセージを出力する場所を選択します。オプションオプション機能を設定します。
**任意の場所に出力する**
本文の前や後ではなく、テーマ内の任意の場所にメッセージを出力したい場合は、出力設定で「自動出力せずテンプレートタグを使用する」を選択します。
そのうえで、テーマ内の出力したい場所に以下のコードを追加します。1`<?php if` `( function_exists( 'wppda_alert'` `) ) wppda_alert(); ?>`
**オプションについて**
「プラグイン付属のCSSを使う」と「<div id=”wppda_alert”>～</div>で括る」の両方にチェックを入れると、以下のような表示になります。

自分でCSSをカスタマイズしたい場合は、「<div id=”wppda_alert”>～</div>で括る」にだけチェックを入れておきましょう。警告メッセージが#wppda_alertで内包されるので、CSSをカスタマイズします。

[](%E5%8F%A4%E3%81%84%E8%A8%98%E4%BA%8B%E3%81%AB%E8%AD%A6%E5%91%8A%E6%96%87%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8BWordPress%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%80%8CWP%20Posts%20Date%20Al/untitled%202)

[](%E5%8F%A4%E3%81%84%E8%A8%98%E4%BA%8B%E3%81%AB%E8%AD%A6%E5%91%8A%E6%96%87%E3%82%92%E8%A1%A8%E7%A4%BA%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8BWordPress%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%80%8CWP%20Posts%20Date%20Al/untitled%203)