#!/usr/bin/python3
"""Module for objects and classes"""


def inherits_from(obj, a_class):
    """Finds if object is in the same class"""
    if isinstance(obj, a_class):
        if obj.__class__ is a_class:
            return False
        return True
    return False
