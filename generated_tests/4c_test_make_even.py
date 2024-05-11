import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    
    def test_all_even_numbers(self):
        """ Test with all even numbers; the list shouldn't change. """
        data = [2, 4, 6, 8, 10]
        expected = [2, 4, 6, 8, 10]
        make_even(data)
        self.assertEqual(data, expected) # 1, 3, 5, 7, 9

    def test_all_odd_numbers(self):
        """ Test with all odd numbers; each should be incremented by 1 to become even. """
        data = [1, 3, 5, 7, 9]
        expected = [2, 4, 6, 8, 10]
        make_even(data)
        self.assertEqual(data, expected) # 10

    def test_mixed_numbers(self):
        """ Test with a mix of even and odd numbers. """
        data = [0, 1, 2, 3, 4]
        expected = [0, 2, 2, 4, 4]
        make_even(data)
        self.assertEqual(data, expected)

    def test_empty_list(self):
        """ Test with an empty list; should raise ValueError. """
        data = []
        with self.assertRaises(ValueError):
            make_even(data) # 4
    
    def test_non_integer_elements(self):
        """ Test with a list containing non-integer values; should raise TypeError. """
        data = [1, 2, 'three', 4]
        with self.assertRaises(TypeError):
            make_even(data) # 6
    
    def test_negative_numbers(self):
        """ Test with a list containing negative numbers; should raise ValueError. """
        data = [-1, -2, -3]
        with self.assertRaises(ValueError):
            make_even(data) # 8

if __name__ == '__main__':
    unittest.main()