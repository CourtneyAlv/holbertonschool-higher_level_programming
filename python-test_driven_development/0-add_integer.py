#!/usr/bin/python3

def add_integer(a, b=98):
    """ Adde two integers or floatsvand return the result as an integer
    :a: the first number(integer or float)
    :b: the second number(int, or float, default is 98)
    :return: The addition of a and b as an integer"""

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = round(a)
    b = round(b)
    return a + b
