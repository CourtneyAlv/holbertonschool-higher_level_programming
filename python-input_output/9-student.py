#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """represents a student"
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of the student
            """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
            }
