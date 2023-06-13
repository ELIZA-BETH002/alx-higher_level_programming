#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test when the list is empty"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test when the list contains a single element"""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_positive_numbers(self):
        """Test when the list contains positive numbers"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """Test when the list contains negative numbers"""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test when the list contains mixed positive and negative numbers"""
        result = max_integer([-1, 2, -3, 4])
        self.assertEqual(result, 4)

    def test_duplicate_numbers(self):
        """Test when the list contains duplicate numbers"""
        result = max_integer([1, 2, 2, 4])
        self.assertEqual(result, 4)

    def test_large_numbers(self):
        """Test when the list contains large numbers"""
        result = max_integer([10**9, 10**10, 10**11])
        self.assertEqual(result, 10**11)

if __name__ == __main__:
    unittest.main()
