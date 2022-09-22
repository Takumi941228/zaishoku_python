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