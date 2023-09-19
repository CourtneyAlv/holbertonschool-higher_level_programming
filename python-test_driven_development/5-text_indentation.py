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

    sentences = []
    orig_sentence = ""
    for char in text:
        orig_sentence += char
        if char in ".?:":
            sentences.append(orig_sentence.strip())
            orig_sentence = ""

    for sentence in sentences:
        print(sentence)
