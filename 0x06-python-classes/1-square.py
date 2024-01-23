#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class representing a square.

    Attributes:
        __size (int): representing the size of the square.
    """


    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): Size of the square.

        Note:
            The size attribute is private and prefixed with "__".
        """
        self.__size = size
