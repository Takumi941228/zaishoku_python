# プログラミング技術（Python入門）

## 統合開発環境（IDE）について（Jupyter NoteBook）

Python言語の基本を学習するために、Webブラウザ上で動作するWebアプリケーションのJupyter NoteBookを使用します。Jupyter Notebookとは、機械学習などのデータ分析に使用されることを想定されており、データの可視化などの作業に適しています。対話型の開発環境であるため結果が直ぐに出力されるので、実行結果やグラフの描画などビジュアル面が充実しています。また、前の実行結果に応じて、次に実行するプログラムや作業を選択することができます。現在は開発が進み、Pythonだけでなく、RubyやGo言語なと多くの言語がサポートされています。

![外観図](./image/img1.png)

Jupyter Notebookはオープンソースであり、無償利用が可能です。また、Numpy、Pandasなどの科学計算やデータ解析、機械学習を行うライブラリもすでにインストール済みで、すぐに始められます。

## 環境構築の準備

Jupyter NoteBookを利用するには、以下の２つがあります。今回は、Anacondaを使ったインストールを行います。

* pipコマンドを使ったインストール
* Anacondaを使ったインストール

以下のアドレスからAnacondaをダウンロードし、インストールします。

* <https://www.anaconda.com/products/distribution>

## Jupyter NoteBookの使い方 

### Jupyter NoteBookの起動

WindowsのスタートメニューからAnaconda3の中のJupyter NoteBookをクリックし、起動します。

![外観図](./image/img2.png)

ターミナル画面が立ち上がり、起動する。

![外観図](./image/img3.png)

ご自身のPC内のディレクトリから開きたいファイル（拡張子は：`.ipynb`）をクリックする。画像は、今回使用するフォルダのコードを参照しています。

フォルダの階層
```
zaishoku_python
|---jyupter_cone
|       |---Matplotlib
|       |---Numpy
|       |---Pandas
|       |---Python
|            |---python_1.ipynb
|---pico_code
```

![外観図](./image/img4.png)

クリックと同時にファイルがRunning状態となり、プログラムが実行できるようになります。

### プログラムの実行

Running状態のコードを[▶Run]をクリックすると、cellごとにプログラムを実行することができます。

![外観図](./image/img5.png)

### 新規ファイルの作成

NeWをクリックし、インタプリタを[Python3(ipykernel)]を選択します。

![外観図](./image/img17.png)

以下のコードを画像のように入力してください。

```python
print('Hello Python')
10 + 10
```

![外観図](./image/img18.png)

入力および実行が終わったら名前を付けて保存しましょう。Untitledをクリックし、任意の名前を入力してください。

![外観図](./image/img19.png)

### Jupyter NoteBookの終了

上記タブのFileから[close and Halt]をクリックして、ターミナル画面上で[ctrl+cキー]を押すと、数秒後に終了します。

![外観図](./image/img20.png)
