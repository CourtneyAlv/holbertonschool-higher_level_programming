#!/usr/bin/python3
"""Defines a pascal Triangle"""

def pascal_triangle(n):
    """representing the Pascal’s triangle of n
        Args:
            n (int): the number of rows to generate
        Returns:
            List (int): a list of list representing pascal triangles
        """

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) is not n:
        tri_angle = triangle[-1]
        temp = [1]
        for t in range(len(tri_angle) - 1):
            temp.append(tri_angle[t] + tri_angle[t + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
