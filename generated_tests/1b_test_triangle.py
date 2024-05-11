import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(2, 2, 2), 'Equilateral') # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(10.0, 10.0, 10.0), 'Equilateral') # 2, 5, 8

    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), 'Isosceles') # 23
        self.assertEqual(triangle(5, 5, 3), 'Isosceles')
        self.assertEqual(triangle(5, 3, 5), 'Isosceles')
        self.assertEqual(triangle(8.0, 8.0, 5.0), 'Isosceles')

    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 3, 4), 'Scalene') # 24
        self.assertEqual(triangle(5.1, 10.2, 12.3), 'Scalene')
    
    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            triangle('3', 4, 5) # 3
        with self.assertRaises(TypeError):
            triangle(1, 'two', 1) # 6

    def test_non_positive_sides(self):
        with self.assertRaises(ValueError):
            triangle(0, 1, 1) # 13
        with self.assertRaises(ValueError):
            triangle(-1, 1, 1)

    def test_violation_of_triangle_inequality(self):
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(10, 5, 5) # 21

if __name__ == '__main__':
    unittest.main()