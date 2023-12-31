#!/usr/bin/python3

def print_square(size):
    """ Print a square with the character '#'
    Args:
        size (int): The size of the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        Returns:
            None"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
