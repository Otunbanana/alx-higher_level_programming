#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
