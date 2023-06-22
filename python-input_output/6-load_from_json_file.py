#!/usr/bin/python3
"""Writing inside a file module"""


import json


def load_from_json_file(filename):
    """Write in sjon string format"""
    with open(filename, 'r', encoding='utf-8') as f:
        read = f.read()
    return json.loads(read)
