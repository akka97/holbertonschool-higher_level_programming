#!/usr/bin/python3
"""Text identation module"""


def text_identation(text):
    """Idents text when needed"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    char = ['.', '?', ':']
    i = 0
    while i in range(len(text)):
        print('{}'.format(text[i]), end="")
        if text[i] in char:
            print('\n')
            while text[i + 1] == " ":
                i += 1
        i += 1
