# ワンポイントに使えるCSS3マウスオーバーアニメーション5種 | webOpixel

タグ: css, アニメーション, ボタン, 動き
作成日時: 2019年1月26日 16:42
更新されました: 2019年1月26日 16:42
URL: http://www.webopixel.net/html-css/831.html

# ワンポイントに使えるCSS3マウスオーバーアニメーション5種

![](%E3%83%AF%E3%83%B3%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%81%AB%E4%BD%BF%E3%81%88%E3%82%8BCSS3%E3%83%9E%E3%82%A6%E3%82%B9%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B35%E7%A8%AE%20webOpixel/1030s.png)

Posted: 2013.10.30 / Category: [HTML&CSS](https://www.webopixel.net/category/html-css) / Tag: [CSS3](https://www.webopixel.net/tag/css3)

ちょっとしたワンポイントに使えそうなCSS3オンリーのマウスオーバーアニメーションです。

IEは10以上で動きます。

**Sponsored Link**
                 
                
                
                
            
**ベースHTML**
ベースのHTMLです。っていっても基本aタグだけです。
html[?](http://www.webopixel.net/html-css/831.html#)12`<a` `href="#"` `class="btn01">BUTTON</a>`
**1.くるくるって回るアニメーション**

        くるくるっと２回転するアニメです。

        くるっと１回転の場合は「rotate」を360にすればOKです。
	
css[?](http://www.webopixel.net/html-css/831.html#)123456789101112131415161718`.btn01` `{    color: #fff;    text-decoration: none;    background-color: #dda0dd;    display: block;    width: 150px;    height: 150px;    line-height: 150px;    border-radius: 50%;    /* ここで動く速度とか設定 */    transition: all` `1s ease;    -webkit-transition: all` `1s ease;}.btn01:hover {    transform: rotate(720deg);    -webkit-transform: rotate(720deg);}`

        デザインてきな処理で長くなってますけど、動き自体は「transition」とhoverの「transform」です。

        最近のFirefoxとかIEではベンダープレフィクスいらないけど、ChromeとかWebkit系列ではまだまだ必要なようです。

        ちなみに「border-radius: 50%;」でまん丸にできます。
    
**2.ぶるぶるぶるって振動する**
ぶるぶるぶるぶるぶるぶるです。
css[?](http://www.webopixel.net/html-css/831.html#)1234567891011121314151617181920212223242526`.btn02` `{    color: #fff;    display: block;    text-decoration: none;    background-color: #dda0dd;    width: 150px;    padding: 30px` `0;}.btn02:hover {    animation: shake 0.2s linear infinite;    -webkit-animation: shake 0.2s linear infinite;}@keyframes shake {    0%` `{ transform: translate(3px, 2px) rotate(0deg); }    10%` `{ transform: translate(-2px, -3px) rotate(-1deg); }    20%` `{ transform: translate(-4px, 0px) rotate(1deg); }    30%` `{ transform: translate(0px, 3px) rotate(0deg); }    40%` `{ transform: translate(2px, -2px) rotate(1deg); }    50%` `{ transform: translate(-2px, 3px) rotate(-1deg); }    60%` `{ transform: translate(-4px, 2px) rotate(0deg); }    70%` `{ transform: translate(3px, 2px) rotate(-1deg); }    80%` `{ transform: translate(-2px, -2px) rotate(1deg); }    90%` `{ transform: translate(2px, 4px) rotate(0deg); }    100%` `{ transform: translate(2px, -3px) rotate(-1deg); }}`

        Webkitに対応するには「@-webkit-keyframes」も同じように作ってください。

        「animation」の4つ目を「infinite」にすることで永久に動き続けます。

        揺れがあまい！　って人は「@keyframes」の値を大きくしてやるといいです。
    
**3.アイコンが拡大する**

        設定したアイコン（背景画像）を拡大させてみます。

        拡大するだけじゃつまらないので全体的に動かしたりもしてみました。
    
テキストも動かしたかったので、spanを挟んでます。
html[?](http://www.webopixel.net/html-css/831.html#)12`<a` `href="#"` `class="btn03"><span>BUTTON 03</span></a>`
css[?](http://www.webopixel.net/html-css/831.html#)12345678910111213141516171819202122232425262728293031323334353637383940414243`.btn03` `{    color: #fff;    text-decoration: none;    background: #9EB8F3;    width: 280px;    padding: 30px` `20px;    position: relative;    overflow: hidden;    text-align: center;    display: block;    -webkit-transition: all` `0.3s ease;    transition: all` `0.3s ease;}.btn03:hover {    background-size: 100px` `100px;    background-position: right` `50%;    background-color: #799CEE;}.btn03::before {    content: "";    width: 100%;    height: 100%;    position: absolute;    top: 0;    left: 30px;    background: url("img/icon.png") no-repeat` `0` `50%;    background-size: 38px` `38px;    -webkit-transition: all` `0.3s ease;    transition: all` `0.3s ease;}.btn03:hover::before {    left: 240px;    background-size: 80px` `80px;` `}.btn03` `span {    -webkit-transition: all` `0.3s ease;    transition: all` `0.3s ease;` `}.btn03:hover span {    margin-left: -180px;}`

        アイコンの付け方は色々あると思いますが、ここでは「::before」の「background」で設定してます。

        最近だとwebfontを使用した方がスマートかもしれないですね。

        あとは「background-size」を大きくするだけですね。
    
**4.枠線のアニメーション**
枠線を拡大したりするアニメーション。
css[?](http://www.webopixel.net/html-css/831.html#)12345678910111213141516171819202122232425262728293031323334`.btn04` `{    color: #fff;    text-decoration: none;    text-align: center;    position: relative;    z-index: 10;    display: block;    width: 150px;    height: 150px;    line-height: 150px;}` `.btn04::before {    content: '';    background-color: #dda284;    display: block;    position: absolute;    width: 150px;    height: 150px;    z-index: -1;    border-radius: 50%;    box-shadow:        0` `0` `0` `0` `#fff,        0` `0` `0` `0` `#dda284;    transition: all` `.2s ease;    -webkit-transition: all` `.2s ease;}.btn04:hover::before {    transform: scale(0.8);    -webkit-transform: scale(0.8);    box-shadow:        0` `0` `0` `25px` `#fff,        0` `0` `0` `27px` `#dda284;}`
「border」のオフセットとかはないっぽいので、「box-shadow」で擬似的に枠線っぽくします。
**5.くるっと奥に１回転**
3D的にz軸に１回転でアニメーションします。
IEだとあまりいい動きしません。
html[?](http://www.webopixel.net/html-css/831.html#)12345`<a` `href="#"` `class="btn05">    <span` `class="front">BUTTON</span>    <span` `class="back">BUTTON</span></a>`
css[?](http://www.webopixel.net/html-css/831.html#)1234567891011121314151617181920212223242526272829303132333435363738`.btn05` `{    color: #fff;    display: block;    text-decoration: none;    width: 200px;    position: relative;    perspective: 300px;    -webkit-perspective: 300px;}` `.btn05` `span {    text-align: center;    display: block;    width: 200px;    padding: 30px` `0;    background-color: #a7dd7d;    position:absolute;    top: 0;    margin-top: -30px;    backface-visibility: hidden;    -webkit-backface-visibility: hidden;    transition: 0.8s;}.btn05` `.back {    background-color: #61a84d;    transform:rotateY(180deg);    -webkit-transform:rotateY(180deg);}` `.btn05:hover .front {    transform:rotateY(180deg);    -webkit-transform:rotateY(180deg);}` `.btn05:hover .back {    transform:rotateY(360deg);    -webkit-transform:rotateY(360deg);}`
keyframesを使えばもっと表現が増えそうな気がしますが、マウスアウトの処理はJSを使用しないと上手くいかない気がします。どうなんすかね。 
    
     
      
    [**138**](http://b.hatena.ne.jp/entry/www.webopixel.net/html-css/831.html)

    
     [***ツイート**](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fwww.webopixel.net%2Fhtml-css%2F831.html&ref_src=twsrc%5Etfw&text=%E3%83%AF%E3%83%B3%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%81%AB%E4%BD%BF%E3%81%88%E3%82%8BCSS3%E3%83%9E%E3%82%A6%E3%82%B9%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B35%E7%A8%AE%20%7C%20webOpixel&tw_p=tweetbutton&url=http%3A%2F%2Fwww.webopixel.net%2Fhtml-css%2F831.html)*

    
     
        
          

    
     
        
     
                    
                    
                    
                
                    
                    
                    
                    
                

![](%E3%83%AF%E3%83%B3%E3%83%9D%E3%82%A4%E3%83%B3%E3%83%88%E3%81%AB%E4%BD%BF%E3%81%88%E3%82%8BCSS3%E3%83%9E%E3%82%A6%E3%82%B9%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B35%E7%A8%AE%20webOpixel/demo_btn.gif)

[](data:image/svg+xml,%3csvg version='1.1' xmlns='http://www.w3.org/2000/svg' preserveAspectRatio='xMidYMid meet' width='48px' height='18px' viewBox='-28 -6 96 36' class='ozWidgetRioButtonSvg_ ozWidgetRioButtonPlusOne_ js-evernote-checked' data-evernote-id='2'%3e%3cpath d='M30 7h-3v4h-4v3h4v4h3v-4h4v-3h-4V7z'%3e%3c/path%3e%3cpath d='M11 9.9v4h5.4C16 16.3 14 18 11 18c-3.3 0-5.9-2.8-5.9-6S7.7 6 11 6c1.5 0 2.8.5 3.8 1.5l2.9-2.9C15.9 3 13.7 2 11 2 5.5 2 1 6.5 1 12s4.5 10 10 10c5.8 0 9.6-4.1 9.6-9.8 0-.7-.1-1.5-.2-2.2H11z'%3e%3c/path%3e%3c/svg%3e)