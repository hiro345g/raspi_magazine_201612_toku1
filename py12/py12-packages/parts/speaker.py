# -*- coding: utf-8 -*-
import time, wiringpi


class Speaker:
    """ Speaker用クラス """

    def __init__(self, pin):
        """ 初期化メソッド """
        self.pin = pin  # 電子スピーカー用のGPIOピン
        wiringpi.softToneCreate(self.pin)

    def play(self, melody):
        """ ソフトウェアトーン再生"""
        for v, play_time in melody:  # 指定されたメロディーの再生
            wiringpi.softToneWrite(self.pin, v)  # トーン発生
            time.sleep(play_time)  # 同じ音を出力するために処理を遅延
        self.play_stop()

    def play_stop(self):
        """ 再生終了 """
        wiringpi.softToneWrite(self.pin, 0)  # 再生終了
