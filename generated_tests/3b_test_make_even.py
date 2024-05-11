import unittest
from make_even import make_even

class TestMakeEvenFunction(unittest.TestCase):

    def test_even_and_odd_numbers(self):
        # Ideally this should cover values around boundaries like -1, 0, and 1
        data = [1, 2, 3, 4, 5, 6]
        expected = [2, 2, 4, 4, 6, 6]
        make_even(data) # 1, 3, 5, 7, 9, 10
        self.assertEqual(data, expected)

    def test_all_even_numbers(self):
        data = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        make_even(data)
        self.assertEqual(data, expected)

    def test_all_odd_numbers(self):
        data = [1, 3, 5]
        expected = [2, 4, 6]
        make_even(data)
        self.assertEqual(data, expected)

    def test_zero_and_near_zero(self):
        data = [0, -1, 2]
        with self.assertRaises(ValueError):
            make_even(data) # 8
        data = [0]
        expected = [0]
        make_even(data)
        self.assertEqual(data, expected)

    def test_empty_list(self):
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_non_integer_elements(self):
        data = [1, 'two', 3]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_negative_numbers(self):
        data = [-2, -3, -4]
        with self.assertRaises(ValueError):
            make_even(data)

    def test_return_value(self):
        data = [1, 3, 5]
        result = make_even(data)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()