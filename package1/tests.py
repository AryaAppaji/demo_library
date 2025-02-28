import unittest
from .math_module import BasicMath
from .exceptions import InvalidValueException


class TestMath(unittest.TestCase):
    def test_add(self):
        bm = BasicMath()
        self.assertEqual(bm.add(10, 15), 25)
    
    def test_subtract(self):
        bm = BasicMath()
        self.assertEqual(bm.subtract(10, 15), -5)

    def test_multiply(self):
        bm = BasicMath()
        self.assertEqual(bm.multiply(10, 20), 200)

    def test_divide(self):
        bm = BasicMath()
        self.assertEqual(bm.divide(100, 10), 10.0)
        
    def test_divide_exception(self):
        bm = BasicMath()
        with self.assertRaises(InvalidValueException):
            bm.divide(5, 0)