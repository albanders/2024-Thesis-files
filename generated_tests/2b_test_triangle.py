import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):

    def test_equilateral_triangle(self):
        # This test checks for equilateral triangles (requirement 3)
        self.assertEqual(triangle(3, 3, 3), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(10.0, 10.0, 10.0), "Equilateral") # 2, 5, 8

    def test_isosceles_triangle(self):
        # This test checks for isosceles triangles (requirement 4)
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4.5, 4.5, 9), "Isosceles")

    def test_scalene_triangle(self):
        # This test checks for scalene triangles (requirement 5)
        self.assertEqual(triangle(3, 4, 5), "Scalene") # 24
        self.assertEqual(triangle(5.5, 6.5, 7.5), "Scalene")

    def test_invalid_input_types(self):
        # This test ensures TypeError is raised with invalid input types (requirement 2)
        with self.assertRaises(TypeError):
            triangle("3", 4, 5) # 3
        with self.assertRaises(TypeError):
            triangle(3, [4], 5) # 6
        with self.assertRaises(TypeError):
            triangle(3, 4, None) # 9

    def test_invalid_input_values(self):
        # This test ensures ValueError is raised with zero or negative sides (requirement 6)
        with self.assertRaises(ValueError):
            triangle(0, 1, 1) # 13
        with self.assertRaises(ValueError):
            triangle(-1, 2, 2)
        with self.assertRaises(ValueError):
            triangle(1, 1, -1) # 15

    def test_triangle_inequality(self):
        # This test ensures that triangle inequality is verified (requirement 7)
        with self.assertRaises(ValueError): # 19
            triangle(1, 2, 3)   # Not satisfying triangle inequality
        with self.assertRaises(ValueError): # 21
            triangle(10, 5, 3)  # One side is too long

    def test_positive_nonzero_floats(self):
        # Additional test to check positive non-zero float inputs not being equilateral, isosceles or scalene
        self.assertEqual(triangle(0.9, 0.9, 0.9), "Equilateral")
        self.assertEqual(triangle(3.1, 3.1, 4.0), "Isosceles")
        self.assertEqual(triangle(2.1, 3.2, 4.3), "Scalene")
        
# This makes it possible to run the tests from command line using python -m unittest test_triangle.py
if __name__ == '__main__':
    unittest.main()