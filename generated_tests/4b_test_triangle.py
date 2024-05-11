import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        # Testing for equilateral triangle
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
    
    def test_isosceles_triangle(self):
        # Testing for isosceles triangle
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4, 3, 4), "Isosceles")  # Covering different sides matching

    def test_scalene_triangle(self):
        # Testing for scalene triangle
        self.assertEqual(triangle(4, 5, 6), "Scalene") # 24
    
    def test_zero_or_negative_side_value_error(self):
        # Testing error for zero or negative sides
        with self.assertRaises(ValueError):
            triangle(0, 1, 1) # 13
        with self.assertRaises(ValueError):
            triangle(1, -1, 1) # 14
    
    def test_non_numeric_types_type_error(self):
        # Testing error for non-numeric inputs
        with self.assertRaises(TypeError):
            triangle('a', 'b', 'c') # 3
        with self.assertRaises(TypeError):
            triangle(1, '2', 3) # 6
    
    def test_triangle_inequality_value_error(self):
        # Testing triangle inequality violation
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(10, 5, 2) # 21
    
    def test_valid_floats(self):
        # Testing for valid float inputs
        self.assertEqual(triangle(2.0, 2.0, 2.0), "Equilateral") # 2, 5, 8
        self.assertEqual(triangle(3.0, 3.0, 2.0), "Isosceles")
        self.assertEqual(triangle(4.5, 5.5, 6.5), "Scalene")

if __name__ == "__main__":
    unittest.main()