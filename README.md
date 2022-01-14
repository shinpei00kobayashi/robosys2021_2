# robosys2021_2
rosを用いてオリジナリティーのあるソフトの開発を行う

#実装内容
ROSを用いてGPIOへの出力と、簡易電卓を実装しました。

# 実装環境

ソフトの実行を行うためには以下の環境を構築してください

|      OS      |GPIO.lib|  ROS   |
|--------------|--------|------- |
| ubuntu20.04  |WiringPi| noetic |

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
端末2:rosrun  testn led.py
```

⑤1⇒GPIO(LED),2⇒Tkinter(簡易電卓)
```bash
$rosrun testn led.py                        
1 or 2を入力してください
```

⑥1⇒1~9までカウントします。3の倍数でバカになり、GPIO24,23,22,21が出力されます
```bash
1 or 2を入力してください1
1
2
3!!!!
...
9!!!
```

⑦2⇒簡易電卓が使用できます。案内に沿って値を入力してください

答えを算出する際GPIOが出力されLEDが光ります

例 2+2

```bash
1 or 2を入力してください2                                                           
最初の数字を入力してください:2                                                    
次の数字を入力:2 
いずれかのkeyを入力してください                                                     
+...加算
-...引算
*...掛算 
/...割算
+
2+2=
4
```

# DEMO動画
https://youtu.be/YZaq_t9PQT4

# 参照サイト
WiringPI_install
https://qiita.com/nanbuwks/items/f70005772133bf54f4d3
