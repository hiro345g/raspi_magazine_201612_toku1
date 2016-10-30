#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import LED, Button
from time import sleep

LED_R_PIN = 17  # Red
LED_Y_PIN = 27  # Yellow
LED_G_PIN = 22  # Green
BUTTON_PIN = 13  # スイッチ
WAIT_TIME = 3  # LED点灯時間用
FILE_NAME = 'led_status.txt'  # セーブ用ファイル名


def status_to_str(led_list):  # LEDの状態を文字列にする関数
    status = '['  # 最初の文字は [
    for led in led_list:  # 各LEDについて処理
        if led.is_active:
            status += '1,'  # 点灯は「1,」
        else:
            status += '0,'  # 消灯は「0,」
    status += ']'  # 最後の文字は ]
    return status


def status_update(led_list, status):  # 文字列からLED状態更新
    if status is None:  # statusの値がNoneの時にTrue
        return  # 関数終了
    status_list = eval(status)  # 文字列statusをリストに変換
    for index, led_status in enumerate(status_list):
        if led_status == 1:  # led_statusの値で点灯消灯判別
            led_list[index].on()  # 対象のLED点灯
        else:
            led_list[index].off()  # 対象のLED消灯


def next_led(led_list):  # 現在のLEDを消灯し次のLEDを点灯
    current_index = 0  # 現在点灯しているLEDの添字
    for index, led in enumerate(led_list):
        if led.is_active:  # 現在点灯しているLEDはTrue
            current_index = index
    next_index = current_index + 1  # 次の添字を計算
    if next_index == 3:  # 3の場合は最初の0にして循環
        next_index = 0
    led_list[current_index].off()  # 現在のLEDは消灯
    led_list[next_index].on()  # 次のLEDは点灯
    sleep(WAIT_TIME)  # 点灯時間分待機


def main():  # メイン処理
    led_list = [  # 3つのLEDを表すリスト変数
        LED(LED_G_PIN),
        LED(LED_Y_PIN),
        LED(LED_R_PIN)
    ]
    button = Button(BUTTON_PIN)  # スイッチ

    # LEDの状態をファイルからロード
    mode = 'rt'
    with open(FILE_NAME, mode) as file_obj:
        s = file_obj.read()
        print('Load')
    status_update(led_list, s)
    sleep(WAIT_TIME)
    saved = False  # セーブ処理実施記録用
    while not saved:  # notはsavedの真偽を反転
        next_led(led_list)
        if button.is_pressed:
            # LEDの状態をファイルへセーブ
            s = status_to_str(led_list)
            mode = 'wt'
            with open(FILE_NAME, mode) as file_obj:
                file_obj.write(s)
                print('Save')
            saved = True


main()
