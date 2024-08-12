#!/usr/bin/python3
""" """
import unittest
from models import storage_type
from models.state import State


class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)
