# pico_micropython1.py
# -*- coding: utf-8-*-
#pico用machineライブラリのPinをインポート
from machine import Pin
#timeライブラリのsleepをインポート
from time import sleep

#picoのled(GPIO25を出力ピンに定義)
led = machine.Pin(25, machine.Pin.OUT)

#無限ループ
while True:
    led.value(1) #led点灯
    sleep(1)	 #1sec待機
    led.value(0) #led消灯
    sleep(1)     #1sec待機