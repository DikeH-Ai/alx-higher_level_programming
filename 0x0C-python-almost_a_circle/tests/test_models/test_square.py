#!/usr/bin/python3
"""
Defines unitests for square.py
"""
import unittest
from models.base import Base
from models.square import Square


class test_size(unittest.TestCase):
    """Unittest for testing square size"""

    def test_size_invalid(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Thisisus")

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(["htw", "home", "depo"])

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(6.5)


class test_init_class(unittest.TestCase):
    def test_doubele_instance(self):
        sq1 = Square(18, 3)
        sq2 = Square(3, 18)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_single_instance(self):
        sq1 = Square(5)
        sq2 = Square(10)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_base_instance(self):
        self.assertIsInstance(Square(5), Base)

    def test_rectangle_insatnce(self):
        self.assertIsInstance(Square(4), Square)

    def test_pass_None(self):
        with self.assertRaises(TypeError):
            Square()


if __name__ == "__main__":
    unittest.main()
