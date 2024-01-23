#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class representing a square.

    Attributes:
        __size (float or int):representing the size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (float or int, optional): Size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            float or int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
            value (float or int): Size to be set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: Area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator."""
        return self.area() >= other.area()
