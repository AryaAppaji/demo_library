import unittest
from .string_operations import StringOperations

class TestStringOperations(unittest.TestCase):
    def test_string_concat(self):
        strop = StringOperations()
        self.assertEqual(strop.concatenate("Hello", "World"), "HelloWorld")
    
    def test_string_repeat(self):
        strop = StringOperations()
        self.assertEqual(strop.repeat("*", 5), "*****")