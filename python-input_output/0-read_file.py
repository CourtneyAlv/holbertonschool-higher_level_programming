#!/usr/bin/python3

def read_file(filename=""):
    """reads a text file and prints to stdout

        Args:
            filename (str): The name of the text file to read
            """
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
