#!/usr/bin/python3
"""Module for objects and classes"""

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """Subclass of Rectangle"""
    def __init__(self, size):
        """initalisation of square object"""
        BaseGeometry.integer_validator(self, 'size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
