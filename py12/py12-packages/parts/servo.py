# -*- coding: utf-8 -*-
import wiringpi


class Servo:
    """ SG90サーボモーター用クラス """
    PWM_CLOCK = 375

    def __init__(self, pin):
        """ 初期化メソッド """
        self.pin = pin  # GPIOピン
        self._degree = 0  # 角度の初期値
        # wiringpiの初期化
        # wiringpi.wiringPiSetupGpio() は __init__.py で実行済み
        wiringpi.pinMode(self.pin, wiringpi.PWM_OUTPUT)
        wiringpi.pwmSetMode(0)
        wiringpi.pwmSetRange(1024)
        wiringpi.pwmSetClock(self.PWM_CLOCK)

    def _set_position(self, degree):
        """ 角度を度数で受け取って指定位置まで回転
        0より小さい値は0、180より大きい値は180へ修正
        """
        d = degree
        if degree < 0:
            d = 0
        elif 180 < degree:
            d = 180
        value = int(26 + (48 * d) / 90)
        wiringpi.pwmWrite(self.pin, value)

    def min(self):
        self.value = -1

    def max(self):
        self.value = 1

    def mid(self):
        self.value = 0

    @property
    def value(self):
        return self._degree

    @value.setter
    def value(self, value):
        self._degree = (value + 1) * 90
        self._set_position(self._degree)

    @value.deleter
    def value(self):
        del self._degree
