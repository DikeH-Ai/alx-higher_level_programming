#!/usr/bin/python3
"""
Defines unitests for rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_instance_width(unittest.TestCase):
    """unittests for testing rectangle width attribute."""

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("thisisus", 2)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.1, 1)

class test_instance_int(unittest.TestCase):
    """unittests for testing instantiation"""
    def test_noargs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_double_parameters(self):
        rec1 = Rectangle(20, 4)
        rec2 = Rectangle(4, 20)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_single_parameter(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_three_args(self):
        rec1 = Rectangle(1, 1, 2)
        rec2 = Rectangle(2, 2, 1)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_is_base(self):
        self.assertIsInstance(Rectangle(12, 2), Base)

class TestRectangle_height(unittest.TestCase):
    """unittests for testing initialization of rectangle."""

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "thisisus")
    
    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, 5.1)