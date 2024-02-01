#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """
    stop user from instantiating new LockedClass attributes
    all but attributes called 'first_name'.
    """
    __slots__ = ("first_name",)
