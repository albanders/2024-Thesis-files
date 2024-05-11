import unittest

from triangle import triangle

"""
Import "triangle" from triangle.py and create unit tests in Python using the
unittest module to verify these requirements:

1. The function "triangle" receives three numbers as inputs, representing the
   sides of a triangle. It returns a name of the type of triangle:
   "Equilateral", "Isosceles" or "Scalene".
2. All input numbers must be either integer or float, else a TypeError is
   raised.
3. If all input numbers are of equal length, the function returns "Equilateral".
4. If two input numbers are of equal length, the function returns "Isosceles".
5. If no input numbers are of equal length, the function returns "Scalene".
6. All input numbers must be greater than zero, else a ValueError is raised.
7. If one number is equal to or greater than the sum of the other two, a
   ValueError is raised. (Hint: look-up "triangle inequality")
"""

class TestTriangle(unittest.TestCase):
   def test_write_result(self):
      self.assertEqual(triangle(6,6,6), "Equilateral")
      self.assertEqual(triangle(6,6,8), "Isosceles")
      self.assertEqual(triangle(6,5,3), "Scalene")

   def test_variety_TypeError(self):
      with self.assertRaises(TypeError):
         triangle('Axel',8,8)
         triangle(9.5,8,8)

   def test_variety_ValueError(self):
      with self.assertRaises(ValueError):
         triangle(0,8,8)
         triangle(-10,8,8)

   def test_variety_ValueError_inequality(self):
      with self.assertRaises(ValueError):
         triangle(16,8,8)
         triangle(18,8,8)
if __name__ == "__main__":
    unittest.main()
