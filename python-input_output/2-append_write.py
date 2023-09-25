#!/usr/bin/python3
""" append a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """"appends a string at the end of a text file (UTF8) and returns the
    number of characters added
        Args:
            filename (str): the name of the text file
            text (str): text to append file to

        Returns:
            int: number of characters added
            """
    with open(filename, mode='a', encoding='utf-8') as file:
        add_char = file.write(text)
    return add_char
