#!/usr/bin/python3

"""
Defines unitests for base.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """testing instantiation of Base class."""

    def test_no_argument(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_base_triple(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_No_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_personal(self):
        self.assertEqual(8, Base(8).id)

    def test_id_public(self):
        base1 = Base(5)
        base1.id = 12
        self.assertEqual(12, base1.id)
