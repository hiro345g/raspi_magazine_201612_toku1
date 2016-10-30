# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from servo import create_servo
from time import sleep
import sys

SERVO_PIN = 18
WAIT_TIME = 1


def main(servo_type):
    servo = create_servo(SERVO_PIN, servo_type)
    v0 = -10
    for i in range(20):
        v = v0 + i
        print(v)
        servo.value = v * 0.1
        sleep(WAIT_TIME)


if __name__ == '__main__':
    servo_type = 'parts.servo'
    if len(sys.argv) > 1:
        servo_type = sys.argv[1]
    main(servo_type)

