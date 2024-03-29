#!/usr/bin/python3
"""
This module contains a function that adds two integers.

"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
