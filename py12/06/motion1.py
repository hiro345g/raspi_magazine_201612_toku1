#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from gpiozero import LED, MotionSensor
from time import sleep

MOTION_SENSOR_PIN = 21
LED_PIN = 4
WAIT_TIME = 1


def on(led, time_str):
    led.on()
    print("{0}\t感知しました".format(time_str))


def off(led, time_str):
    led.off()
    print("{0}\t感知しませんでした".format(time_str))


def main():
    motion_sensor = MotionSensor(MOTION_SENSOR_PIN)
    led = LED(LED_PIN)
    motion_sensor.wait_for_motion()
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    print('{0}'.format(current_datetime))
    print('\t{0}'.format(current_date))
    print('\t{0}'.format(current_time))
    print("\t感知しました")
    sleep(WAIT_TIME)

    fmt = '%Y/%m/%d %H:%M:%S'
    for i in range(10):
        current_datetime = datetime.now()
        time_str = current_datetime.strftime(fmt)
        if motion_sensor.motion_detected:
            on(led, time_str)
        else:
            off(led, time_str)
        sleep(WAIT_TIME)


main()
