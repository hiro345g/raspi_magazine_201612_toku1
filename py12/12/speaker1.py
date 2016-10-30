#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import Button
from parts.speaker import Speaker
from configparser import ConfigParser

config_file_name = 'speaker.ini'
config = ConfigParser()
config.read(config_file_name)
for section in config.sections():
    print(section)
    for key in config[section]:
        print('\t{0} : {1}'.format(key, config[section][key]))

speaker_pin = int(config['SPEAKER']['pin'])
interval = int(config['SPEAKER']['interval'])
melody_str = config['SPEAKER']['melody']
print('{0}, {1}, {2}'.format(speaker_pin, interval, melody_str))
button_pin = int(config['BUTTON']['pin'])
print('{0}'.format(button_pin))

button = Button(button_pin)
print('初期ファイルを読み込みました。スイッチを押してください')
button.wait_for_press()

speaker = Speaker(speaker_pin)
melody = eval(melody_str)
speaker.play(melody)

