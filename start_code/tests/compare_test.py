import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))
    
    def test_compare_7_7_returns_7_is_equal_to_7(self):
        self.assertEqual("7 is equal to 7", compare(7, 7))
    
