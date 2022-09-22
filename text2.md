# プログラミング技術（Python入門）

## Raspberry　Pi Picoについて

Raspberry Pi財団が独自に開発したARM Cortex M0+デュアルコアのRP2040マイコンを搭載した開発基板です。C/C++およびMicroPythonで開発が可能です。既存のRaspberry Piとは異なりLinux OSは搭載できません。

### [主な特徴](https://www.raspberrypi.com/products/raspberry-pi-pico/)

* Paspberry Pi設計のRP2040マイコン搭載
* USBを介しマスストレージを使ったドラッグアンドドロップによるプログラムの書き込みが可能
* USB 1.1 ホスト/デバイス両対応
* 低消費電力スリープモードおよびドーマントモードが利用可
* C/C++及びPython3ベースの組み込み用MicroPython言語による開発が可能
* 温度センサが搭載

### 仕様

- RP2040（デュアルコア ARM Cortex M0+プロセッサ）
- 最大動作周波数 133 MHz
- SRAM：264KB
- フラッシュメモリ：2MB
- インターフェース
    - GPIO x 26pin
    -  SPI x 2
    - I2C x 2
    - UART x 2
    - 12 bit ADC x 3
    - PWM x 16
    - プログラマブルI/Ox 8

### ピン配置

ピンレイアウトは下図の通りとなる。

![外観図](./image/img6.png)

### [Raspberry Pi Picoの環境構築](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

Rapberry Pi Pico用のUF2ファイルをダウンロードする。（Pico WはWi-Fiモジュール搭載用なので間違わないようにすること。※日本未発売R4.9.22現在）

* BOOTSELボタンを押したまま、PicoをPCのUSB ポートに接続します。Picoが接続されたら、BOOTSELボタンを放します。

* RPI-RP2と呼ばれるマスストレージデバイスとしてマウントされます。

* MicroPython UF2ファイルをRPI-RP2ボリュームにドラッグ＆ドロップします。Picoが再起動します。

