#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import LED
from time import sleep

LED_R_PIN = 17  # Red
LED_Y_PIN = 27  # Yellow
LED_G_PIN = 22  # Green
WAIT_TIME = 3

led_list = [
    LED(LED_R_PIN),
    LED(LED_Y_PIN),
    LED(LED_G_PIN)
]
led_list[0].on()
led_list[1].on()
led_list[2].on()
sleep(WAIT_TIME)
led_list[0].off()
led_list[1].off()
led_list[2].off()

