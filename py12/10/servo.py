# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
import gpiozero
import parts.servo
import sys

SERVO_DEFAULT_TYPE = 'parts.servo'
SERVO_PIN = 18
DEFAULT_WAIT_TIME = 1


def create_servo(pin, servo_type):
    if servo_type == 'gpiozero':
        return gpiozero.Servo(pin)
    else:
        return parts.servo.Servo(pin)


def main(servo_type, pin, wait_time):
    servo = create_servo(pin, servo_type)
    servo.min()
    sleep(wait_time)
    servo.mid()
    sleep(wait_time)
    servo.max()
    sleep(wait_time)


if __name__ == '__main__':
    t = SERVO_DEFAULT_TYPE
    if len(sys.argv) > 1:
        t = sys.argv[1]
    main(t, SERVO_PIN, DEFAULT_WAIT_TIME)

