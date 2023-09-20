#!/usr/bin/python3

def text_indentation(text):
    """A function that prints 2 new lines after each character: ., ?, :

    Args:
        :text (str): The input to be processed and printed

        Raises:
            TypeError: if the input is not a string.

        :return: None
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    result = 0
    while result < len(text) and text[result] == ' ':
        result += 1
    while result < len(text):
        print(text[result], end="")
        if text[result] == "\n" or text[result] in ".?:":
            if text[result] in ".?:":
                print("\n")
            result += 1
            while result < len(text) and text[result] == ' ':
                result += 1
            continue
        result += 1
