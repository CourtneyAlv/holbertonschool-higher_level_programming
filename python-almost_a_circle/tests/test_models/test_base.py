#!/usr/bin/python3
"""Defines unittests for base.py"""
import unittest
from models.base import Base


class TestBase_create(unittest.TestCase):
    """Unittests for testing of the Base class"""

    def test_create_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

class TestBase_instantiation(unittest.TestCase):

    def test_instance_create_id(self):
        instance = Base(12)
        self.assertEqual(instance.id, 12)

    def test_instance_without_id(self):
        instance = Base()
        self.assertIsNotNone(instance.id, 12)

class TestBase_to_json_string(unittest.TestCase):

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_nonempty(self):
        data = [{"id": 1, "name": "Courtney"}, {"id": 2, "name": "Pancake"}]
        json_str = Base.to_json_string(data)
        self.assertEqual(json_str, '[{"id": 1, "name": "Courtney"}, {"id": 2, "name": "Pancake"}]')
    
