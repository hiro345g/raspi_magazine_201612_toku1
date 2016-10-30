#!/usr/bin/env python3
# -*- coding: utf-8 -*-

empty_dict = {}  # 空の辞書
dict1 = {'led':13, 'button':15}  # 要素数2の辞書
dict2 = { 1:'Jan', 2:'Feb', 3:'Mar' }  # 要素数3の辞書
print(dict2[1])  # キー1に対応するJanが表示
print(dict2[2])  # キー2に対応するFebが表示
dict2[4] = 'Apr'  # キー4と対応する値の設定
print('dict1のキーと値の一覧')
for k in list(dict1.keys()):
    print('\t{0}:{1}'.format(k, dict1[k]))
print('dict1のキーと値一覧（キーでソート済み）')
for k in sorted(dict1.keys()):
    print('\t{0}:{1}'.format(k, dict1[k]))
print('dict2のキーと値を同時に取得')
for k, v in dict2.items():
    print('\t{0}:{1}'.format(k, v))
print('dict1からキーbutton削除')
del dict1['button']  # 要素の削除
for k, v in dict1.items():
    print('\t{0}:{1}'.format(k, v))
