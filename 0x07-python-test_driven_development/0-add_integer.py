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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    """
    casting a and b to be an integer value
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    
    return a + b
