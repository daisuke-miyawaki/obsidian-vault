# ウィジェットのH3をH4にするには

作成日時: 2012年2月11日 15:55
更新されました: 2012年2月11日 16:37
URL: http://the-fool.me/wordpress/customize/widget-h2-h3.html

| 2.2既定のfunctions.php
<?php
if ( function_exists('register_sidebar') )
register_sidebar(array(
'before_widget' => '<li id="%1$s" class="widget %2$s">',
'after_widget' =>'</li>',
'before_title' => '<h2>',
'after_title' => '</h2>',
));
?>
３カラムの左右に１個づつ、２個のウィジェットを使うには function.php のregister_sidebar を　register_sidebars （複数！）にして、カッコの中にウィジェットの数を指定する。
<?php
if ( function_exists('register_sidebar') )
register_sidebars(2);
?>
これで管理画面の表示　ウィジェット画面に　２個のウィジェットが現れる。
sidebar.php をもう一つつくる。
標準の sidebar.php をベースに　左右のウィジェットを呼び出す sidebar1.php と sidebar2.php を作る。各phpの先頭に対応するウィジェットの番号を設定する。
<?php /* Widgetized sidebar, if you have the plugin installed. */
if ( !function_exists('dynamic_sidebar') || !dynamic_sidebar(2) ) : ?>
上は ２個目のウィジェットを対応させた例。
標準の sidebar.php を　dynamic_sidebar(1) として、新規のサイドバーを dynamic_sidebar(2) としても良いが、 get_sidebar() では sidebar.php しか呼び出せない。
get_sidebar も使わないことにして　sidebar1.php sidebar2.php を　<?php include(TEMPLATEPATH.'/sidebar2.php'); ?>で呼んだ方が後々理解しやすいかもしれない。
ウィジェットはメニュのタイトルとして　h2 を返している。expssのスタイルとしては、h1でページタイトル、h2でページ説明、h3で記事やメニュのタイトル　という使い方をしているので、ウィジェットの h2 は具合が悪い。functions.php　で ウィジェットタイトルとして　h3 を返すように手を加える。
<?php
if ( function_exists('register_sidebar') ) {
register_sidebars(2);
register_sidebar(array(1,
'before_widget' => '<li id="%1$s" class="widget %2$s">',
'after_widget' =>'</li>',
'before_title' => '<h3>',
'after_title' => '</h3>',
));register_sidebar(array(2,
'before_widget' => '<li id="%1$s" class="widget %2$s">',
'after_widget' =>'</li>',
'before_title' => '<h2>',
'after_title' => '</h2>',
));
}
?> |
| --- |