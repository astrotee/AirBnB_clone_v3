#!/usr/bin/python3
""" """
import unittest
from models import storage_type
from models.city import City


class test_City(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.state_id, None)
        else:
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)
