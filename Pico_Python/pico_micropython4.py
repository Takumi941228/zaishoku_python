# -*- coding: utf-8-*-
#pico用ライブラリPinとI2Cをインポート
from machine import Pin, I2C
#timeライブラリsleepをインポート
from time import sleep
#bme280ライブラリBME280をインポート
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
    #センサデータを取得
    temp, press, humi = bme.read_compensated_data()
    #温度,湿度,気圧のデータを計算
    temp = float(temp / 100)
    press = float((press // 256) / 100)
    humi = float(humi / 1024)
    #文字型に変換してdataに格納
    #humiを小数点以下第二位で四捨五入
    data = str(temp) + ',' + str(press) + ',' + str(round(humi, 2))
    #計測したデータを戻り値として返す
    return data, temp, press, humi

while True:
    #sensor関数を呼び出し、戻り値をdata,temp,press,humiに格納
    data, temp, press, humi = sensor()
    
    #oledにセンサデータを表示
    oled.fill(0)	#oledの表示を削除
    oled.text("Rasp Pi Pico",0,0)  
    oled.text("Temp:       'C",0,10)
    oled.text(str(temp),48,10)
    oled.text("Press:      hP",0,20)
    oled.text(str(press),48,20)
    oled.text("Humi:         %",0,30)
    oled.text(str(humi),48,30)
    oled.show()		#oledにデータを表示
    
    led.value(1) #led点灯
    print(data)  #シリアル通信にてデータ送信
    sleep(60)	 #1min待機
    led.value(0) #led消灯