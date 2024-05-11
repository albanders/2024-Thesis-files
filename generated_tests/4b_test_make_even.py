import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):

    def test_make_even_all_odd(self):
        """Test make_even with all odd numbers. Equivalence class: all odd non-negative integers."""
        numbers = [1, 3, 5]
        make_even(numbers)
        self.assertEqual(numbers, [2, 4, 6]) # 1, 3, 5, 7, 10
        
    def test_make_even_all_even(self):
        """Test make_even with all even numbers. Equivalence class: all even non-negative integers."""
        numbers = [2, 4, 6]
        make_even(numbers)
        self.assertEqual(numbers, [2, 4, 6]) # 9

    def test_make_even_mixed_numbers(self):
        """Test make_even with a mix of odd and even numbers. Equivalence class: mixed even and odd non-negative integers."""
        numbers = [0, 1, 2, 3]
        make_even(numbers)
        self.assertEqual(numbers, [0, 2, 2, 4])

    def test_make_even_empty_list(self):
        """Test make_even with empty list. Equivalence class: empty input list."""
        with self.assertRaises(ValueError):
            make_even([]) # 4

    def test_make_even_non_integer(self):
        """Test make_even with non-integer in list. Equivalence class: non-integer values."""
        with self.assertRaises(TypeError):
            make_even([1, 2, 'three']) # 6

    def test_make_even_negative_numbers(self):
        """Test make_even with negative numbers in list. Equivalence class: negative integers."""
        with self.assertRaises(ValueError):
            make_even([-1, 2, 3]) # 8

if __name__ == '__main__':
    unittest.main()