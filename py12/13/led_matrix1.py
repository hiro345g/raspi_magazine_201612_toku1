#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import parts.led_matrix as led_matrix

HT16K33_ADDRESS = 0x70
WAIT_TIME = 3


def pattern1(fd):
    # クリア
    matrix_data = led_matrix.clear()
    led_matrix.update(fd, matrix_data)
    # (0,0)から(7,7)まで順に点灯
    wait_time = 0.1
    for j in range(8):
        for i in range(8):
            matrix_data = led_matrix.turn_on_led(i, j, matrix_data)
            led_matrix.update(fd, matrix_data)
            sleep(wait_time)


def pattern2(fd):
    # クリア
    matrix_data = led_matrix.clear()
    led_matrix.update(fd, matrix_data)
    # (0,0)から(7,7)まで順に1つずつ点灯
    wait_time = 0.1
    for j in range(8):
        for i in range(8):
            matrix_data = led_matrix.clear()
            matrix_data = led_matrix.turn_on_led(i, j, matrix_data)
            led_matrix.update(fd, matrix_data)
            sleep(wait_time)


def pattern3(fd):
    list_8x8_b = [
        0b00000000,  # 0x00
        0b00000000,  # 0x00
        0b00000000,  # 0x00
        0b00011000,  # 0x18
        0b00011000,  # 0x18
        0b00000000,  # 0x00
        0b00000000,  # 0x00
        0b00000000,  # 0x00
    ]
    # クリア
    matrix_data = led_matrix.clear()
    led_matrix.update(fd, matrix_data)
    led_matrix.update(fd, list_8x8_b)


def main():
    fd = led_matrix.init(HT16K33_ADDRESS)
    pattern1(fd)
    sleep(WAIT_TIME)
    pattern2(fd)
    sleep(WAIT_TIME)
    pattern3(fd)
    sleep(WAIT_TIME)
    matrix_data = led_matrix.clear()
    led_matrix.update(fd, matrix_data)


if __name__ == '__main__':
    main()
