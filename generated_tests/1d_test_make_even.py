import unittest
from make_even import make_even  # Import the make_even function from make_even.py

class TestMakeEven(unittest.TestCase):
    def test_empty_list(self):
        """ Test input with an empty list should raise ValueError. """
        with self.assertRaises(ValueError):
            make_even([]) # 4

    def test_non_integer_elements(self):
        """ Test input with non-integer elements should raise TypeError. """
        with self.assertRaises(TypeError):
            make_even([1, 2, '3', 4]) # 6

    def test_negative_numbers(self):
        """ Test input with negative numbers should raise ValueError. """
        with self.assertRaises(ValueError):
            make_even([1, -2, 3]) # 8

    def test_all_even_numbers(self):
        """ Test input with all even numbers should remain unchanged. """
        data = [2, 4, 6, 8]
        make_even(data)
        self.assertEqual(data, [2, 4, 6, 8]) # 1, 3, 5, 7, 9

    def test_all_odd_numbers(self):
        """ Test input with all odd numbers should be incremented by 1. """
        data = [1, 3, 5]
        make_even(data)
        self.assertEqual(data, [2, 4, 6]) # 10

    def test_mixed_numbers(self):
        """ Test input with a mix of odd and even numbers. """
        data = [1, 2, 3, 4]
        make_even(data)
        self.assertEqual(data, [2, 2, 4, 4])

    def test_no_side_effects(self):
        """ Ensure the function returns None. """
        data = [1, 2, 3]
        result = make_even(data)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()