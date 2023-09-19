#!/usr/bin/python3
"""Module to find the max integer in a list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMxInteger(unittest.TestCase):

    def test_max_integer_standard(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)
    
    def test_max_integer(self):
        result = max_integer([1, 5, 3, 7, 2])
        self.assertEqual(result, 7)

    def test_max_int_negative(self):
        result = max_integer([-1, -5, -3, -7, -2])
        self.assertEqual(result, -1)

    def test_max_int_empty(self):
        result = max_integer([])
        self.assertIsNone(result)
    
    def test_max_int_one_element(self):
        result = [3]
        self.assertEqual(max_integer(result), 3)


    '''def test_max_integer_with_strings(self):
        result = max_integer([1, 5, 'three', 7, 2])
        self.assertEqual(result, 7)'''


if __name__ == '__main__':
    unittest.main()

