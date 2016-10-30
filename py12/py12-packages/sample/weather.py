#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bme280 import bme280, bme280_i2c


# データの取得と表示
def print_weather():
    data = bme280.read_all()
    p = "{0:7.2f} hPa".format(data.pressure)
    h = "{0:7.2f} ％".format(data.humidity)
    t = "{0:7.2f} C".format(data.temperature)
    print('{0}:{1}:{2}'.format(p, h, t))
