#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    if (i - ord('z')) % 2 == 0:
        print(f"{}".format(chr(i).lower()), end='')
    else:
        print(f"{}".format(chr(i).upper()), end='')
