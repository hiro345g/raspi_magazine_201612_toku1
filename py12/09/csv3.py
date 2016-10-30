#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

values = [
  ['2016-10-01 00:00:00', 23],
  ['2016-10-01 00:00:01', 24],
  ['2016-10-01 00:00:02', 25],
  ['2016-10-01 00:00:03', 23.5],
]
file_name = 'csv3.csv'
mode = 'wt'
with open(file_name, mode) as file_obj:
    csv_writer = csv.writer(file_obj, delimiter='\t', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerows(values)

mode = 'rt'
with open(file_name, mode) as file_obj:
    csv_reader = csv.reader(file_obj, delimiter='\t', quotechar='"')
    for row in csv_reader:
        print('----')
        for column in row:
            print(column)

