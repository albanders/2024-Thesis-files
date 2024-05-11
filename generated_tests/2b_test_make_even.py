import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):

    def test_make_all_numbers_even(self):
        # Test to ensure all odd numbers are incremented by 1 to make them even
        data = [1, 2, 3, 4, 5]
        expected = [2, 2, 4, 4, 6]
        make_even(data)
        self.assertEqual(data, expected) # 1, 3, 5, 7, 9, 10

    def test_empty_list(self):
        # Test that an empty list raises a ValueError
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_elements(self):
        # Test that a list with non-integer elements raises a TypeError
        data = [1, 2, 'three', 4]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_numbers(self):
        # Test that a list including negative numbers raises a ValueError
        data = [1, 2, -3, 4]
        with self.assertRaises(ValueError):
            make_even(data) # 8

    def test_already_even_numbers(self):
        # Test that a list of even numbers is unchanged
        data = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        make_even(data)
        self.assertEqual(data, expected)

    def test_all_odd_numbers(self):
        # Test that all odd numbers gets incremented to become even
        data = [1, 3, 5, 7]
        expected = [2, 4, 6, 8]
        make_even(data)
        self.assertEqual(data, expected)

    def test_mixed_types_raises_error(self):
        # Test that a list including non-integer types alongside integers raises TypeError
        data = [1, 'two', 3.4, None]
        with self.assertRaises(TypeError):
            make_even(data)

    def test_negative_and_positive_mixed(self):
        # Test that mixing negative and positive numbers raises ValueError
        data = [0, 1, -2, 3]
        with self.assertRaises(ValueError):
            make_even(data)

    def test_zero_and_positive(self):
        # Test changing zero (even) and positive odd numbers
        data = [0, 1, 3]
        expected = [0, 2, 4]
        make_even(data)
        self.assertEqual(data, expected)

    def test_single_odd_number(self):
        # Test with a single odd number
        data = [3]
        expected = [4]
        make_even(data)
        self.assertEqual(data, expected)

# This allows the test cases to be run from the command line
if __name__ == '__main__':
    unittest.main()