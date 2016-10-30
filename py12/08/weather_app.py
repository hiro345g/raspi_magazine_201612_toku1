#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sample.weather import print_weather
from time import sleep

WAIT_TIME = 1
for i in range(10):
    print_weather()
    sleep(WAIT_TIME)

