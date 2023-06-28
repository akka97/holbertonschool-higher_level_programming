#!/usr/bin/python3
'''First Class'''


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.if = id
        else:
            Base._nb_objects += 1
            self.id = Base.__nb_objects
