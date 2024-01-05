#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = sum(map(int, argv[1:]))
    print(result)
