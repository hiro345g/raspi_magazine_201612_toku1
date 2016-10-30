#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep
import parts.led_7seg as led_7seg
import sys

# -- 変数 -- #
HT16K33_ADDRESS = 0x70


def count_up(fd):  # 最初のカウントアップ処理用の関数
    for i in range(0, 10):
        data = led_7seg.clear()
        for digit in range(4):
            data[digit] = led_7seg.get_font(str(i))
        led_7seg.update(fd, data)  # 4桁を同時に更新
        sleep(1)


def clock(fd):  # 時計処理用の関数
    fmt = '%H%M%S'
    interval = 1  # 1秒単位で更新
    data = led_7seg.clear()  # クリア
    led_7seg.update(fd, data)  # 4桁を同時に更新
    while True:
        current_datetime = datetime.now()
        time_str = current_datetime.strftime(fmt)
        time_list = list(time_str)
        data = led_7seg.clear()
        data[0] = led_7seg.get_font(time_list[0])
        data[1] = led_7seg.get_font(time_list[1])
        if int(time_str) % 2 == 0: # 偶数秒はドット点灯
            data[1] += led_7seg.SEVEN_SEG_PERIOD
        data[2] = led_7seg.get_font(time_list[2])
        data[3] = led_7seg.get_font(time_list[3])
        led_7seg.update(fd, data)  # 4桁を同時に更新
        sleep(interval)


def main(font_type):
    if font_type == 'sample':
        font = {  # 6, 9を変更してある
            '0': 0x3F,
            '1': 0x06,
            '2': 0x5B,
            '3': 0x4F,
            '4': 0x66,
            '5': 0x6d,
            '6': 0x7c,
            '7': 0x07,
            '8': 0x7F,
            '9': 0x67,
        }
        fd = led_7seg.init(HT16K33_ADDRESS, font)
    elif font_type == 'default':
        fd = led_7seg.init(HT16K33_ADDRESS)
    else:
        print('未対応')
        return
    count_up(fd)
    sleep(3)
    clock(fd)


if __name__ == '__main__':
    # 下記のどちらを実行するかで7セグLEDの表示が変わる
    # $ sudo sh ~/py12/14/run1.sh
    # $ sudo sh ~/py12/14/run1.sh sample
    argv_font_type = 'default'
    if len(sys.argv) > 1:
        argv_font_type = sys.argv[1]
    main(argv_font_type)

