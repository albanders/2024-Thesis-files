import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    def test_even_conversion(self):
        """Test if all odd numbers are converted to even by adding 1 and even numbers remain unchanged."""
        data = [1, 2, 3, 4, 5]
        make_even(data) # 1, 3, 5, 7, 9, 10
        self.assertEqual(data, [2, 2, 4, 4, 6], "Odd numbers should be converted to even")

    def test_empty_list(self):
        """Test that passing an empty list raises ValueError."""
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_elements(self):
        """Test that a list with non-integer elements raises TypeError."""
        data = [1, 2, 'three', 4]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_numbers(self):
        """Test that a list with negative numbers raises ValueError."""
        data = [1, -2, 3]
        with self.assertRaises(ValueError):
            make_even(data) # 8

    def test_non_negative_even_numbers(self):
        """Test that non-negative even numbers are unchanged."""
        data = [0, 2, 4, 6]
        original_data = data.copy()
        make_even(data)
        self.assertEqual(data, original_data, "Non-negative even numbers should remain unchanged")

    def test_edge_cases(self):
        """Test edge cases including the minimum integer value and the boundary condition of 0."""
        data = [0, 1, 0]
        make_even(data)
        self.assertEqual(data, [0, 2, 0], "Boundary case of zero should be handled correctly.")

# This allows the test cases to be run directly by the script.
if __name__ == '__main__':
    unittest.main()