#!/usr/bin/python3

def matrix_divided(matrix, div):
    """ Divide all elements of a matrix by a number and return a new matrix
        :matrix: a list of lists of ints, or floats
        :div: a number (integers or float) to divide the elements
        :return: a new matrix with elements rounded 2 decimals"""

    if not isinstance(matrix, list) or not all(
            all(isinstance(e, (int, float)) for e in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [
           [round(element / div, 2) for element in row] for row in matrix
        ]
    return new_matrix
