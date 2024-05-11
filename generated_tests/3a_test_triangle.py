import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):

    def test_equilateral_triangle(self):
        # Equivalence Class: All sides equal
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22

    def test_isosceles_triangle(self):
        # Equivalence Classes: Any two sides equal 
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4, 3, 4), "Isosceles")
        self.assertEqual(triangle(5, 7, 5), "Isosceles")

    def test_scalene_triangle(self):
        # Equivalence Class: No sides equal
        self.assertEqual(triangle(4, 5, 6), "Scalene") # 24

    def test_non_numeric_inputs(self):
        # Equivalence Classes: Non-integer and non-float should raise TypeError
        with self.assertRaises(TypeError): # 3
            triangle("2", "2", "2")
        with self.assertRaises(TypeError): # 6
            triangle(2, "2", 3)

    def test_negative_or_zero_sides(self):
        # Equivalence Classes: Sides less than or equal to zero should raise ValueError
        with self.assertRaises(ValueError): # 13
            triangle(-1, -1, -1)
        with self.assertRaises(ValueError):
            triangle(0, 2, 2)

    def test_triangle_inequality_violation(self):
        # Equivalence Classes: Violating the triangle inequality should raise ValueError
        with self.assertRaises(ValueError): # 19
            triangle(1, 2, 3)
        with self.assertRaises(ValueError): # 21
            triangle(10, 5, 3)

    def test_valid_triangle_inequality(self):
        # Ensuring no error when the triangle sides obey triangle inequality
        self.assertEqual(triangle(3, 4, 5), "Scalene")

    def test_float_inputs(self):
        # Additional test for floating point values
        self.assertEqual(triangle(2.0, 2.0, 2.0), "Equilateral") # 2, 5, 8
        self.assertEqual(triangle(2.3, 2.3, 1.2), "Isosceles")
        self.assertEqual(triangle(3.5, 4.6, 5.7), "Scalene")

if __name__ == "__main__":
    unittest.main()