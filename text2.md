# プログラミング技術（Python入門）

## Raspberry Pi Picoについて

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

ピンレイアウトは下図の通りとなります。

![外観図](./image/img6.png)

### [Raspberry Pi Picoの環境構築](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

以下のアドレスからRapberry Pi Pico用のUF2ファイルをダウンロードします。（Pico WはWi-Fiモジュール搭載用なので間違わないようにします。※日本未発売R4.9.22現在）

* <https://www.raspberrypi.com/documentation/microcontrollers/micropython.html>

* `BOOTSELボタン`を押したまま、PicoをPCのUSB ポートに接続します。Picoが接続されたら、`BOOTSELボタン`を放します。

* `RPI-RP2`と呼ばれるマスストレージデバイスとしてマウントされます。

![外観図](./image/img21.png)

* MicroPython UF2ファイルをRPI-RP2ボリュームに`ドラッグ＆ドロップ`します。Picoが再起動します。

### 配線

配線図は以下の図及び表にならって、配線します。

![外観図](./image/img14.png)

| Pico | pin| SSD1306 | BME280 |
| --- | --- | --- | --- |
| 3V3(OUT) | 36 | VCC | VDD |
| GND | 23 | GND | GND |
| SCL | 22 | SCL | SCK |
| SDA | 21 | SDA | SDI |
| 3V3(OUT) | 36 | --- | CSB |
| GND | 23 | --- | SDO |


## MicroPython用開発環境Thonnyについて

Raspberry Pi向けのPython開発環境Thonnyは、初心者向けの統合開発環境であり、最新のRaspberry Pi OSに標準でインストールされています。

### MicroPythonとは

マイクロコンピュータや組み込み機器で使われるプログラミング言語はC/C++が一般的ですが、初心者にとっては学習障壁が比較的高い言語でもあります。`「MicroPython」`はPython3と高い互換性があるプログラミング言語であるため、プログラミング初心者でも理解しやすいPythonの文法を使ってプログラミングすることができます。

* MicroPython - Python for microcontrollers
    * <http://micropython.org/>


### インタプリタの選択

ツール＜オプション からインタプリタの設定画面を開きます。

- Which kind of interpreter...code?
    - MicroPython(Raspberry Pi Pico)
- ポート
    - USBシリアルデバイス（自身のCOM番号）
- OK

![外観図](./image/img23.png)

## サンプルプログラム

いくつかのサンプルプログラムを実行し、Picoと各種センサについて学習します。

タブから`ファイル`＞`ファイルを開く`
* where are to open from?
    * `このコンピュータ`を選択

`C:\Users\user\Desktop\zaishoku_python\Pico_Python\pico_micropython1.py`を開きます。

### LEDの制御

Raspberry Pi Picoに内蔵されているLED（`GPIO25pin`）を使用して、Lチカを行います。

* ファイル名（pico_micropython1.py）
```python
# pico_micropython1.py
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
    sleep(1)	 #1sec待機
    led.value(0) #led消灯
    sleep(1)     #isec待機
```

プログラムの実行をするには、`緑色のアイコン`をクリックします。止めるときは、`STOP`のアイコンです。

![外観図](./image/img28.png)

### ライブラリのインストール

`SSD1306`及び`AE-BME280`をMicroPythonで開発する際に便利なライブラリがあるのでダウンロードします。

ツール＜パッケージを管理...、`ssd1306`で検索する。
- micropython_ssd1306
    - `https://github.com/stlehmann/micropython-ssd1306`

ツール＜パッケージを管理...、`bme280`で検索する。
- micropython_bme280
    - `https://github.com/stlehmann/micropython-ssd1306`

ライブラリがインストールされると以下のようにインストール項目に追加されます。

![外観図](./image/img22.png)

### OLEDの表示

有機ELディスプレイ（OLED）をPicoにI2C接続を行い、文字を表示します。

* ファイル名（pico_micropython2.py）

```python
# -*- coding: utf-8-*-
# pico_micropython2.py
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep
#ssd1306ライブラリをインポート
import ssd1306

#I2C通信の設定(16pinをsda, 17pinをscl）
i2c = I2C(0, sda = Pin(16), scl = Pin(17))

#OLEDの初期設定（解像度128x64, i2c通信を選択）
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Rasp Pi Pico",0,0)  #x=0, y=0座標に文字を出力
oled.text("Hello Python",0,20) #x=0, y=20座標に文字を出力

oled.show() #oledにデータを表示
```

### BME280センサデータの取得

BME280センサをPicoにI2C接続を行いデータを取得する

* ファイル名（pico_micropython3.py）

```python
# -*- coding: utf-8-*-
# pico_micropython3.py
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep
#bme280ライブラリをインポート
from bme280 import BME280

import math

#I2C通信の設定(16pinをsda, 17pinをscl)
i2c = I2C(0, sda = Pin(16), scl = Pin(17))
#BME280の初期設定
bme = BME280(i2c = i2c)

'''
bme280センサの計測を行う関数
'''
def sensor():
    #温度・湿度・気圧データを取得し、それぞれに格納
    temp, press, humi = bme.read_compensated_data()
    #温度,湿度,気圧のデータを計算
    temp = float(temp / 100)
    press = float((press // 256) / 100)
    humi = float(humi / 1024)
    #文字型に変換してlist型dataに格納
    #humiを小数点以下第二位で四捨五入
    data = str(temp) + ',' + str(press) + ',' + str(round(humi, 2))
    #計測したデータを戻り値として返す
    return data, temp, press, humi

while True:
    #sensor関数を呼び出し、戻り値をdata,temp,press,humiに格納
    data, temp, press, humi = sensor()
    
    print(data)  #シリアル通信にてデータ送信
    sleep(1)     #1msec待機
```

正しく接続ができていれば、以下のようなセンサデータがshell画面に1秒間隔で表示されます。

![外観図](./image/img9.png)

## Raspberry Pi Picoからシリアル通信でPCに送信する

温湿度・気圧のデータを1分間隔で、シリアル通信にて、PCに送るプログラムになっています。以下のプログラムを実行した後、`Thonny`を終了してください。※shellにデータを表示する際に、シリアル通信を行っているため、PCへのシリアル通信と競合してしまうのを防ぐためです。

```python
# -*- coding: utf-8-*-
#pico用ライブラリをインポート
from machine import Pin, I2C
#timeライブラリをインポート
from time import sleep
#bme280ライブラリをインポート
from bme280 import BME280
#ssd1306ライブラリをインポート
import ssd1306

#picoのled(GPIO25を出力ピンに定義)
led = machine.Pin(25, machine.Pin.OUT)
#I2C通信の設定(16pinをsda, 17pinをscl)
i2c = I2C(0, sda = Pin(16), scl = Pin(17))
#bme280の初期設定
bme = BME280(i2c = i2c)
#ssd1306の初期設定
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

'''
bme280センサの計測を行う関数
'''
def sensor():
    temp, press, humi = bme.read_compensated_data()
    #温度,湿度,気圧のデータを計算
    temp = float(temp / 100)
    press = float((press // 256) / 100)
    humi = float(humi / 1024)
    #文字型に変換してlist型dataに格納
    #humiを小数点以下第二位で四捨五入
    data = str(temp) + ',' + str(press) + ',' + str(round(humi, 2))
    #計測したデータを戻り値として返す
    return data, temp, press, humi

while True:
    #sensor関数を呼び出し、戻り値をdata,temp,press,humiに格納
    data, temp, press, humi = sensor()
    
    oled.fill(0)  #oledの表示を削除
    oled.text("Rasp Pi Pico",0,0)  
    oled.text("Temp:       'C",0,10)
    oled.text(str(temp),48,10)
    oled.text("Press:      hP",0,20)
    oled.text(str(press),48,20)
    oled.text("Humi:         %",0,30)
    oled.text(str(humi),48,30)
    oled.show()   #oledにデータを表示
    
    led.value(1) #led点灯
    print(data)  #シリアル通信にてデータ送信
    sleep(60)    #1min待機
    led.value(0) #led消灯
```
