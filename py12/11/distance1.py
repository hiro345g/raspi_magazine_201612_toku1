#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HC-SR04を使った距離測定プログラム例
"""

import time
import wiringpi

ECHO_PIN = 26
TRIGGER_PIN = 19
WAIT_TIME = 1


class DistanceSensor:
    """ HC-SR04用クラス """
    # 「self.変数名」で使用可能な定数
    PULSE_TRIGGER = 0.00001  # 測定用超音波発生時間 10 μsec
    SPEED_OF_SOUND = 340  # 音速340 m/sec
    PULSE_TRIGGER_INTERVAL = 0.06  # 次のパルス発生までの待機時間 60 msec
    TIMEOUT = 2 * 180 * 0.01 / SPEED_OF_SOUND  # タイムアウト約0.0105 sec

    def __init__(self, echo, trigger):
        """ 初期化メソッド """
        self.echo = echo  # Echo用のGPIOピン
        self.trig = trigger  # Trig用のGPIOピン
        wiringpi.wiringPiSetupGpio()  # wiringpi初期化
        wiringpi.pinMode(self.trig, wiringpi.OUTPUT)
        wiringpi.pinMode(self.echo, wiringpi.INPUT)
        wiringpi.digitalWrite(self.trig, wiringpi.LOW)

    def _wait_for_echo(self, wait_value, wait_time):
        """ エコーの値が変化した時刻を取得するメソッド """
        timeout = False
        start_time = time.time()
        current_time = start_time
        while wiringpi.digitalRead(self.echo) != wait_value:
            current_time = time.time()
            timeout = (current_time - start_time) > wait_time
            if timeout is True:
                break
        return not timeout, current_time

    def _get_time_echo_on(self):
        """ エコーがHIGHになった時刻を取得するメソッド """
        return self._wait_for_echo(wiringpi.HIGH, self.TIMEOUT)

    def _get_time_echo_off(self):
        """ エコーがLOWになった時刻を取得するメソッド """
        return self._wait_for_echo(wiringpi.LOW, self.TIMEOUT)

    def read(self):
        time.sleep(self.PULSE_TRIGGER_INTERVAL)
        # トリガー信号を発信
        wiringpi.digitalWrite(self.trig, wiringpi.HIGH)
        time.sleep(self.PULSE_TRIGGER)
        wiringpi.digitalWrite(self.trig, wiringpi.LOW)
        # エコーがHIGHになった時刻を取得
        echo_result, start_time = self._get_time_echo_on()
        if echo_result:
            # エコーがLOWになった時刻を取得
            echo_result, end_time = self._get_time_echo_off()
            if echo_result:
                # 距離を計算
                timedelta = end_time - start_time
                return True, timedelta * self.SPEED_OF_SOUND / 2
        return False, 0


def main():
    sensor = DistanceSensor(ECHO_PIN, TRIGGER_PIN)
    while True:
        result, distance = sensor.read()
        print('距離: {0} [mm]'.format(distance * 1000))
        time.sleep(WAIT_TIME)


if __name__ == '__main__':
    main()
