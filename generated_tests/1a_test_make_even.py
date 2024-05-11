import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    def test_make_even_odd_numbers(self):
        numbers = [1, 3, 5]
        make_even(numbers) # 1, 3, 5, 7, 10
        self.assertEqual(numbers, [2, 4, 6], "The function should make all numbers even")

    def test_make_even_mixed_numbers(self):
        numbers = [0, 1, 2, 3]
        make_even(numbers) # 9
        self.assertEqual(numbers, [0, 2, 2, 4], "The function should correctly handle a mix of even and odd numbers")

    def test_make_even_no_change_needed(self):
        numbers = [2, 4, 6]
        make_even(numbers)
        self.assertEqual(numbers, [2, 4, 6], "The function should leave even numbers unchanged")

    def test_make_even_empty_list(self):
        with self.assertRaises(ValueError, msg="The function should raise ValueError if the list is empty"):
            make_even([]) # 4

    def test_make_even_non_integers(self):
        with self.assertRaises(TypeError, msg="The function should raise TypeError if any element is not an integer"):
            make_even([1, 3.5, 2]) # 6

    def test_make_even_negative_numbers(self):
        with self.assertRaises(ValueError, msg="The function should raise ValueError if any number is negative"):
            make_even([1, -1, 3]) # 8

if __name__ == "__main__":
    unittest.main()