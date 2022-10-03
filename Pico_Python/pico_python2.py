# pico_python2.py
import pandas as pd
# グラフ描画ライブラリ matplotlibのpyplotを plt という名前でimport
import matplotlib.pyplot as plt

#データフレームdfにcsvファイルからのデータにカラムの名前を付けて格納する
df = pd.read_csv('test.csv', names=("TimeStamp", "Temperature", "Pressure", "Humidity"),encoding='utf8')

#2x2=4つのグラフを作成する
fig, axes = plt.subplots(2,2,tight_layout=True)

#グラフそれぞれにx軸とy軸のデータ、色を指定し、プロットする
df.plot(ax=axes[0,0], x='TimeStamp', y=["Temperature"], color="red")
df.plot(ax=axes[0,1], x='TimeStamp', y=["Pressure"], color="blue")
df.plot(ax=axes[1,0], x='TimeStamp', y=["Humidity"], color="green")

#サブプロットにタイトル追加
axes[0,0].set_title("Temperature")
axes[0,1].set_title("Pressure")
axes[1,0].set_title("Humidity")

#サブプロットに軸ラベル追加
axes[0,0].set_ylabel("Temp[℃]")
axes[0,1].set_ylabel("Press[hPa]")
axes[1,0].set_ylabel("Humi[%]")

#サブプロットに軸範囲を追加
axes[0,0].set_ylim(0,40)
axes[0,1].set_ylim(800, 1100)
axes[1,0].set_ylim(0, 100)

#グラフの表示（jupyterだと不要）
plt.show()