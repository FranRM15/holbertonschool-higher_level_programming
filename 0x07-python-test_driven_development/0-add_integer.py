#!/usr/bin/python3
"""Function that adds 2 integers"""


def add_integer(a, b=98):
    """Validations of variables for error handling"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    elif type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)

    return a + b
