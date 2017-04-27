# i2clcd
ラズパイで i1c を使って 16x2 のLCDを使うためのやつ

## 準備
### ハード

LCDの基盤に書かれたピン | RPiのGPIOピン
--- | ---
GND | GND
VCC | 5V (右の列の上から１番目のピン)
SDA | SDA (GPIO 2)
SCL | SCL (GPIO 3)

### ソフト

`sudo raspi-config` を実行 `Advanced Option`→`I2C`→`Enable I2C`→`Finish`　　　　　　　　     

*ここで一回再起動する。*　　　

`sudo nano /etc/modules`を実行して`i2c-bcm2708`と`i2c-dev`を足す（終わったら`Ctrl + X`と`Y`と押す）　　　

ダウンロードした`setup.sh`を実行する (`sudo chmod a+x setup.sh`→`./setup.sh`) そうすると自動的に再起動する。   

最後に`sudo i2cdetect -y 1`か`sudo i2cdetect -y 0`を実行してちゃんとつながってるかチェックする。 (`ERRno 5`が出る場合はこれを実行してつながってるかチェックしよう！)
