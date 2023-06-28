#!/usr/bin/python3
'''Inherted class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        tostr = "[Square] ({}) ".format(self.id)
        tostr += "{}/{} - ".format(self.x, self.y)
        tostr += "{}".format(Self.size)
        return tostr
