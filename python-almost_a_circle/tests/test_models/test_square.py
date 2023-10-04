#!/usr/bin/python3
"""Unittest for recatangle"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):

    def test_if_integer(self):
        with self.assertRaises(TypeError):
            s = Square(10, 'five')
    
    def test_if_neg(self):
        with self.assertRaises(ValueError):
            s = Square(10, -3)

    def test_if_int_xy(self):
        with self.assertRaises(TypeError):
            s = Square(2, 2, "six", "eight", "nine")

    def test_if_neg_xy(self):
        with self.assertRaises(ValueError):
            s = Square(2, -6, -8, 9)

    def test_instance_creation(self):
        s = Square(10, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        
    def test_area_calc(self):
        s = Square(7, 7)
        self.assertEqual(s.area(), 49)
    
    def test_str(self):
        s = Square(2, 6, 8, 9)
        self.assertEqual(str(s), "[Square] (9) 6/8 - 2")
    
    def test_dict_rep(self):
        s = Square(2, 6, 8, 9)
        dicts = {'id': 9, 'width': 2, 'height': 2, 'x': 6, 'y': 8}



if __name__ == '__main__':
    unittest.main()