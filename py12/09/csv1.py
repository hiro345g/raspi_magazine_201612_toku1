#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

values = [
  ['2016-10-01 00:00:00', 23],
  ['2016-10-01 00:00:01', 24],
  ['2016-10-01 00:00:02', 25],
  ['2016-10-01 00:00:03', 23.5],
]
file_name = 'csv1.csv'
mode = 'wt'
with open(file_name, mode) as file_obj:
    csv_writer = csv.writer(file_obj)
    csv_writer.writerows(values)

