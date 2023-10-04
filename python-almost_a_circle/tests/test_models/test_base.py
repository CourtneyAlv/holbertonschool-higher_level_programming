#!/usr/bin/python3

import unittest
from models.base import Base


class Testbase(unittest.TestCase):

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_instance_create_id(self):
        instance = Base(12)
        self.assertEqual(instance.id, 12)
