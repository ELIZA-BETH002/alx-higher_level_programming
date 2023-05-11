#!/usr/bin/python3
if __name__ == "__main__":
import sys

# Get the command-line arguments
arguments = sys.argv[1:]  # Exclude the script name

# Print the number of arguments
num_arguments = len(arguments)
print("Number of argument(s):", num_arguments, end="")

if num_arguments == 0:
    print(".", end="\n\n")
else:
    print(":", end="\n\n")

    # Print the list of arguments
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))

    print()  # Add an extra new line after printing the arguments
