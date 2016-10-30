#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

file_name = 'csv1.csv'
mode = 'rt'
with open(file_name, mode) as file_obj:
    csv_reader = csv.reader(file_obj)
    for row in csv_reader:
        print('----')
        for column in row:
            print(column)

