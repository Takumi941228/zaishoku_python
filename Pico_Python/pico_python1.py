# coding: utf-8
#各種ライブラリをインポート
from time import sleep
import datetime
import csv
import serial

#シリアルポートを設定(XXにはPicoのCOM番号, 通信速度:921600bps)
ser = serial.Serial('COMXX', 921600)

try:
    while True:
        #シリアル通信からデータを改行コード¥nまで取得
        data = ser.readline()
        sleep(1) #1sec待機

        #改行コードで分割
        data = data.split(b'\r\n')
        #バイナリデータを文字列に変換
        data = data[0].decode()
        #カンマで分割し、list型dataに格納
        data = data.split(',')
        #データの確認
        print(data)
        
        #datetimeライブラリから現在の時刻を取得
        dt_now = datetime.datetime.now()
        #ファイル名(test.csv)を作成し、カンマ区切りで(現在時刻,温度,湿度,気圧)書き込む
        with open('test.csv', 'a') as f:
            f.write(dt_now.strftime('%Y/%m/%d %H:%M:%S') + "," + data[0]  + "," + data[1]  + "," + data[2] + "\n")
    
except KeyboardInterrupt:#キーを押して終了した時は何もしないでプログラムを終了する
    pass