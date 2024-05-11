# # make_even.py
# # This file should have the make_even function implemented as described.

# def make_even(numbers):
    # if not numbers:
        # raise ValueError("The input list must not be empty.")
    
    # for num in numbers:
        # if not isinstance(num, int):
            # raise TypeError("All numbers in the input list must be integers.")
        # if num < 0:
            # raise ValueError("All numbers in the input list must be non-negative.")
    
    # for i in range(len(numbers)):
        # if numbers[i] % 2 != 0:
            # numbers[i] += 1


# test_make_even.py
import unittest
from make_even import make_even

class TestMakeEvenFunction(unittest.TestCase):

    def test_make_numbers_even(self):
        input_list = [1, 2, 3, 4, 5]
        make_even(input_list)
        self.assertEqual(input_list, [2, 2, 4, 4, 6]) # 1, 3, 5, 7, 9, 10

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            make_even([]) # 4

    def test_non_integer_raises_type_error(self):
        with self.assertRaises(TypeError):
            make_even([1, 2, '3', 4]) # 6

    def test_negative_numbers_raises_value_error(self):
        with self.assertRaises(ValueError):
            make_even([0, 1, -2, 3]) # 8
    
    def test_no_modification_needed(self):
        input_list = [2, 4, 6, 8]
        make_even(input_list)
        self.assertEqual(input_list, [2, 4, 6, 8])

    def test_all_odd_numbers(self):
        input_list = [1, 3, 5, 7]
        make_even(input_list)
        self.assertEqual(input_list, [2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()