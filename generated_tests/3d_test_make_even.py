import unittest
from make_even import make_even

class TestMakeEvenFunction(unittest.TestCase):
    def test_make_even_with_odd_numbers(self):
        # Test with all odd numbers
        data = [1, 3, 5]
        make_even(data) # 1, 3, 5, 7, 10
        self.assertEqual(data, [2, 4, 6])

    def test_make_even_with_even_numbers(self):
        # Test with all even numbers
        data = [2, 4, 6]
        make_even(data) # 9
        self.assertEqual(data, [2, 4, 6])

    def test_make_even_with_mixed_numbers(self):
        # Test with a mix of even and odd numbers
        data = [0, 1, 2, 3]
        make_even(data)
        self.assertEqual(data, [0, 2, 2, 4])

    def test_make_even_with_empty_list(self):
        # Test should raise ValueError if list is empty
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4

    def test_make_even_with_non_integer_elements(self):
        # Test with non-integer elements in list
        data = [1, 'two', 3]
        with self.assertRaises(TypeError):
            make_even(data) # 6

    def test_make_even_with_negative_numbers(self):
        # Test with negative numbers in list
        data = [0, -1, 2]
        with self.assertRaises(ValueError):
            make_even(data) # 8
        
    def test_make_even_with_non_negative_integer(self):
        # Test with all non-negative integers
        data = [0, 2, 10]
        make_even(data)
        self.assertEqual(data, [0, 2, 10])

# To run the tests
if __name__ == '__main__':
    unittest.main()