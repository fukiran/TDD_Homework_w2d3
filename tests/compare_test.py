import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))


    def test_compare_3_5_returns_5_is_greater_than_1(self):
        self.assertEqual("3 is les than 5",compare(3, 5))


    def test_compare_10_10_return_equal(self):
        self.assertEqual("both numbers are equal",compare(10, 10))