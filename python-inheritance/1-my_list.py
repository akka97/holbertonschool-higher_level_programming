#!/usr/bin/python3
"""list subclass"""

class MyList(list):
    """Prints a sorted list"""
    def print_sorted(self):
        ls = self.copy()
        list.sort()
        print(list)
        return list
