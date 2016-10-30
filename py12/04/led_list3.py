#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import LED
from time import sleep

LED_R_PIN = 17  # Red
LED_Y_PIN = 27  # Yellow
LED_G_PIN = 22  # Green
WAIT_TIME = 3

led_list = [
    LED(LED_G_PIN),
    LED(LED_Y_PIN),
    LED(LED_R_PIN)
]
while True:
    for led in led_list:
        led.on()
        sleep(WAIT_TIME)
        led.off()

