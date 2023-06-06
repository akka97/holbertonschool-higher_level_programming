#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 += (0, 0)[:2 - len(t1)]
    t2 += (0, 0)[:2 - len(t2)]
    result = (t1[0] + t2[0], t1[1] + t2[1])
    return result
