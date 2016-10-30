#!/bin/sh
cd /home/pi/py12/10
PYTHONPATH="/home/pi/py12/py12-packages:$PYTHONPATH" python3 servo2.py $@
