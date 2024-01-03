#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{}".format(chr(i)), end="")
    if i - 1 >= 65:
        print("{}".format(chr(i - 1).upper()), end="")
