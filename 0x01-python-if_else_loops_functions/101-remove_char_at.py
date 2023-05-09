#!/usr/bin/python3
def remove_char_at(string, n):
    # Check if n is a valid index
    if n < 0 or n >= len(string):
        return string
    
    # Copy the string character by character, skipping the one at index n
    result = ""
    for i in range(len(string)):
        if i != n:
            result += string[i]
    
    return result
