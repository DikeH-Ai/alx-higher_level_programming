#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        dlist = [52, 3, 23, 5, 3, 8]
        self.assertEqual(max_integer(dlist), 52)
        clist = [1, 2, 3, 4, 44]
        self.assertEqual(max_integer(clist), 44)
        alist = [5, 17, 2]
        self.assertEqual(max_integer(alist), 17)

    def test_negative(self):
        dlist = [-1, 4, 8]
        self.assertEqual(max_integer(dlist), 8)
        clist = [-43, -3, -17]
        self.assertEqual(max_integer(clist), -3)

    def test_one_element(self):
        dlist = [12]
        self.assertEqual(max_integer(dlist), 12)

    def test_emptylist(self):
        dlist = []
        self.assertEqual(max_integer(dlist), None)
