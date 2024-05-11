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

   def Test_Valid(self):
      List = [0,1,2,3]
      make_even(List)
      self.assertEqual(List, [0,2,2,4])

   def Test_Invalid(self):
      with self.assertRaises(TypeError):
         make_even(["a","b","c"])

   def Test_Empty(self):
      with self.assertRaises(ValueError):
         make_even([])
   def Test_Negative(self):
      with self.assertRaises(ValueError):
         make_even([-1,-5])

if __name__ == "__main__":
    unittest.main()
