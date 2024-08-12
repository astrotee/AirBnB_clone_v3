#!/usr/bin/python3
""" """
import unittest
from models import storage_type
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.name, None)
        else:
            self.assertEqual(type(new.name), str)
