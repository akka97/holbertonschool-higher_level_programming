#!/usr/bin/python3
"""list subclass"""

class MyList(list):
    """Prints a sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
