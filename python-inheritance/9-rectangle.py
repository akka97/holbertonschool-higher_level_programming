#!/usr/bin/python3
"""Module for objects and classes"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry"""
    def __init__(self, width, height):
        """initalisation of an object"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        to_str = "[Rectangle] "
        to_str += str(self.__width) + '/' + str(self.__height)
        return to_str
