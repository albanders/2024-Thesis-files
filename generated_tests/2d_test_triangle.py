# Assuming the file triangle.py exists and has a triangle function in it
from triangle import triangle
import unittest

class TestTriangleFunction(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        """Tests that three equal sides return 'Equilateral'."""
        self.assertEqual(triangle(2, 2, 2), 'Equilateral') # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22

    def test_isosceles_triangle(self):
        """Tests that exactly two equal sides return 'Isosceles'."""
        self.assertEqual(triangle(2, 2, 3), 'Isosceles') # 23
        self.assertEqual(triangle(3, 2, 2), 'Isosceles')
        self.assertEqual(triangle(2, 3, 2), 'Isosceles')

    def test_scalene_triangle(self):
        """Tests that three different sides return 'Scalene'."""
        self.assertEqual(triangle(2, 3, 4), 'Scalene') # 24

    def test_type_error_with_non_numbers(self):
        """Tests that non-number inputs raise a TypeError."""
        with self.assertRaises(TypeError): # 3
            triangle('a', 2, 2)
        with self.assertRaises(TypeError):
            triangle(1, 'b', 3) # 6

    def test_value_error_for_non_positive_sides(self):
        """Tests that sides <= 0 raise a ValueError."""
        with self.assertRaises(ValueError):
            triangle(-1, 2, 2) # 13
        with self.assertRaises(ValueError):
            triangle(0, 2, 2)

    def test_value_error_for_invalid_triangles(self):
        """Tests that invalid triangles (one side >= sum of others) raise a ValueError."""
        with self.assertRaises(ValueError):
            triangle(5, 1, 1) # 21
        with self.assertRaises(ValueError):
            triangle(1, 5, 1) # 20
        with self.assertRaises(ValueError):
            triangle(1, 1, 5) # 19

if __name__ == '__main__':
    unittest.main()