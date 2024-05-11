import unittest

from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    # Equivalence Classes
    # Valid inputs:
    # 1. Equilateral: All sides the same and satisfy triangle inequality and positive integers or floats
    # 2. Isosceles: Exactly two sides the same, satisfy triangle inequality and positive integers or floats
    # 3. Scalene: All sides different, satisfy triangle inequality and positive integers or floats
    # Invalid inputs:
    # 4. Non-numeric inputs: One or more sides not a number (int or float)
    # 5. Non-positive inputs: One or more sides <= 0
    # 6. Triangle inequality violation: A side >= sum of other two sides
    
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(3, 3, 3), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(2.0, 2.0, 2.0), "Equilateral") # 2, 5, 8

    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4.0, 4.0, 5.0), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(triangle(3, 4, 5), "Scalene") # 24
        self.assertEqual(triangle(2.5, 3.5, 4.5), "Scalene")

    def test_invalid_type_inputs(self):
        with self.assertRaises(TypeError): # 3
            triangle('a', 2, 3)
        with self.assertRaises(TypeError): # 6
            triangle(1, 'b', 3)
        with self.assertRaises(TypeError): # 9
            triangle(1, 2, [3])

    def test_non_positive_inputs(self):
        with self.assertRaises(ValueError): # 13
            triangle(-1, 2, 3)
        with self.assertRaises(ValueError): # 14
            triangle(1, 0, 3)
        with self.assertRaises(ValueError):
            triangle(0, 0, 0)

    def test_triangle_inequality_violation(self):
        with self.assertRaises(ValueError): # 19
            triangle(1, 2, 3)
        with self.assertRaises(ValueError): # 21
            triangle(10, 5, 3)
        with self.assertRaises(ValueError): # 20
            triangle(5, 10, 3)

if __name__ == "__main__":
    unittest.main()