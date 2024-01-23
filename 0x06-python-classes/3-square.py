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
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int, optional): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
