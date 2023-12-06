#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for m, n in list(a_dictionary.items()):
        if n is value:
            a_dictionary.pop(m)
    return a_dictionary
