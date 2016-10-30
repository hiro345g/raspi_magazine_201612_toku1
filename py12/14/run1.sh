#!/bin/sh
cd /home/pi/py12/14
PYTHONPATH="/home/pi/py12/py12-packages:$PYTHONPATH" python3 led_7seg1.py $@
