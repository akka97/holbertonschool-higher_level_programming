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
        if attrs is None:
            for attr, value in self.__dict__.items():
                d[attr] = value
        else:
            for string in attrs:
                if type(string) is str:
                    if string in self.__dict__.keys():
                        d[string] = self.__dict__[string]
        return d
