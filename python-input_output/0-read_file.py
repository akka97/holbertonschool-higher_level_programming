#!/usr/bin/python3
"""Opening and reading file module"""


def read_file(filename=""):
    """reading a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        fr = f.read()
        print(fr, end="")
