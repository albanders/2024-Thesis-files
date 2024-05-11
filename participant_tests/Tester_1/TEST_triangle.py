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
   def test_correct(self):
      self.assertEqual(triangle(2,2,2), "Equilateral")
      self.assertEqual(triangle(2.1,2.1,2.1), "Equilateral")
      self.assertEqual(triangle(2,2,1), "Isosceles")
      self.assertEqual(triangle(2,3,4), "Scalene")
      
   
   def test_incorrect_value(self):
      with self.assertRaises(ValueError):
         triangle(1,2,3)
      with self.assertRaises(ValueError):
         triangle(-1,2,3)


   def incorrect_datatype(self):
      with self.assertRaises(TypeError):
         triangle("a",3,4)
      with self.assertRaises(TypeError):
         triangle(2,"b",4)
      with self.assertRaises(TypeError):
         triangle(2,3,"c")



   
      
       



if __name__ == "__main__":
    unittest.main()
