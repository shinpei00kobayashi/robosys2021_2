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

# 実行方法
①プログラムインストール
'''bash
cd ~/catkin_ws/src
git clone https://github.com/shinpei00kobayashi/robosys2021_2.git
'''

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

