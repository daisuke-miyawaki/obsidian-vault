# 外付けSSDをMacBook ProでWindowsの起動ディスクとし使用する方法

クライアント: SUNNYSH (../DB_%E3%82%AF%E3%83%A9%E3%82%A4%E3%82%A2%E3%83%B3%E3%83%88%E3%83%BB%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9/SUNNYSH%2008d06c9684c3467ba3373ef7768d2323.md)
プロジェクト: SUNNYSH 効率化・便利メモ (../DB_%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88/SUNNYSH%20%E5%8A%B9%E7%8E%87%E5%8C%96%E3%83%BB%E4%BE%BF%E5%88%A9%E3%83%A1%E3%83%A2%20c6ba48251c8c4ce8898844a88a9faebf.md)
テキスト: Macbook proのHDDをSSDにして、WINも入れる
書類制作日付: 2024年7月18日 19:23

外付けSSDをMacBook ProでWindowsの起動ディスクとして使用することは可能ですが、いくつかの手順が必要です。以下はその手順です：

### 必要なもの

- Windows 10またはWindows 11のISOイメージ
- 外付けSSD
- Boot Campアシスタント（macOSに内蔵されています）

### 手順

1. **WindowsのISOイメージを用意する**:
    - Microsoftの公式サイトからWindowsのISOイメージをダウンロードします。
2. **外付けSSDをフォーマットする**:
    - 「ディスクユーティリティ」を開きます。
    - 外付けSSDを選択し、「消去」をクリックします。
    - フォーマット形式を「ExFAT」または「MS-DOS (FAT)」に設定し、消去を実行します。
3. **Boot Campアシスタントを使用する**:
    - 「アプリケーション」フォルダ内の「ユーティリティ」フォルダにある「Boot Campアシスタント」を開きます。
    - 画面の指示に従って、Windowsのインストール用ドライブを作成します。このとき、外付けSSDをインストール先として選択します。
4. **Windowsのインストール**:
    - Boot CampアシスタントがWindowsのインストールを開始します。途中でMacが再起動し、Windowsインストーラが起動します。
    - Windowsのインストールプロセスに従い、外付けSSDをインストール先として選択します。
5. **ドライバーのインストール**:
    - Windowsのインストールが完了したら、Boot Campアシスタントが自動的に必要なドライバーをインストールします。
6. **起動ディスクの選択**:
    - Macを再起動し、起動音が聞こえたらすぐに「Optionキー（⌥）」を押し続けます。
    - 起動ディスク選択画面が表示されたら、外付けSSD上のWindowsを選択して「Enter」を押します。

### 注意点

- **速度**: Thunderbolt 3を使用することで、高速なデータ転送速度が得られますが、内蔵SSDと比較すると若干の速度低下が発生する可能性があります。
- **信頼性**: 外付けSSDを使用する際には、物理的な接続状態に注意してください。特に移動中に外付けSSDが接続された状態で使用する場合、接続が切れるリスクがあります。
- **サポートと保証**: Appleは外付けドライブ上のWindowsインストールに関して公式サポートを提供していないため、自己責任で行う必要があります。

これらの手順に従うことで、外付けSSDを使ってMacBook ProでWindowsを起動することができます。ただし、安定性やパフォーマンスに影響を与える可能性があるため、使用する前に十分にテストすることをお勧めします。

参考サイト

[https://digi-blo.com/computer/mac_book/win-ssd2](https://digi-blo.com/computer/mac_book/win-ssd2)

[https://www.maclab.tokyo/document/bootcamp-windows11-2/5200/](https://www.maclab.tokyo/document/bootcamp-windows11-2/5200/)