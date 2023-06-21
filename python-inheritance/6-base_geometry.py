#!/usr/bin/python3
"""Module for objects and classes"""


class BaseGeometry:
    """base geometry"""
    def area(self):
        raise Exception("area() is not implemented")
