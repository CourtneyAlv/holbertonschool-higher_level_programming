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

    result = ""
    new_line = True

    for char in text:
        if char in [".", "?", ":"]:
            result += char + "\n\n"
            new_line = True
        elif char != " ":
            result += char
            new_line = False
        elif char == " " and not new_line:
            result += char
    if text.strip()[-1] in [".", "?", ":"]:
        result = result.strip()

    print(result)
