#!/usr/bin/python3
"""Opening and reading file module"""


def write_file(filename="", text=""):
    """text written inside the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
