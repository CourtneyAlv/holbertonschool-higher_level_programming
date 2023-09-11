#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

matrix = [[0] * 3 for i in range(3)]

    for i in range(3):
        for j in range(3):
            matrix[i][j] = "{}, {},".format(i, j)