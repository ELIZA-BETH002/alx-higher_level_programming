#!/usr/bin/python3
"""Defines a Rectangle Class"""

class Rectangle:

    # Private instance attribute: width

    __width = None

    # Property def width(self): to retrieve it

    @property

    def width(self):

        return self.__width

    # Property setter def width(self, value): to set it:

    @width.setter

    def width(self, value):

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self.__width = value

    # Private instance attribute: height

    __height = None

    # Property def height(self): to retrieve it

    @property

    def height(self):

        return self.__height

    # Property setter def height(self, value): to set it:

    @height.setter

    def height(self, value):

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self.__height = value

    # Instantiation with optional width and height: def __init__(self, width=0, height=0):

    def __init__(self, width=0, height=0):

        self.width = width

        self.height = height

    # Public instance method: def area(self): that returns the rectangle area

    def area(self):

        return self.width * self.height

    # Public instance method: def perimeter(self): that returns the rectangle perimeter:

    def perimeter(self):

        if self.width == 0 or self.height == 0:

            return 0

        return 2 * (self.width + self.height)

    # print() and str() should print the rectangle with the character #: (see example below)

    # if width or height is equal to 0, return an empty string

    def __str__(self):

        if self.width == 0 or self.height == 0:

            return ""

        return "#" * self.width + "\n" * (self.height - 1) + "#" * self.width

    def __repr__(self):

        return "Rectangle(width={!r}, height={!r})".format(self.width, self.height)
