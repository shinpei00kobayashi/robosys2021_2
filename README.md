# robosys2021_2
rosを用いてオリジナリティーのあるソフトの開発を行う

# 実装内容
ROSを用いてGPIOへの出力と、簡易電卓を実装しました。また実行結果をサブスクライバにて確認することができます

・プログラム１

1から9の数字をカウントし3の倍数でバカになります。その際にGPIO24から21が出力されます

※昔のお笑い芸人のネタをオマージュしています

・プログラム２

簡易電卓が使えます。答えを算出する際にGPIOが出力されます

いずれも値を入力する際に間違った値が入力されると警告文が表示されプログラムが終了するようにしました。


# 実装環境

ソフトの実行を行うためには以下の環境を構築してください

|  CPU |      OS      |GPIO.lib|  ROS   |
|------|--------------|--------|------- |
|corei5| ubuntu20.04  |WiringPi| noetic |

GPIO.libのインストールはページの下部のサイトを参照してください

配線は以下のように行ってください
![E6323D9E-2F5E-4D66-8113-4261162DED92](https://user-images.githubusercontent.com/97512094/149515616-0d6f4653-724b-43b4-bb3c-723ca176098e.jpg)
![9D923F95-16BB-44C8-B31A-161B656EA777](https://user-images.githubusercontent.com/97512094/149515678-32fe5f85-daa0-4583-80c8-ed46632985e6.jpg)

# 実行方法
①プログラムインストール
```bash
cd ~/catkin_ws/src
git clone https://github.com/shinpei00kobayashi/robosys2021_2.git
```

②パッケージをビルド

```bash
cd ~/catkin_ws
catkin_make
souce ~/catkin_ws/devel/set_up.bash
```

③roscoreの起動
```bash
端末1: roscore
```

④プログラム起動
```bash
端末2:rosrun testn led.py
端末3:rosrun testn leds.py
```

⑤1⇒GPIO(LED),2⇒Tkinter(簡易電卓)
```bash
$rosrun testn led.py                        
1 or 2を入力してください
```

⑥1⇒1~9までカウントします。3の倍数でバカになり、GPIO24,23,22,21が出力されます
```bash

端末2
1 or 2を入力してください1
1
2
3!!!!
...
9!!!


端末3
[INFO]1
[INFO]2
[INFO]3
'''
[INFO]9

```

⑦2⇒簡易電卓が使用できます。案内に沿って値を入力してください

答えを算出する際GPIOが出力されLEDが光ります

また小数の計算の場合計算式で使用した型(decmal)と送信用の型(Float32)が違うため出力結果が多少異なります


例 20.14+2021.2

```bash
端末2
1 or 2を入力してください2                                                           
最初の数字を入力してください:2                                                    
次の数字を入力:2 
いずれかのkeyを入力してください                                                     
+...加算
-...引算
*...掛算 
/...割算
+
20.14+2021.2=
2041.34

端末3
[INFO]2041.3399658203125
```

# DEMO動画
https://youtu.be/gjBjQuyFM9s

# 参照サイト
WiringPI_install
https://qiita.com/nanbuwks/items/f70005772133bf54f4d3
