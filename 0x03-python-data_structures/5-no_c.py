#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = (char for char in my_string if char.lower() not in ('c', 'C'))
    return (''.join(filtered_chars))
