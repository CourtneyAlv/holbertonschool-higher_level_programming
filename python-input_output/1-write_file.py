#!/usr/bin/python3
""" writes a string to a text file (UTF8) and returns the number of
characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters
        Args:
            filename (str): the name of the text file to write to
            text (str): text to write to the file

            Returns:
                int: number of characters written
                """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters = file.write(text)
    return characters
