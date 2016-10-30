#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from parts.speaker import Speaker

SPEAKER_PIN = 5
# ドレミのメロディ
melody = ((262, 1),(294, 1),(330, 1),)

# メロディーの値を表示
for value in melody:
    pitch_name, length = value
    print('{0}, {1}'.format(pitch_name, length))

# メロディーの再生
speaker = Speaker(SPEAKER_PIN)
speaker.play(melody)

