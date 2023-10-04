#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

class Testbase(unittest.TestCase):

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_instance_create_id(self):
        instance = Base(12)
        self.assertEqual(instance.id, 12)

    def test_dictionary(self):
        dictionary = {'id': 10}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 10)
