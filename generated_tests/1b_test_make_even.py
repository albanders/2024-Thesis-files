import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):

    def test_even_conversion(self):
        """ Test if odd numbers in the list are converted to even. """
        data = [1, 2, 3, 4, 5]
        expected = [2, 2, 4, 4, 6]
        make_even(data) # 1, 3, 5, 7, 9, 10
        self.assertEqual(data, expected, "Should convert all odd numbers to even by adding 1.")
    
    def test_empty_list(self):
        """ Test if passing an empty list raises a ValueError. """
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_elements(self):
        """ Test if passing a list with non-integer elements raises a TypeError. """
        data = [1, '2', 3]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_numbers(self):
        """ Test if passing a list with negative numbers raises a ValueError. """
        data = [1, -2, 3]
        with self.assertRaises(ValueError):
            make_even(data) # 8
    
    def test_all_even_numbers(self):
        """ Test if passing all even numbers keeps them the same. """
        data = [2, 4, 6]
        expected = [2, 4, 6]
        make_even(data)
        self.assertEqual(data, expected, "Even numbers should remain unchanged.")
    
    def test_return_value(self):
        """ Test if the function returns None. """
        data = [1, 3, 5]
        result = make_even(data)
        self.assertIsNone(result, "Function should return None.")

if __name__ == "__main__":
    unittest.main()