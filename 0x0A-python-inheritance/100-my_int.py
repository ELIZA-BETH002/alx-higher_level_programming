#!/usr/bin/python3

class MyInt(int):
    def __init__(self, value):
        super().__init__(value)

    # Override the == operator
    def __eq__(self, other):
        # Invert the behavior of the original == operator
        return super().__ne__(other)

    # Override the != operator
    def __ne__(self, other):
        # Invert the behavior of the original != operator
        return super().__eq__(other)
