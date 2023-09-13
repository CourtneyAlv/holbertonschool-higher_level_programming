#!/usr/bin/python3

def uniq_add(my_list=[]):

    new_list = set()

    total_sum = 0

    for element in my_list:
        if isinstance(element, int) and element not in new_list:
            new_list.add(element)
            total_sum += element
    return total_sum
