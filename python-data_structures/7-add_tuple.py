#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    element_1a = tuple_a[0] if len(tuple_a) > 0 else 0
    element_2a = tuple_a[1] if len(tuple_a) > 1 else 0
    element_1b = tuple_b[0] if len(tuple_b) > 0 else 0
    element_2b = tuple_b[1] if len(tuple_b) > 1 else 0

    sum_1 = element_1a + element_1b
    sum_2 = element_2a + element_2b

    return sum_1, sum_2
