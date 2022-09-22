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

## MicroPython用開発環境Thonnyについて

Raspberry Pi向けのPython開発環境Thonnyは、初心者向けの統合開発環境であり、最新のRaspberry Pi OSに標準でインストールされています。

### インタプリタの選択

ツール＜オプション からインタプリタの設定画面を開く。

- Which kind of interpreter...code?
    - MicroPython(Raspberry Pi Pico)
- ポート
    - USBシリアルデバイス（自身のCOM番号）
- OK

![外観図](./image/img7.png)

### LEDの制御

```python
# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin
#timeライブラリをインポート
from time import sleep

#picoのled(GPIO25を出力ピンに定義)
led = machine.Pin(25, machine.Pin.OUT)

#無限ループ
while True:
    led.value(1) #led点灯
    sleep(1)	 #1min待機
    led.value(0) #led消灯
    sleep(1)
```

### ライブラリのインストール

OLED及びAE-BME280をMicroPythonで開発する際に便利なライブラリがあるのでダウンロードする。

ツール＜パッケージを管理...、`ssd1306`で検索する。
- micropython_ssd1306
    - `https://github.com/stlehmann/micropython-ssd1306`

ツール＜パッケージを管理...、`bme280`で検索する。
- micropython_bme280
    - `https://github.com/stlehmann/micropython-ssd1306`

![外観図](./image/img8.png)

```python
# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep
#ssd1306ライブラリをインポート
import ssd1306

#I2C通信の設定(16pinをsdaに, 17pinをscl)
i2c = I2C(0, sda = Pin(16), scl = Pin(17), freq = 40000)
#OLEDの初期設定
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Rasp Pi Pico",0,0)  #x=0, y=0座標に文字を出力
oled.text("Hello Python",0,20) #x=0, y=20座標に文字を出力

oled.show()		#oledにデータを表示
```