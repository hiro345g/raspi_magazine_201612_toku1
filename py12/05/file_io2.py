#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file_name = 'led_status.txt'
status = '[1,0,0,]'
mode = 'wt'  # mode = 'w'でも同じ
file_obj = open(file_name, mode)
file_obj.write(status)
file_obj.close()
