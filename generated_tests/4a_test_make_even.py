import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    def test_valid_input(self):
        """Test with a valid list containing both odd and even non-negative integers."""
        data = [0, 1, 2, 3, 4]
        expected = [0, 2, 2, 4, 4]
        make_even(data) # 1, 3, 5, 7, 9, 10
        self.assertEqual(data, expected, "The function should modify odd numbers to even.")

    def test_empty_list(self):
        """Test input with an empty list should raise ValueError."""
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_input(self):
        """Test input containing non-integer types should raise TypeError."""
        data = [0, 1, "two", 3]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_integer_input(self):
        """Test input containing negative integers should raise ValueError."""
        data = [0, 1, -2, 3]
        with self.assertRaises(ValueError):
            make_even(data) # 8

if __name__ == "__main__":
    unittest.main()