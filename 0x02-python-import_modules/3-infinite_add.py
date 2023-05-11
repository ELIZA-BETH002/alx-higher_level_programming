#!/usr/bin/python3
import sys

# Get the command-line arguments
arguments = sys.argv[1:]  # Exclude the script name

# Calculate the sum of the arguments
result = sum(int(arg) for arg in arguments)

# Print the result
print(result)

