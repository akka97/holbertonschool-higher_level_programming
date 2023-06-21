#!/usr/bin/python3
"""Module for objects and classes"""


def is_kind_of_class(obj, a_class):
    """Finds if object is in the same class"""
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
