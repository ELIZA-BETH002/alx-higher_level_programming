#!/usr/bin/python3

"""
contains MyList class
"""

class MyList(list):

    def print_sorted(self):

        sorted_list = sorted(self)  # Sort the list in ascending order

        print(sorted_list)  # Print the sorted list
