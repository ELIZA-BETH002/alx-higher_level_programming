#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from
    the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from
        the specified class. Otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class