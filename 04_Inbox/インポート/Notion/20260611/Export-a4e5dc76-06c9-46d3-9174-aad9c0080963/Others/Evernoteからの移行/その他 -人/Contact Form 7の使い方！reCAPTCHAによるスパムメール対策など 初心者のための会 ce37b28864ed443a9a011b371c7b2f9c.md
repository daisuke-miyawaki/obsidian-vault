# Contact Form 7の使い方！reCAPTCHAによるスパムメール対策など | 初心者のための会社ホームページ作り方講座｜エックスサーバー株式会社

作成日時: 2023年5月29日 12:56
更新されました: 2023年5月29日 12:57
URL: https://www.xserver.ne.jp/bizhp/wordpress-contact-form-7/

### **reCAPTCHAのAPIキーを取得**

**STEP. 1**

**まずは[reCAPTCHAのホームページ](https://www.google.com/recaptcha/about/)にアクセスし、『Contact Form 7』に接続するための「APIキー（認証コード）」を取得します。**

**画面上部の「v3 Admin Console」をクリックしましょう。**

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-01.png)

**STEP. 2**

**必要事項を入力して、reCAPTCHAの利用登録を済ませます。**

- [ ]  **ラベル：名称を入力（ホームページを複数登録したときに識別するため）**
- [ ]  **reCAPTCHA タイプ：reCAPTCHA v3を選択**
- [ ]  **ドメイン：ドメインを入力（例example.com）**
- [ ]  **オーナー：登録するreCAPTCHAの管理者**
- [ ]  **reCAPTCHA 利用条件に同意する：内容を確認して同意**
- [ ]  **アラートをオーナーに送信する：チェックする（設定エラーや不審なトラフィックなどの通知）**

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-02.png)

**STEP. 3**

**登録すると「サイトキー」「シークレットキー」が表示されるので、それぞれコピーしてメモ帳に貼り付けておきましょう。**

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-03.png)

[**Contact Form 7にAPIキーをセットアップSTEP. 1
WordPressの管理画面に戻り、「お問い合わせ → インテグレーション」をクリックし、セットアップをしていきます。
「reCAPTCHA」のインテグレーションのセットアップをクリックしましょう。STEP. 2
先ほどコピーした「サイトキー」「シークレットキー」を貼り付けて、変更を保存をクリックします。STEP. 3
これで設定は完了です。
ホームページにアクセスし、右下にアイコンが表示されていれば完了です。**](https://www.google.com/recaptcha/about/)

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-04.png)

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-05.png)

![](Contact%20Form%207%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%EF%BC%81reCAPTCHA%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%83%91%E3%83%A0%E3%83%A1%E3%83%BC%E3%83%AB%E5%AF%BE%E7%AD%96%E3%81%AA%E3%81%A9%20%E5%88%9D%E5%BF%83%E8%80%85%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E4%BC%9A/wordpress-contact-form-7-spam-06.png)