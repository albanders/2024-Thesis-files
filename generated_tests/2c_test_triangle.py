import unittest
from triangle import triangle  # Assuming the function is defined in triangle.py

class TestTriangleFunction(unittest.TestCase):

    # Test that checks for Equilateral triangle    
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(10.5, 10.5, 10.5), "Equilateral") # 2, 5, 8

    # Test that checks for Isosceles triangle
    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4, 6, 4), "Isosceles")

    # Test that checks for Scalene triangle
    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 3, 4), "Scalene") # 24
        self.assertEqual(triangle(5.5, 6.7, 7.8), "Scalene")

    # Test checks that a TypeError is raised for invalid input types
    def test_input_types(self):
        with self.assertRaises(TypeError): # 3
            triangle("a", 2, 3)
        with self.assertRaises(TypeError): # 6
            triangle(1.5, "b", 3)

    # Test checks for zero or negative side values
    def test_non_positive_side_values(self):
        with self.assertRaises(ValueError): # 13
            triangle(0, 1, 2)
        with self.assertRaises(ValueError):
            triangle(-1, 1, 1)

    # Test that checks the triangle inequality theorem
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError): # 19
            triangle(1, 2, 3)
        with self.assertRaises(ValueError): # 20
            triangle(2, 9, 5)

if __name__ == "__main__":
    unittest.main()