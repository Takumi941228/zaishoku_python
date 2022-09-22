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