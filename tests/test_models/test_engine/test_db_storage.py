#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models import storage_type

from models.state import State


class test_dbstorage(unittest.TestCase):
    """ Class to test the db storage method """
    @unittest.skipIf(storage_type != 'db', 'not using db storage')
    def test_all(self):
        """ correct data type is properly returned """
        BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(storage_type != 'db', 'not using db storage')
    def test_get(self):
        """test get object by id"""
        state = State(name='test_state')
        state.save()
        get_state = storage.get(State, state.id)
        self.assertEqual(state, get_state)

    @unittest.skipIf(storage_type != 'db', 'not using db storage')
    def test_count(self):
        """test count of objects in storage"""
        self.assertEqual(len(storage.all()), storage.count())
        state = State(name='test_state')
        state.save()
        self.assertEqual(len(storage.all()), storage.count())
