#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bme280 import bme280, bme280_i2c
from gpiozero import Button, LED
from time import sleep
from datetime import datetime
import csv

# 定数
LED_PIN = 4
BUTTON_PIN = 13
I2C_ADDRESS = 0x76
I2C_BUS = 1
WAIT_TIME = 1
FILE_NAME = '09-%Y%m%d%H%M%S.csv'
DATA_NUM = 30  # 記録するデータ数

# 初期設定
led = LED(LED_PIN)
led.off()
button = Button(BUTTON_PIN)
bme280_i2c.set_default_i2c_address(I2C_ADDRESS)
bme280_i2c.set_default_bus(I2C_BUS)
bme280.setup()

is_stop = False  # 繰り返し継続判定用
while not is_stop:  # is_stopがFalseの間、繰り返し
    cnt = 0  # 記録するデータ数に到達したかの判定用
    values = []  # CSV出力用データを保存するリスト
    while cnt < DATA_NUM:  # DATA_NUMまでリストへ記録
        if button.is_pressed:  # スイッチの状態確認
            is_stop = True  # 停止のためTrue
            led.on()  # 保存開始のLED点灯
            break  # このwhileの処理を抜ける
        t = datetime.now()  # 現在時刻取得
        data = bme280.read_all()  # データ取得
        values.append([  # valuesリストへデータ追加
             t,  # 時刻
             data.pressure,  # 気圧
             data.humidity,  # 湿度
             data.temperature])  # 温度
        cnt += 1  # カウントアップ
        sleep(WAIT_TIME)  # WAIT_TIME秒休止
    current_datetime = datetime.now()  # ファイル名用
    file_name = current_datetime.strftime(FILE_NAME)
    mode = 'wt'  # ↑ 現在時刻からファイル名決定
    with open(file_name, mode) as file_obj:  # 記録
        csv_writer = csv.writer(file_obj)
        csv_writer.writerows(values)

led.off()  # 保存完了のLED消灯

