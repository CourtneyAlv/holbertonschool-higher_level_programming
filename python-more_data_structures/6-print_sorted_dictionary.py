#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sort = sorted(a_dictionary)

    for key in sort:
        print("{}: {}".format(key, a_dictionary[key]))
