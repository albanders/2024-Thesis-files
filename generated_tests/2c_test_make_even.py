import unittest
from make_even import make_even  # Import the required function from the module

class TestMakeEven(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError): # 4
            make_even([])  # Expecting a ValueError for empty list

    def test_incorrect_types(self):
        with self.assertRaises(TypeError): # 6
            make_even([1, 2, '3', 4])  # Mix of integers and a string

    def test_negative_numbers(self):
        with self.assertRaises(ValueError): # 8
            make_even([-1, 2, 3])  # Including a negative integer

    def test_all_even_numbers(self):
        numbers = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        make_even(numbers) # 1, 3, 5, 7, 9
        self.assertEqual(numbers, expected)  # Confirm that list remains unchanged

    def test_all_odd_numbers(self):
        numbers = [1, 3, 5, 7]
        expected = [2, 4, 6, 8]
        make_even(numbers) # 10
        self.assertEqual(numbers, expected)  # Each odd number should be incremented by 1

    def test_mixed_numbers(self):
        numbers = [0, 1, 2, 3]
        expected = [0, 2, 2, 4]
        make_even(numbers)
        self.assertEqual(numbers, expected)  # Verify both odd and even handling

    def test_non_negative_requirement(self):
        numbers = [0, 2, 4, 6]
        expected = [0, 2, 4, 6]
        make_even(numbers)
        self.assertEqual(numbers, expected)  # Edge case: including zero

    def test_integer_type_requirement(self):
        numbers = [0, 2.5, 4, 6]  # Including a float
        with self.assertRaises(TypeError):
            make_even(numbers)

if __name__ == '__main__':
    unittest.main()