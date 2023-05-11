#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number"""
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)
