#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)[:2 - len(t1)]
    tuple_b += (0, 0)[:2 - len(t2)]
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
