#!/usr/bin/python3
"""Writing inside a file module"""


import json


def save_to_json_file(my_obj, filename):
    """Write in sjon string format"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
