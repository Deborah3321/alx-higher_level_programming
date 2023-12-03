#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    given_list = my_list[0:]
    if idx >= 0 and idx <= len(given_list) - 1:
        given_list[idx] = element
        return given_list
    return my_list
