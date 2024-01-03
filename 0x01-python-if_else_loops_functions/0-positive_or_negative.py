#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0: 
    print("{} is negetaive\n")
elif number == 0:
    print("{} is zero\n")
else:
    print("{} is positive\n")
