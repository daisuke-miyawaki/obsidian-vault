# Contact Form 7 カスタム 住所有

作成日時: 2013年4月28日 18:12
更新されました: 2014年7月9日 12:43
URL: http://hello.lumiere-couleur.com/smilkobuta/2010/12/02/contact-form-7%E3%81%A7%E7%A2%BA%E8%AA%8D%E7%94%A8%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%AE%E5%85%A5%E5%8A%9B%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%82%92%E5%8A%A0/

★メール確認

■functions.phpに下記を追加
<?php
add_filter( 'wpcf7_validate_email', 'wpcf7_text_validation_filter_extend', 11, 2 );
add_filter( 'wpcf7_validate_email*', 'wpcf7_text_validation_filter_extend', 11, 2 );
function wpcf7_text_validation_filter_extend( $result, $tag ) {
    $type = $tag['type'];
    $name = $tag['name'];
    $_POST[$name] = trim( strtr( (string) $_POST[$name], "\n", " " ) );
    if ( 'email' == $type || 'email*' == $type ) {
        if (preg_match('/(.*)_confirm$/', $name, $matches)){
            $target_name = $matches[1];
            if ($_POST[$name] != $_POST[$target_name]) {
                $result['valid'] = false;
                $result['reason'][$name] = '確認用のメールアドレスが一致していません'%3B
            }
        }
    }
    return $result;
}
?>
を追加
■Contact Form 7の設定画面では次のようなフォームを記述
<p>メールアドレス<br />
[email* your-email] </p>
<p>メールアドレス (確認用）<br />
[email* your-email_confirm] </p>

★フォーム

<p>お名前 (必須）<br />

[text* your-name] </p>

<p>ふりがな(必須）<br />

[text* your-ruby] </p>

<p>メールアドレス (必須）<br />

[email* your-email] </p>

<p>TEL(必須）<br />

[text* your-tel]</p>

<p>郵便番号<br />

[text* your-zip]</p>

<p>都道府県(必須）<br />

[select menu-163 "北海道" "青森県" "岩手県" "秋田県" "宮城県" "山形県" "福島県" "群馬県" "栃木県" "茨城県" "埼玉県" "東京都" "千葉県" "神奈川県" "新潟県" "石川県" "富山県" "長野県" "福井県" "岐阜県" "山梨県" "愛知県" "静岡県" "京都府" "滋賀県" "兵庫県" "大阪府" "奈良県" "三重県" "和歌山県" "鳥取県" "島根県" "岡山県" "広島県" "山口県" "香川県" "愛媛県" "徳島県" "高知県" "福岡県" "佐賀県" "長崎県" "大分県" "熊本県" "宮崎県" "鹿児島県" "沖縄県"]</p>

<p>市町村（例：東京都中央区○-○-○）<br />

[text* your-city]</p>

<p>マンション名（例：○○マンション）<br />

[text your-building]</p>

<p>ご相談やメッセージをご記入下さい<br />

[textarea your-message] </p>

<p>[submit "送信"]</p>

★返信メッセージ

差出人: [your-name] <[your-email]>
メッセージ本文:
[your-message]
--
このメールは サンライトシールド㈱ ホームページの資料請求フォームから送信されました
お名前
[your-name]
ふりがな
[your-ruby]
メールアドレス
[your-email]
TEL
[your-tel]
郵便番号
[your-zip]
都道府県
[menu-163]
市町村
[your-city]
マンション名
[your-building]
ご相談やメッセージをご記入下さい
[your-message]