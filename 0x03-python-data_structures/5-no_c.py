#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = [char for char in my_string if char != 'c' and char != 'C']
    return ("".join(filtered_chars))
