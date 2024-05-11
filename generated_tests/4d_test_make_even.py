import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    def test_non_empty_all_even_numbers(self):
        input_list = [2, 4, 6]
        expected_list = [2, 4, 6]
        make_even(input_list) # 1, 3, 5, 7, 9
        self.assertEqual(input_list, expected_list, "Should not modify even numbers.")

    def test_non_empty_all_odd_numbers(self):
        input_list = [1, 3, 5]
        expected_list = [2, 4, 6]
        make_even(input_list) # 10
        self.assertEqual(input_list, expected_list, "Should convert all odd numbers to even.")

    def test_non_empty_mixed_numbers(self):
        input_list = [0, 1, 2, 3]
        expected_list = [0, 2, 2, 4]
        make_even(input_list)
        self.assertEqual(input_list, expected_list, "Should correctly handle mixed numbers list.")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            make_even([]) # 4

    def test_contains_non_integer(self):
        with self.assertRaises(TypeError):
            make_even([1, 2, 'a', 3]) # 6

    def test_contains_negative_number(self):
        with self.assertRaises(ValueError):
            make_even([1, -1, 2]) # 8

    def test_all_zeros(self):
        input_list = [0, 0, 0]
        expected_list = [0, 0, 0]
        make_even(input_list)
        self.assertEqual(input_list, expected_list, "Zeros are already even and should remain unchanged.")

if __name__ == '__main__':
    unittest.main()