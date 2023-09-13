#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    new_dic = dict(a_dictionary)

    if key in new_dic:
        del new_dic[key]
    return new_dic
