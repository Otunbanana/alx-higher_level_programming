#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0: 
    print(f"{number:d} is negetaive\n")
elif number == 0:
    print(f"{number:d} is zero\n")
else:
    print(f"{number:d} is positive\n")