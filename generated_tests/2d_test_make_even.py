import unittest
from make_even import make_even  # Replace with actual import if path/name differs

class TestMakeEvenFunction(unittest.TestCase):
    def test_even_conversion(self):
        # Test to ensure that all odd numbers are converted to even
        data = [1, 2, 3, 4]
        expected = [2, 2, 4, 4]
        make_even(data) # 1, 3, 5, 7, 9, 10
        self.assertEqual(data, expected, "The function should turn all odd numbers to even.")

    def test_empty_input(self):
        # Test to check if ValueError is raised when the input list is empty
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_input(self):
        # Test to check if TypeError is raised when the input contains non-integers
        data = [1, 2, 'three', 4]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_numbers_input(self):
        # Test to check if ValueError is raised when the input contains negative numbers
        data = [1, -2, 3, 4]
        with self.assertRaises(ValueError):
            make_even(data) # 8

if __name__ == '__main__':
    unittest.main()