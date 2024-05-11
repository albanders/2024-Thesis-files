import unittest
from make_even import make_even

class TestMakeEven(unittest.TestCase):
    def test_all_even_numbers(self):
        data = [2, 4, 6, 8]
        expected = [2, 4, 6, 8]
        make_even(data) # 1, 3, 5, 7, 9
        self.assertEqual(data, expected, "Should not change even numbers")
        
    def test_all_odd_numbers(self):
        data = [1, 3, 5, 7]
        expected = [2, 4, 6, 8]
        make_even(data) # 10
        self.assertEqual(data, expected, "Should make all numbers even")
        
    def test_mixed_numbers(self):
        data = [0, 1, 2, 3]
        expected = [0, 2, 2, 4]
        make_even(data)
        self.assertEqual(data, expected, "Should handle mixed numbers properly")
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            make_even([]) # 4
    
    def test_contains_non_integers(self):
        with self.assertRaises(TypeError):
            make_even([1, 'two', 3.5, True]) # 6
    
    def test_contains_negative_numbers(self):
        with self.assertRaises(ValueError): # 8
            make_even([1, -2, 3, -4])

# Running the tests
if __name__ == "__main__":
    unittest.main()