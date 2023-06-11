def add_attribute(obj, attr_name, attr_value):

    """

    Adds a new attribute to an object if it’s possible.

    Args:

        obj: The object to add the attribute to.

        attr_name: The name of the attribute to add.

        attr_value: The value of the attribute to add.

    Raises:

        TypeError: If the object cannot have new attributes.

    """

    if not hasattr(obj, "__setattr__"):

        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
