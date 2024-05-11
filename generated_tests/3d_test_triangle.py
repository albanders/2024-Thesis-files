import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    # Test for type verification
    def test_triangle_input_types(self):
        with self.assertRaises(TypeError):
            triangle('3', 4, 5) # 3
        with self.assertRaises(TypeError):
            triangle(3, '4', 5) # 6
        with self.assertRaises(TypeError):
            triangle(3, 4, '5') # 9

    # Test input values greater than zero
    def test_triangle_input_values_positive(self):
        with self.assertRaises(ValueError):
            triangle(-1, 4, 5) # 13
        with self.assertRaises(ValueError):
            triangle(3, -1, 5) # 14
        with self.assertRaises(ValueError):
            triangle(3, 4, -1) # 15

    # Test triangle inequality
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(1, 5, 3) # 20
        with self.assertRaises(ValueError):
            triangle(12, 5, 5) # 21
 
    # Test for Equilateral triangle
    def test_triangle_equilateral(self):
        self.assertEqual(triangle(3.0, 3.0, 3.0), 'Equilateral') # 2, 5, 8, 10, 11, 12, 16, 17, 18, 22
        self.assertEqual(triangle(10, 10, 10), 'Equilateral') # 1, 4, 7

    # Test for Isosceles triangle
    def test_triangle_isosceles(self):
        self.assertEqual(triangle(5, 5, 3), 'Isosceles') # 23
        self.assertEqual(triangle(3, 4, 4), 'Isosceles')
        self.assertEqual(triangle(4.0, 6.0, 4.0), 'Isosceles')

    # Test for Scalene triangle
    def test_triangle_scalene(self):
        self.assertEqual(triangle(3, 4, 5), 'Scalene') # 24
        self.assertEqual(triangle(7.1, 7.2, 7.3), 'Scalene')

if __name__ == '__main__':
    unittest.main()