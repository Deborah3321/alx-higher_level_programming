#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            string += i
    return string
