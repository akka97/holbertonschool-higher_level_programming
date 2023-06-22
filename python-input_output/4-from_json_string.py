#!/usr/bin/python3
"""Writing inside a file module"""


import json


def from_json_string(my_obj):
    """Write in sjon string format"""
    return json.loads(my_obj)
