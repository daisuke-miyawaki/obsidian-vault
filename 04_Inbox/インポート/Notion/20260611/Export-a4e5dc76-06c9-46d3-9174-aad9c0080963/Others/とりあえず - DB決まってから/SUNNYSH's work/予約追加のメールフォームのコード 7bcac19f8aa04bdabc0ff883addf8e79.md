# 予約追加のメールフォームのコード

<label>お名前（必須）<br />
[text* your-name]</label><br />

<label>電話番号（必須）<br />
[tel* tel-123]</label><br />

<label>メールアドレス（必須）<br />
[email* your-email]</label><br />

<label>メールアドレス確認<br />
[email* your-email_confirm placeholder "確認のためもう一度入力してください"]</label><br />

<label>予約希望日時<br />
<p>予約ご希望の場合はご希望の日をご入力ください。</p>

<label>第一希望</label><br />
[date reservation-date-first max:today+8year class:form-control]

<label>第二希望</label><br />
[date reservation-date-second max:today+8year class:form-control]</label><br />

<label>メッセージ<br />
[textarea your-message]</label><br />

[acceptance acceptance-0] 確認ページはございません。内容をご確認の上チェックを入れてください<br />

[submit "送信する"]

予約希望日時：
第一希望：[your-date-first]
第二希望：[your-date-second]