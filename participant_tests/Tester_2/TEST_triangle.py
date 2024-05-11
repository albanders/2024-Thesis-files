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
    def test_name(self):
        self.assertEqual(triangle(2, 2, 2), 'Equilateral')
        self.assertEqual(triangle(4, 4, 2), 'Isosceles')
        self.assertEqual(triangle(2, 3, 4), 'Scalene')

    def test_numbers(self):
        with self.assertRaises(TypeError):
            triangle(1, "2", 3.2)
            triangle(1.23, 2.33, 2)

    def test_numbnonzero(self):
        with self.assertRaises(ValueError):
            triangle(0, -1, 3)
            triangle(1, 2, 3)

    def test_equ(self):
        with self.assertRaises(ValueError):
            triangle(2, 2, 4)

if __name__ == "__main__":
    unittest.main()
