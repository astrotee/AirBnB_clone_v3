#!/usr/bin/python3
""" """
import unittest
from models import storage_type
from models.review import Review


class test_review(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.place_id, None)
        else:
            self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.user_id, None)
        else:
            self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.text, None)
        else:
            self.assertEqual(type(new.text), str)
