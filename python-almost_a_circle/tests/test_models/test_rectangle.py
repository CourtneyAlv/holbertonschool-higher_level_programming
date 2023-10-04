#!/usr/bin/python3
"""Unittest for recatangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_instance_creation(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_if_integer(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 'five')

    def test_if_neg(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -3)

    def test_if_int_xy(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 4, "six", "eight", "nine")

    def test_if_neg_xy(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2, 4, -6, -8, -9)

    def test_area_calc(self):
        r = Rectangle(7, 4)
        self.assertEqual(r.area(), 28)

    def test_str(self):
        r = Rectangle(2, 4, 6, 8, 9)
        self.assertEqual(str(r), "[Rectangle] (9) 6/8 - 2/4")

    def test_dict_rep(self):
        r = Rectangle(2, 4, 6, 8, 9)
        dicts = {'id': 9, 'width': 2, 'height': 4, 'x': 6, 'y': 8}

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_two_args(self):
        r1 = Rectangle(7, 4)
        r2 = Rectangle(4, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(7, 7, 5)
        r2 = Rectangle(5, 5, 7)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_four_args(self):
        r1 = Rectangle(7, 6, 5, 4)
        r2 = Rectangle(4, 5, 6, 7)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_five_args(self):
        self.assertEqual(7, Rectangle(13, 2, 3, 3, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(13, 2, 3, 3, 7, 8)

class TestRectangle_width(unittest.TestCase):
    """**Unittests for testing initialization of Rectangle width attribute""" 
    
    def test_None_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (None, 2)
    
    def test_str_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle ("invalid", 2)
    
    def test_float_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (5.5, 1) 
    
    def test_complex_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle (complex(5), 2)
    
    def test_dict_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle({"a": 1, "b": 21}, 2) 
    
    def test_list_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle ([1, 2, 3], 2) 
    
    def test_set_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle ((1, 2, 3), 2) 
    
    def test_tuple_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle ( (1, 2, 3), 2) 
    
    def test_frozenset_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (frozenset ({1, 2, 3, 11}), 2) 
    
    def test_range_width(self) : 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (range (5), 2) 
    
    def test_bytes_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (b' Python', 2) 
    
    def test_memoryview_width(self): 
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            Rectangle (memoryview (b' abcedg' ) , 2) 



if __name__ == "__main__":
    unittest.main()
