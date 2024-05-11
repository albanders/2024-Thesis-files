import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        # Test case for Equilateral triangle (all sides equal)
        self.assertEqual(triangle(5, 5, 5), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
    
    def test_isosceles_triangles(self):
        # Test cases for Isosceles triangle (exactly two sides equal)
        self.assertEqual(triangle(5, 5, 3), "Isosceles") # 23
        self.assertEqual(triangle(3, 5, 5), "Isosceles")
        self.assertEqual(triangle(5, 3, 5), "Isosceles")
    
    def test_scalene_triangle(self):
        # Test case for Scalene triangle (no sides equal)
        self.assertEqual(triangle(4, 5, 6), "Scalene") # 24
    
    def test_input_type_errors(self):
        # Test cases where input is not integer or float
        with self.assertRaises(TypeError):
            triangle('3', 4, 5) # 3
        with self.assertRaises(TypeError):
            triangle(3, '4', 5) # 6
        with self.assertRaises(TypeError):
            triangle(3, 4, '5') # 9
    
    def test_zero_or_negative_side_lengths(self):
        # Test cases where sides are 0 or negative
        with self.assertRaises(ValueError):
            triangle(0, 5, 5) # 13
        with self.assertRaises(ValueError):
            triangle(-1, 5, 5)
        with self.assertRaises(ValueError):
            triangle(5, 0, 5) # 14
        with self.assertRaises(ValueError):
            triangle(5, -2, 5)
        with self.assertRaises(ValueError):
            triangle(5, 5, 0) # 15
        with self.assertRaises(ValueError):
            triangle(5, 5, -3)
    
    def test_triangle_inequality_violations(self):
        # Test cases that violate the triangle inequality theorem
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(2, 1, 3)
        with self.assertRaises(ValueError):
            triangle(2, 3, 1) # 20
        with self.assertRaises(ValueError):
            triangle(1, 10, 2)
        with self.assertRaises(ValueError):
            triangle(10, 2, 1) # 21
        with self.assertRaises(ValueError):
            triangle(10, 1, 2)

if __name__ == "__main__":
    unittest.main()