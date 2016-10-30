#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import Button
from time import sleep

BUTTON_PIN = 13
WAIT_TIME = 1

button = Button(BUTTON_PIN)
while True:
    if button.is_pressed:
        print('スイッチは押されています')
    else:
        print('スイッチは押されていません')
    sleep(WAIT_TIME)

