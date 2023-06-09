#!/usr/bin/python3
"""Class to json Module"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        d = {}
        for attr, value in self.__dict__.items():
            d[attr] = value
        return d
