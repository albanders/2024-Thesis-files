import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):

    def test_make_even_all_even_numbers(self):
        # Equivalence Partition: All numbers even
        numbers = [2, 4, 6, 8]
        make_even(numbers) # 1, 3, 5, 7, 9
        self.assertEqual(numbers, [2, 4, 6, 8], "Should not change even numbers")

    def test_make_even_all_odd_numbers(self):
        # Equivalence Partition: All numbers odd
        numbers = [1, 3, 5, 7]
        make_even(numbers) # 10
        self.assertEqual(numbers, [2, 4, 6, 8], "Should change all odd numbers to even")

    def test_make_even_mixed_numbers(self):
        # Equivalence Partition: Mixed numbers
        numbers = [0, 1, 2, 3]
        make_even(numbers)
        self.assertEqual(numbers, [0, 2, 2, 4], "Odd numbers should be incremented by 1")

    def test_make_even_empty_list(self):
        # Boundary Value: Empty list
        numbers = []
        with self.assertRaises(ValueError):
            make_even(numbers) # 4

    def test_make_even_non_integer(self):
        # Equivalence Partition: Non-integer values
        numbers = [1, 2, 3.5, 4]
        with self.assertRaises(TypeError):
            make_even(numbers) # 6

    def test_make_even_negative_numbers(self):
        # Equivalence Partition: Negative numbers
        numbers = [0, -1, -2, 3]
        with self.assertRaises(ValueError):
            make_even(numbers) # 8

    def test_make_even_large_numbers(self):
        # Additional Test: Large numbers
        numbers = [9999, 10000, 10001, 10002]
        make_even(numbers)
        self.assertEqual(numbers, [9999, 10000, 10002, 10002], "Should correctly make odd very large integers even")

    def test_make_even_single_odd(self):
        # Boundary Value: Single odd value
        numbers = [7]
        make_even(numbers)
        self.assertEqual(numbers, [8], "Single odd value should be incremented by 1")

    def test_make_even_single_even(self):
        # Boundary Value: Single even value
        numbers = [8]
        make_even(numbers)
        self.assertEqual(numbers, [8], "Single even value should remain unchanged")


if __name__ == "__main__":
    unittest.main()