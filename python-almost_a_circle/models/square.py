#!/usr/bin/python3
'''Module for square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        tostr = "[Square] ({}) ".format(self.id)
        tostr += "{}/{} - ".format(self.x, self.y)
        tostr += "{}".format(self.size)
        return tostr

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates square object attributes"""
        att = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returning dictionary representation of square'''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
