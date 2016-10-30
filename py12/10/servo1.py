# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
import gpiozero

SERVO_PIN = 18
WAIT_TIME = 1


servo = gpiozero.Servo(SERVO_PIN)
servo.min()  # 最小の位置
sleep(WAIT_TIME)
servo.mid()  # 中間の位置
sleep(WAIT_TIME)
servo.max()  # 最大の位置
sleep(WAIT_TIME)

