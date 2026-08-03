# Google reCAPTCHAの設置、V2化、デザイン修正

クライアント: 海のサロン空 (../DB_%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%E3%83%BB%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9/%E6%B5%B7%E3%81%AE%E3%82%B5%E3%83%AD%E3%83%B3%E7%A9%BA%20cac1b30910c34287934a1c33094eb8d8.md)
プロジェクト: ザキヤマ　予約フォームスパムメール防止 (../DB_%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88/%E3%82%B6%E3%82%AD%E3%83%A4%E3%83%9E%20%E4%BA%88%E7%B4%84%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E9%98%B2%E6%AD%A2%20851925551c1a470bbef1270817b2fd67.md)
タグ: HP, WP, work notes, 学び
Category: work notes
重要度: ★
書類制作日付: 2024年8月14日 18:58

## reCAPTCHAの利用は、伊藤事務所ですでにやっていたので、追加し、サロン空さんでも利用

ChatGPTのお陰で、結構簡単だった、

## Contact Form 7が、 reCAPTCHA v2に対応していないことで、拡張プラグインで対応可に！

「Contact Form 7 - reCAPTCHA v2」プラグインは、以下のリンクからダウンロードできます。このプラグインを使用することで、Contact Form 7でreCAPTCHA v2を再び使用できるようになります。

[ReCaptcha v2 for Contact Form 7 - WordPress.org](https://wordpress.org/plugins/wpcf7-recaptcha/)【56†source】

# reCAPTCHA v2 設置詳細

### 1. **Google reCAPTCHA APIキーの取得**

まず、Google reCAPTCHAの管理画面でv2のAPIキーを取得します。すでに取得している場合は次のステップに進んでください。

1. Google reCAPTCHA管理画面にアクセス。
2. 「新しいサイトを登録」ページで、reCAPTCHAのバージョン「v2 チャレンジ」を選択。
3. ドメイン名を入力し、「登録」ボタンを押してサイトキーとシークレットキーを取得します。

### 2. **Contact Form 7の設定**

次に、Contact Form 7の設定に進みます。

1. **WordPress管理画面**にログイン。
2. サイドバーから **「Contact」→「インテグレーション」** の順にクリックします。
3. 「Google reCAPTCHA」の項目を見つけて、**「インテグレーションのセットアップ」** をクリックします。
4. 先ほど取得した「サイトキー」と「シークレットキー」をそれぞれ入力し、保存します。

### 3. **フォームにreCAPTCHAを追加**

次に、実際のフォームにreCAPTCHA v2を設置します。

1. **「Contact」→「コンタクトフォーム」** に移動します。
2. フォームを編集し、以下のようなreCAPTCHAのショートコードを追加します：
※設置コード詳細は下の方に例あり
    
    ```html
    [recaptcha]
    ```
    
3. このショートコードをフォームの適切な場所に挿入します。通常は送信ボタンの直前に追加するのが一般的です。

---

## チェックと、送信ボタンとの間隔の修正例

```jsx

<label>
 メッセージ<br />
  <textarea name="your-message"></textarea>
</label><br />
<br />
<div style="margin-bottom: 20px;">
    [recaptcha]
</div>
<input type="submit" value="送信する">
```