#!/usr/bin/python3
""" """
import unittest
from models import storage_type
from models.user import User


class test_User(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.first_name, None)
        else:
            self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.last_name, None)
        else:
            self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.email, None)
        else:
            self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        if storage_type == 'db':
            self.assertEqual(new.password, None)
        else:
            self.assertEqual(type(new.password), str)
