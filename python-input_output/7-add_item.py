#!/usr/bin/python3
"""Loading, adding and saving module"""


import os
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if os.path.exists('ad_item.json') is not True:
    with open('add_item.json', 'w', encoding='utf=8') as f:
        load = []
        save_to_json_file(load, 'add_item.json')
load = load_from_json_file('add_item.json')
for i in range(len(atgv)):
    if i != 0:
        load.append(argv[i])
save_to_json_file(load, 'add_item.json')
