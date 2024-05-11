# Assuming this test file is saved in the same directory where triangle.py is located with the triangle function
import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):

    # Test Equilateral Triangle
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(7.0, 7.0, 7.0), "Equilateral") # 2, 5, 8

    # Test Isosceles Triangle
    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4, 5, 5), "Isosceles")
        self.assertEqual(triangle(8.0, 8.0, 5.0), "Isosceles")

    # Test Scalene Triangle
    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 3, 4), "Scalene") # 24
        self.assertEqual(triangle(5.5, 6.6, 7.7), "Scalene")

    # Test Triangle Inequality Theorem
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
            triangle(2, 1, 5)

    # Test Input Types
    def test_input_types(self):
        with self.assertRaises(TypeError):
            triangle("a", 2, 3) # 3
            triangle(1.0, "b", 3) # 6
            triangle(1, 2, [1, 2, 3]) # 9

    # Test Negative Side Lengths
    def test_negative_side_lengths(self):
        with self.assertRaises(ValueError):
            triangle(-1, 2, 2) # 13
            triangle(3, -3, 3) # 14 
            triangle(3, 4.5, -6) # 15

    # Additional scenario for zero side length
    def test_zero_side_lengths(self):
        with self.assertRaises(ValueError):
            triangle(0, 2, 2)
            triangle(3, 0, 3)
            triangle(3, 4, 0)

if __name__ == "__main__":
    unittest.main()