import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(3, 3, 3), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22

    def test_isosceles_triangle(self):
        self.assertEqual(triangle(5, 5, 3), "Isosceles") # 23
        self.assertEqual(triangle(3, 5, 5), "Isosceles")
        self.assertEqual(triangle(5, 3, 5), "Isosceles")
    
    def test_scalene_triangle(self):
        self.assertEqual(triangle(4, 5, 6), "Scalene") # 24

    def test_type_error_with_non_numbers(self):
        with self.assertRaises(TypeError):
            triangle('a', 2, 3) # 3
        with self.assertRaises(TypeError):
            triangle(1, 'b', 2) # 6
        with self.assertRaises(TypeError):
            triangle(4, 5, 'c') # 9

    def test_value_error_for_sides_less_than_or_equal_to_zero(self):
        with self.assertRaises(ValueError):
            triangle(0, 1, 2) # 13
        with self.assertRaises(ValueError):
            triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            triangle(3, 4, -5) # 15
        with self.assertRaises(ValueError):
            triangle(0, 0, 0)
    
    def test_triangle_inequality_violation(self):
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(1, 10, 2) # 20
        with self.assertRaises(ValueError):
            triangle(12, 5, 4) # 21
    
    def test_float_inputs(self):
        self.assertEqual(triangle(3.0, 3.0, 3.0), "Equilateral") # 2, 5, 8
        self.assertEqual(triangle(4.0, 4.0, 5.5), "Isosceles")
        self.assertEqual(triangle(4.5, 5.5, 6.5), "Scalene")


if __name__ == "__main__":
    unittest.main()