#!/usr/bin/python3
"""
This module contains the function is_same_class
"""
def is_same_class(obj, a_class):

    """

    Returns True if the object is exactly an instance of the specified class ; otherwise False.

    Args:

        obj: The object to check.

        a_class: The class to check against.

    Returns:

        True if obj is an instance of a_class, False otherwise.

    """

    return isinstance(obj, a_class) and not isinstance(obj, type(a_class))

