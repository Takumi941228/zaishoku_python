# -*- coding: utf-8-*-
# pico_micropython3.py
#pico用ライブラリPinとI2Cをインポート
from machine import Pin, I2C
#timeライブラリsleepをインポート
from time import sleep
#bme280ライブラリBME280をインポート
from bme280 import BME280

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
    #実際の温度値,湿度値,気圧値にデータを計算
    temp = float(temp / 100)
    press = float((press // 256) / 100)
    humi = float(humi / 1024)
    #文字型に変換してdataに格納
    #humiをround関数で小数点以下第二位で四捨五入
    data = str(temp) + ',' + str(press) + ',' + str(round(humi, 2))
    #計測したデータを戻り値として返す
    return data, temp, press, humi

while True:
    #sensor関数を呼び出し、戻り値をdata,temp,press,humiに格納
    data, temp, press, humi = sensor()
    
    print(data)  #シリアル通信にてデータ送信
    sleep(1)	 #1sec待機