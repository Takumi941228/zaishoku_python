# プログラミング技術（Python入門）

こちらのテキストは、県央産業技術専門校セミナー「プログラミング技術（Python入門）」で使用するテキストです。

## 研修項目

* Pythonの概要
* Pythonの学習
* Raspberry Pi Picoを使ったMicroPythonの学習
* Pythonを使ったグラフによる可視化

## 研修内容

### Pythonの概要
Pythonについて、概要など知識の学習を行います。

### Pythonの学習
初心者向けのPython開発環境Jupyter NoteBookを使って、Pythonの基本的な書き方からライブラリを使った応用的な内容まで、学習します。

### Raspberry Pi Picoを使ったPythonの学習
Raspberry Pi Picoを使って、Python3と互換性がある言語MicroPythonで、マイコンを使ったLEDの制御や液晶ディスプレイ`[SSD1306]`と温湿度・気圧センサ`[AE-BME280]`の制御方法、センサデータ取得をシリアル通信で行うなどの、組み込み向けのPythonを使い方を学習します。

### Pythonでグラフによる可視化
Rapberry Pi Picoに接続された温湿度・気圧センサ`[AE-BME280]`で計測したデータをシリアル通信で送信し、PCで受信したデータをPythonを用いてcsvデータとして保存し、以下のようなグラフを作成し、可視化を行います。

![外観図](./image/Figure_1.png)

左上の赤色のグラフが温度値、右上の青色のグラフが気圧値、左下の緑色のグラフが湿度値となっています。右下のグラフは、温度値と湿度値を同時に描画したものです。

## 基本セット

本セミナーにおいて使用するものは以下とし、ハードウェアとソフトウェアに分けて記述します。

## 利用ハードウェア

使用するハードウェアの紹介をします。

* マイコンボード（Raspberry Pi Pico）

    * <https://akizukidenshi.com/catalog/g/gM-16132/>

* 温湿度・気圧センサ（AE-BME280）

    * <https://akizukidenshi.com/catalog/g/gK-09421/>

* 有機ELディスプレイ（SSD1306）

    * <https://akizukidenshi.com/catalog/g/gP-12031/>

* ブレッドボード （BB-801）

    * <https://akizukidenshi.com/catalog/g/gP-05294/>

* ブレッドボード・ジャンパーワイヤ

    * <https://akizukidenshi.com/catalog/g/gC-05371/>

## 利用ソフトウェア

使用するソフトウェアを紹介します。

* Jupyter NoteBook（Anaconda3）

    * <https://www.anaconda.com/products/distribution>

* Visual Studio Code

    * <https://code.visualstudio.com/download>

* Thonny

    * <https://thonny.org/>

## 開発言語

今回使用する言語はPythonで、Pythonは3系をインストールします。

* Python3系

    * <https://www.python.org/>

* MicroPython
    * <https://micropython.org/>

Thank you!
