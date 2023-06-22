#!/usr/bin/python3
"""Writing inside a file module"""


def append_write(filename="", text=""):
    """text written inside the file"""
    with open(filename, 'a', encoding="utf-8") as f:
        count = f.write(text)
    return count
