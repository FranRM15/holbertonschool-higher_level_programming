#!/usr/bin/python3
"""Function that returns True if the object is exactly an instance
    of the specified class"""


def is_same_class(obj, a_class):
    """Is an instance verification"""

    return type(obj) is a_class
