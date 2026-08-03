# WordPressの自動整形（ビジュアルエディタ含む）を無効にする方法 - Qiita

タグ: </br>, WordPress, br, html, わーど, ワードの, ワードのの, 改行
作成日時: 2019年3月20日 12:24
更新されました: 2019年3月20日 12:24
URL: https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620

# **WordPressの自動整形（ビジュアルエディタ含む）を無効にする方法**

[WordPress](https://qiita.com/tags/wordpress)

この記事は最終更新日から1年以上が経過しています。

WordPressで既存サイトのテーマ化などを行った際、胃が痛いのがWordPressの自動整形の問題だと思う。

これはWordPress内部に定義されている `wpautop` という関数が行っている処理なのだけど、この関数が結構やっかいで、

- [ ]  改行コードを `<br>` タグに変換
- [ ]  インラインタグまたは文章には `<p>` タグを適用
- [ ]  改行が2回続いたら `<p>` タグを適用

といった処理を自動的に行ってしまうのである。

[wpautop関数](https://wpdocs.osdn.jp/%E9%96%A2%E6%95%B0%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9/wpautop)

通常、ブログ用のテーマを使っているのであれば大きな問題にはならず、逆にタグを正規化してくれるので便利な関数なのだけど、通常のウェブサイトにまでこれが適用されてしまうと、単純に2回改行を入れたいだけなのに `<p>` タグを挿入されてレイアウトが崩れてしまったり、意図しないところに `<p>` タグが紛れ込むことでレイアウトが崩れてしまったりと、割と余計なお世話の関数だったりする。

また、この `wpautop` はビジュアルエディタであるTinyMCEにも組み込まれており、WordPressのエディタを切り替えたタイミングで実行され、やっぱり `<p>` タグや `<br>` タグを自動的に変換してしまうのである。

# [**プラグインを利用して一括回避**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6%E4%B8%80%E6%8B%AC%E5%9B%9E%E9%81%BF)

[これを簡単に回避出来るプラグインが](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6%E4%B8%80%E6%8B%AC%E5%9B%9E%E9%81%BF) [PS Disable Auto Formatting](https://ja.wordpress.org/plugins/ps-disable-auto-formatting/) である。

このプラグインを導入するだけで、ビジュアルエディタ上の変換機能を停止しさらに出力の変換も停止してくれるため、とにかく便利なプラグインだったのだけど・・・

2015年10月13日現在、WordPress 4.3.x 系でWordPress側のエディター切替スクリプトが大幅に修正された影響を受け、このプラグインを導入するとビジュアルエディタとテキストエディタの切替ができなくなってしまう。

そのため、WordPress 4.3.x 系ではこのプラグインを利用することが出来なくなってしまったのである。

# [**プラグインを使わず手動で対応する**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%82%92%E4%BD%BF%E3%82%8F%E3%81%9A%E6%89%8B%E5%8B%95%E3%81%A7%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8B)

[というわけで、プラグインを使わずに手動で対応する方法をまとめてみた。](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%82%92%E4%BD%BF%E3%82%8F%E3%81%9A%E6%89%8B%E5%8B%95%E3%81%A7%E5%AF%BE%E5%BF%9C%E3%81%99%E3%82%8B)

## [**出力側の変換機能を無効化する**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E5%87%BA%E5%8A%9B%E5%81%B4%E3%81%AE%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

[出力の自動変換を回避するためには、`functions.php` に以下のコードを追加する。

`remove_filter( 'the_content', 'wpautop' );`

これで投稿本文においては、上記の `wpautop` による処理がされなくなるため、HTMLがそのまま出力される。
ただ逆に、改行の自動変換も効かなくなってしまうため `<br>` タグが挿入されていないと改行さえ無効になるので注意が必要。](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E5%87%BA%E5%8A%9B%E5%81%B4%E3%81%AE%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

### [**さらに出力側の余計な変換機能を無効化する**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%81%95%E3%82%89%E3%81%AB%E5%87%BA%E5%8A%9B%E5%81%B4%E3%81%AE%E4%BD%99%E8%A8%88%E3%81%AA%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

[WordPressの出力関数にはさらにフィルターが組み込まれていて、特定の記号のならびを別の文字に変換したり、ダブルクォートやシングルクォートを実体参照に変換したりしている。](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%81%95%E3%82%89%E3%81%AB%E5%87%BA%E5%8A%9B%E5%81%B4%E3%81%AE%E4%BD%99%E8%A8%88%E3%81%AA%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

[wptexturize関数](https://wpdocs.osdn.jp/%E9%96%A2%E6%95%B0%E3%83%AA%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9/wptexturize)

これが便利なようで逆に不便で、たとえばコード中のHTMLコメントなんかも変換されてしまい、レイアウトが崩れたりしてしまう。

というわけで、以下のコードを用いてこのフィルターを解除しておくことで、さらにHTMLコードを忠実に出力することが出来る。

`remove_filter( 'the_content', 'wptexturize' );`

## [**ビジュアルエディタの変換機能を無効化する**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%81%AE%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

[ビジュアルエディタ側の対応もそこまで難しくない。
`functions.php` に以下のコードを追加することで簡単に回避できる。

`function override_mce_options( $init_array ) {
    $init_array['indent']  = true;
    $init_array['wpautop'] = false;

    return $init_array;
}

add_filter( 'tiny_mce_before_init', 'override_mce_options' );`](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%81%AE%E5%A4%89%E6%8F%9B%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

### [**さらにビジュアルエディタの余計な機能を無効化する**](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%81%95%E3%82%89%E3%81%AB%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%81%AE%E4%BD%99%E8%A8%88%E3%81%AA%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)

[ついでにビジュアルエディタに備わっている余計なフィルターを無効化することで、さらに便利に利用することができる。
先ほどのコードを以下のように修正。

`function override_mce_options( $init_array ) {
    global $allowedposttags;

    $init_array['valid_elements']          = '*[*]';
    $init_array['extended_valid_elements'] = '*[*]';
    $init_array['valid_children']          = '+a[' . implode( '|', array_keys( $allowedposttags ) ) . ']';
    $init_array['indent']                  = true;
    $init_array['wpautop']                 = false;
    $init_array['force_p_newlines']        = false;

    return $init_array;
}

add_filter( 'tiny_mce_before_init', 'override_mce_options' );`

上記のコードは以下のようなことをしている。
• [ ] 全てのタグ・全ての属性を許可（空の `<span>` タグや `<div>` タグなどが削除されるのを防ぐ）
• [ ] `<a>` タグに全てのタグを入れられるようにする
• [ ] 自動的に `<p>` タグで囲われることを防ぐ
これでビジュアルエディターを使ったときにも、タグが無くなったり変換されてしまうことを最小限に抑えられると思う。](https://qiita.com/jyokyoku/items/c560b0d1eacc1df61620#%E3%81%95%E3%82%89%E3%81%AB%E3%83%93%E3%82%B8%E3%83%A5%E3%82%A2%E3%83%AB%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%81%AE%E4%BD%99%E8%A8%88%E3%81%AA%E6%A9%9F%E8%83%BD%E3%82%92%E7%84%A1%E5%8A%B9%E5%8C%96%E3%81%99%E3%82%8B)