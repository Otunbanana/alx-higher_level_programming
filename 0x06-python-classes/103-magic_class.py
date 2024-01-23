#!/usr/bin/python3
"""
This module defines a MagicClass class.
"""

import math

class MagicClass:
    """
    Class representing a magic circle.

    Attributes:
        __radius (float):representing the radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Parameters:
            radius (float, optional): Radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
            float: Circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
