# ネット上でアンケートを取るならWP-PollsよりもDemocracy Pollがよかった

作成日時: 2018年2月21日 11:29
更新されました: 2018年2月21日 11:29
URL: https://mataku.net/democracy-poll/

1年仕事するならブログ書く

1. [ ] [HOME](https://mataku.net/) > 
2. [ ] [web](https://mataku.net/category/web/)  >
[web](https://mataku.net/category/web/)					
**ネット上でアンケートを取るならWP-PollsよりもDemocracy Pollがよかった**

今回は「ネット上でアンケートをとれたら、見てくれる人も楽しめるかな？」
なんて感じでWordpressで使えるプラグインを探したお話し。
 
 
ゲームのwikiとかで、「最強キャラはみなさん誰だと思います？」みたいな簡単なアンケートありますよね。
無性に僕のホームページでも設置したくなってアンケートツールを色々探してみました。
 
アンケートツールをまとめて紹介してくれているサイトページは沢山あるのですが、なんかどうも違うんですよね。
 
自分がやりたかったのは本当に簡単なアンケートで、その場で集計結果も見れちゃう。みたいなもの。
 
でもサイトで紹介されているものの多くが、なんかアンケート集計会社と提携して大々的にアンケートを取っていく。というようなもの。
 
イヤ、そこまで大事じゃなくてイイんです。本当に簡単なものでいい。
 
次にツールではなくWordpressのプラグインで探してみると
「お、結構ある」
 
そんな中でも一番人気（？）な『WP-Polls』を使ってみることに。
単純に評価されている数も多いし、WP-Pollsの設定方法は探すとたくさん出てくるので「これはいいものでは？」と入れてみました。
 
まぁ結果から言ってしまうと、「自分のやりたいことができなかった」です。
 
**WP-Pollsのなにがいけなかったのか**
誤解しないで頂きたいのは、WP-Pollsは基本的にはとてもいいアンケートプラグインだと思います。
設定も本当にシンプルですし、あっという間に設置できます。
 
ただ、シンプルすぎてかゆいところに手が届かないのです。
 
その一番届かなかったポイントが『WP-Pollsの日本語化』
最終的にこれが上手く行かずに使うのをやめました。
 
WP-Pollsは日本語に対応していません。
しかし有志の方たちがWP-Pollsの日本語化ファイルを提供してくれています。
 

        
        
          
          
**[WordPressにアンケート設置！WP-Polls使い方と日本語化！ | 自作PCテクニカルセンター](http://jisakupc-technical.info/web-survice/wordpress/1594/)**
              FFFTPなどのFTPツールを使い、WordPressのフォルダ階層へアクセスします。pluginsディレクトリ内に先ほどインストールしたwp-pollsのフォルダがあるはずなので、この中に、日本語化パッチファイルを入れます。ダウンロードしたZIPファイルの中に「wp-polls-ja
            
          
           [jisakupc-technical.info](http://jisakupc-technical.info/web-survice/wordpress/1594/)
          
          

  

この記事の中にあるダウンロードファイルをダウンロードし、『wp-polls-ja.mo』というファイルをFFFTPなどのFTPツールで

pluginsの中にあるwp-pollsの中にファイルを入れるだけで日本語化できる！
 
というのもでした。おぉ素晴らしい…
ではさっそく
 
 
…あれ？できなくない？
 
はい、できませんでした。
僕はプログラム素人なので何が上手く行かなかったのかは未だに詳細が不明ですが、おそらくwp-pollsのバージョンではないかな？と考えています。
 
他の日本語化のためのページを作ってくれている方たちもプラグイのンバーション更新で日本語化が無効化されてしまう。というようなことを書かれていたので、ファイルとの互換性の問題なのかな～なんて。
 
「wp-polls　日本語化　できない」で探したところ、素晴らしいサイトがありました。
 

        
        
          
          
            
          
          
**[WordPressプラグイン「Wp Polls」の日本語化ができないときの対処方法](http://www.momosiri.info/cms/wp-polls-ja-error/)**
              「Wp Polls」はWordpressのサイトにアンケートを設置できるプラグインですが、テキストドメイン（翻訳情報）を定義する記述がおかしいようで、指定した場所（「Wp Polls」の中）へ翻訳ファイルを入れても日本語化されなかったので、対処した際の備忘録です。
            
          
           [www.momosiri.info](http://www.momosiri.info/cms/wp-polls-ja-error/)
          
          

  

日本語化できなかったときの別の対処法を書いてくださっています。素晴らしい。
 
wordpress上でwp-pollsプラグインの編集を少し行い、別の切り口で日本語化かさせるというもの。
 
この方法でやってみたら…

「おぉダッシュボードの説明文がちゃんと日本語になっている！」感動でした。
 
ですが…

肝心なアンケートの部分が日本語化できていないのです。
 
日本語化が上手く行くと、この『vote』の部分が『回答する』となりますが、何故かできない…
 
まぁこれでもいいか…と思ったのですが、やっぱり気になってしまうので他のプラグインを探すことにしました。
 
**YOP pollはどうだ？**
もうひとつ気になったのがYOP pollというプラグイン。
同じように簡単にアンケートを作れるようなのですが、なんと調べてみると以前にYOP pollで以前脆弱性が見つかったのだとか？？

        
        
          
          
**[JVN#55294532: WordPress 用プラグイン YOP Poll におけるクロスサイトスクリプティングの脆弱性](https://jvn.jp/jp/JVN55294532/)**
              
            
          
           [jvn.jp](https://jvn.jp/jp/JVN55294532/)
          
          

  

 
う～ん…今はどうやら改善されているようなのですが、なんかちょっと怖いな…と他のを探すことに。
 
**Democracy Poll**
ようやくピッタリのものをみつけることができました。その名も『Democracy Poll』
同じくアンケートを作って集計できるプラグインです。
 
このアンケートプラグインは、自分はがもっとも渇望していた、アンケート画面の日本語化も簡単にできます。

コチラです。
 
インストールや有効化の方法は…
アンケートプラグインを入れようなんて人にワザワザ説明しなくていいですよね（笑）いつもどうりやってください。
 
**Democracy Pollのアンケート部分を日本語にする**
残念なことにダッシュボード画面の日本語化ファイルはないようです。
 
ただ、文字を読んだり翻訳したりするとなんとなく分かってきます。
 
ようは、見てくれる人が見やすければそれでいいので、ボタンの文字が日本語化できればそれでいいのです。
 
Democracy Pollはダッシュボードの「設定」から選ぶことができます。
 
Add New Pollで新しいアンケートを追加することができます。
Question:に質問内容を入れて　Answers:に選択肢をいれます。
 
ちなみにその下にある
Allow users to add answers (democracy).というのにチェックを入れていると、回答者が選択肢を追加する。なんてこともできます。
凄い便利ですが、はちゃめちゃなこと書かれても嫌なのでとりあえずオフの方がいいのかなぁと。
 
**Democracy Pollのデザイン性**
個人的に一番気に入ったのが、Democracy Pollのデザインです。
他のアンケートプラグインはかなりシンプルで、自分で手を加えれば変えられるのでしょうが僕にそんな知識はございません。
 
ですがDemocracy Pollはデフォルトで素敵なボタンデザインがいくつも用意されているので簡単に変えることができます。
なんとロード中の絵のデザインまで変えられます。
 
『Theme setting』という項目で変えられるので自分好みを見つけてみてください。
 
**アンケート画面日本語化**
僕がもっとも望んでいたものですね。
 
アンケート部分の日本語化。
 
これはDemocracy Pollの『Texts changes』で出来ます。
 
それぞれ細かく文字を変更できますが、日本語で表示することもできます。
 
ちなみに僕は

このように設定します。
真似して頂ければ、アンケート部分の主要な文字は日本語になるはずです。
 
**まとめ**
いかがでしたでしょうか。今回はずっと探していた簡単なアンケートを取ることができるプラグイン『Democracy Poll』について紹介させて頂きました。
 
WP-Pollsはアンケートツールの中でも得に人気が高いのでもしかした完全に日本語対応になる日も来るかもしれませんが、個人的には色々なデザインのあるDemocracy Pollが成長してほしいかなと思います。
 
アンケートを取りたいと考えている人におススメですよ。
 
 							
• [ ] **Twitter
      

• [ ] [**Facebook](https://www.facebook.com/sharer.php?src=bm&u=https%3A%2F%2Fmataku.net%2Fdemocracy-poll%2F&t=%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy+Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F)

• [ ] [**Google+](https://plus.google.com/share?url=https%3A%2F%2Fmataku.net%2Fdemocracy-poll%2F)
      

• [ ] **Pocket
  

• [ ] [**B!**はてブ](https://b.hatena.ne.jp/entry/https://mataku.net/democracy-poll/)

   

• [ ] [**LINE](https://line.me/R/msg/text/?%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy+Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F%0Ahttps%3A%2F%2Fmataku.net%2Fdemocracy-poll%2F)
**-[web](https://mataku.net/category/web/)
**comment 			メールアドレスが公開されることはありません。 * が付いている欄は必須項目です
コメント 
名前 * 
メールアドレス * 
ウェブサイト 
			関連記事**											[
**【検索結果から消えた】PV数が一気に下がって一気に復活した話**](https://mataku.net/pv-down-up/)						
どもども！性懲りもなく初心者ブロガーをしているマタクです。 今回は面白い（？）ことがPV数に起きたので紹介させていただきます。   面白いう事というのは、PV数の変化。   なんと ... 											[
**functions.phpで失敗しないためのプラグインCode Snippetsが便利過ぎる**](https://mataku.net/codesnippets/)						
こんにちは。wordpressを愛してやまない初心者です。 今回『Code Snippets』という素晴らしいプラグインを発見したので報告までに。   functions.phpを追加できる ... 											[
**Autoptimizeでブログが高速化したけど不具合も付いて来た件**](https://mataku.net/autoptimize%e3%81%a7%e3%83%96%e3%83%ad%e3%82%b0%e3%81%8c%e9%ab%98%e9%80%9f%e5%8c%96%e3%81%97%e3%81%9f%e3%81%91%e3%81%a9%e4%b8%8d%e5%85%b7%e5%90%88%e3%82%82%e4%bb%98%e3%81%84%e3%81%a6%e6%9d%a5%e3%81%9f/)						
どうもこんにちは。相も変わらずwordpressのブログの高速化を模索しています。   なぜそんなに高速化をさせていのか。それは単純にSEO対策を意識して。ということもありますが、実際私自身 ... 											[
**情報商材の「毎月100万稼げる」「大金が儲かる」ネタは本当にできるのか？**](https://mataku.net/jyouhousyouzai-real/)						
Youtuberヒカルさんが情報商材を販売し、っ関わっていたとしてすこぶる情報商材の印象が悪くなっているようですが…   今回はそんな情報商材によくある「この方法で100万円稼げる」「大金が ... 											[
**W3 Total Cache使用で500エラーが出てから復旧までのお話し**](https://mataku.net/w3totalcache500error/)						
  やっと直せた…　こんな思いで現在記事を書いています。   プラグインの不具合の怖さを思い知らされました…（といっても不具合の中でも軽い方だったとは思うが、素人の自分には難解でし ... **PREV**[成績が上がる勉強法](https://mataku.net/have-a-good-record/)**NEXT**[神Wordpressテーマ　ルクセリタスのGoogleアナリティクス設置方法](https://mataku.net/luxeritas-analytics/)						
• [ ] [Youtuber1本で生きていくことは超不安定　おススメできない7つの理由](https://mataku.net/youtuber-only-life/)
• [ ] [情報商材の「毎月100万稼げる」「大金が儲かる」ネタは本当にできるのか？](https://mataku.net/jyouhousyouzai-real/)
• [ ] [神WordPressテーマ　ルクセリタスのGoogleアナリティクス設置方法](https://mataku.net/luxeritas-analytics/)
• [ ] [ネット上でアンケートを取るならWP-PollsよりもDemocracy Pollがよかった](https://mataku.net/democracy-poll/)
• [ ] [成績が上がる勉強法](https://mataku.net/have-a-good-record/)				
• [ ] [2017年9月](https://mataku.net/2017/09/)
• [ ] [2017年8月](https://mataku.net/2017/08/)
• [ ] [2017年6月](https://mataku.net/2017/06/)
• [ ] [2017年5月](https://mataku.net/2017/05/)
• [ ] [2017年4月](https://mataku.net/2017/04/)
• [ ] [2017年3月](https://mataku.net/2017/03/)
• [ ] [2017年1月](https://mataku.net/2017/01/)
• [ ] [2016年11月](https://mataku.net/2016/11/)		
• [ ] [web](https://mataku.net/category/web/)
• [ ] [勉強](https://mataku.net/category/%e7%94%9f%e6%b4%bb/%e5%8b%89%e5%bc%b7/)
• [ ] [生活](https://mataku.net/category/%e7%94%9f%e6%b4%bb/)			
• [ ] [ログイン](https://mataku.net/wp-login.php)
• [ ] [投稿の RSS](https://mataku.net/feed/)
• [ ] [コメントの RSS](https://mataku.net/comments/feed/)
• [ ] [WordPress.org](https://ja.wordpress.org/)																	[**Youtuber1本で生きていくことは超不安定　おススメできない7つの理由**](https://mataku.net/youtuber-only-life/)											[**情報商材の「毎月100万稼げる」「大金が儲かる」ネタは本当にできるのか？**](https://mataku.net/jyouhousyouzai-real/)											[**神WordPressテーマ　ルクセリタスのGoogleアナリティクス設置方法**](https://mataku.net/luxeritas-analytics/)											[**ネット上でアンケートを取るならWP-PollsよりもDemocracy Pollがよかった**](https://mataku.net/democracy-poll/)											[**成績が上がる勉強法**](https://mataku.net/have-a-good-record/)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/urlhttpjisakupc-technical.infoweb-survicewordpress1594.png)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/entry.count.image.png)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/1594.gif)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/httpswww.momosiri.infowp-contentuploads201611wordpress-logo-simplified-rgb.png)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/urlhttpwww.momosiri.infocmswp-polls-ja-error.png)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/entry.count.image.png)

[](https://app.notion.com07fff40b5dd495aca2ac4e1c3fbc60aa)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%201)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%202)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/urlhttpsjvn.jpjpJVN55294532.png)

![](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/entry.count.image.png)

[](https://app.notion.com07fff40b5dd495aca2ac4e1c3fbc60aa)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%203)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%204)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%205)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%206)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%207)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%208)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%209)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%2010)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%2011)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%209)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%2012)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%2013)

[](%E3%83%8D%E3%83%83%E3%83%88%E4%B8%8A%E3%81%A7%E3%82%A2%E3%83%B3%E3%82%B1%E3%83%BC%E3%83%88%E3%82%92%E5%8F%96%E3%82%8B%E3%81%AA%E3%82%89WP-Polls%E3%82%88%E3%82%8A%E3%82%82Democracy%20Poll%E3%81%8C%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F/untitled%2014)

- [ ]  [Yop Poll Archive](https://mataku.net/yop-poll-archive/)
    
    ### [**毎月1000円を10万に変える方法**](https://mataku.net/)
    
    [1年仕事するならブログ書く](https://mataku.net/)
    
    Copyright© 毎月1000円を10万に変える方法 ,  2018 AllRights Reserved Powered by [AFFINGER4](http://manualstinger.com/cr).
    

S