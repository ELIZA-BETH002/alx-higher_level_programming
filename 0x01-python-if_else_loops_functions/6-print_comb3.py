#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        print("{:02d}, {:02d}, ".format(i, j), end="")
print("\b\b\n", end="")
