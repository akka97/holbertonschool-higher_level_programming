#!/usr/bin/python3
"""another square model"""


class Square:
    """init func"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
