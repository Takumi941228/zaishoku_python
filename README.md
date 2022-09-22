# プログラミング技術（Python入門）

こちらのテキストは、県央産業技術専門セミナー「プログラミング技術（Python入門）」で使用するテキストです。

## 研修内容

* Pythonの概要
* Pythonの学習（Jupyter NoteBook）
* Raspberry Pi Picoを使ったセンサデータ収集（Thonny）
* Pythonを使ったグラフによる可視化（Vitual Studio Code）

## 実施内容

Rapberry Pi Picoに接続された温湿度・気圧センサ(AE-BME280)で計測したデータをシリアル通信にて送信し、PCで受信したデータをPythonを用いてcsvデータとして保存し、以下のようなグラフにする。

![外観図](./image/Figure_1.png)

赤色のグラフが温度、青色が気圧、緑色が湿度となっている。

## 基本セット

本セミナーにて使用するものは以下とする。

## 利用ハードウェア

使用すハードウェアの紹介をします。

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

* Jupyter NoteBook（Anaconda3）

    * <https://www.anaconda.com/products/distribution>

* Visual Studio Code

    * <https://code.visualstudio.com/download>

* Thonny

    * <https://thonny.org/>

## 開発言語

* Python3系

    * <https://www.python.org/>

* MicroPython
    * <https://micropython.org/>
