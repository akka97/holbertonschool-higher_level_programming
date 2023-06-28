#!/usr/bin/python3


'''Inherted class'''

class Square(Rectangle):
    '''Square class'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

