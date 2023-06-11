#!/usr/bin/python3

# This class inherits from the built-in `list` class and adds a

# public instance method `print_sorted()` that prints the list,

# but sorted (ascending sort).

class MyList(list):

    # Prints the list, but sorted (ascending sort).

    def print_sorted(self):

        """

        This method prints the list, but sorted (ascending sort).

        Args:

            self: The instance of the `MyList` class.

        Returns:

            None.

        """

        print(sorted(self))
