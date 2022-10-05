# -*- coding: utf-8-*-
# pico_micropython2.py
#pico用ライブラリのPin1とI2Cをインポート
from machine import Pin, I2C
#timeライブラリのsleepをインポート
from time import sleep
#ssd1306ライブラリをインポート
import ssd1306

#I2C通信の設定(id(I2C0 SCL(GPIO16=21pin))と(I2C0 SDA(GPIO17=22pin))=0), 16pinをsda, 17pinをscl）
i2c = I2C(0, sda = Pin(16), scl = Pin(17))

#OLEDの初期設定（OLED画面解像度128x64, i2c通信を選択）
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Rasp Pi Pico",0,0)  #x=0, y=0座標に文字を出力
oled.text("Hello Python",0,20) #x=0, y=20座標に文字を出力

oled.show()		#oledにデータを表示