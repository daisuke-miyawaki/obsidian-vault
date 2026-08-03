# レスポンシブル　CSS レイアウト　回りこみ isotype

作成日時: 2016年1月19日 15:48
更新されました: 2018年2月22日 13:21

PCではいいが、スマホでの表示で、画像などが、下に移動しない場合。

cssファイルを直接編集する必要がありますが、

.entry img {

float:nonel

}

Powered by. [isotope](http://isotype.blue/).の場合、

responcive.css　　 705行目あたりに、

---

ザキヤマ　フッターがコンテンツ部分に入ってしまう

---

> このサイトでWPの更新をすると、コンテンツ部分の色が、

> フッターで指定した色に変わってしまい、

> [http://resetinnovation.com/category/%E3%81%8A%E5%BD%B9%E7%AB%8B%E3%81%A1%E6%83](http://resetinnovation.com/category/%E3%81%8A%E5%BD%B9%E7%AB%8B%E3%81%A1%E6%83)> %85%E5%A0%B1/

> や

> [http://resetinnovation.com/category/%E3%81%8A%E5%AE%A2%E6%A7%98%E3%81%AE%E5%A3](http://resetinnovation.com/category/%E3%81%8A%E5%AE%A2%E6%A7%98%E3%81%AE%E5%A3)> %B0-2/

> など、投稿記事の一覧ページへのページ送りができない状態です。

> （１ページ目は見られますが、２ページ目以降のボタンを押しても移動できません）

この症状については、フッターが、メインコンテンツに食い込んでしまっているようなので、[テーマオプション]-[カスタムcss]に下記を記述することで、回避できると思います。

footer{

clear:both;

}