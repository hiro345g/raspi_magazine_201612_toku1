#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import PWMLED
from time import sleep

LED = 4
WAIT_TIME = 1

led = PWMLED(LED)
v = 0.0
dv = 0.1
try:
    for i in range(30):
        led.value = v
        v += dv
        if v > 1.0:
            print('max')
            v = 1.0
            dv = -0.1
        elif v < 0.0:
            print('min')
            v = 0.0
            dv = 0.1
        sleep(WAIT_TIME)
except KeyboardInterrupt:
    print('キャンセルしました')
finally:
    for i in range(3):
        led.value = 1
        sleep(WAIT_TIME/6)
        led.value = 0
        sleep(WAIT_TIME/6)
    print('終了しました')
