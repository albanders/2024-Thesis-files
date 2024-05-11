import unittest

from make_even import make_even

"""
Import "make_even" from make_even.py and create unit tests in Python using the
unittest module to verify these requirements:

1. The function "make_even" receives a list of numbers as input. It changes
   the input list by adding 1 to every odd number, and then returns None.
2. The input list must not be empty, else a ValueError is raised.
3. All numbers in the input list must be integers, else a TypeError is raised.
4. All numbers in the input list must be non-negative (>= 0), else a
   ValueError is raised.
"""

class TestMakeEven(unittest.TestCase):
    def test_return(self):
        num = [1, 2, 3]
        make_even(num)
        self.assertEqual(num, [2, 2, 4])
        self.assertEqual(make_even([1, 2, 3]), None)

    def test_error(self):
        with self.assertRaises(ValueError):
            make_even([])

    def test_allint(self):
        with self.assertRaises(TypeError):
            make_even([1, 2, 3, "4", 5])
    
    def test_noneg(self):
        with self.assertRaises(ValueError):
            make_even([-1, 2, -3, 4])

if __name__ == "__main__":
    unittest.main()
