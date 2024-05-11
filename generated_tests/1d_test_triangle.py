import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):

    # Test case for requirement 2: Inputs must be integer or float
    def test_input_type(self):
        with self.assertRaises(TypeError):
            triangle('a', 2, 3) # 3
        with self.assertRaises(TypeError):
            triangle(1, 'b', 3) # 6
        with self.assertRaises(TypeError):
            triangle(1, 2, 'c') # 9

    # Test cases for requirement 3, 4 and 5: Check triangle types
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(2, 2, 2), 'Equilateral') # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
    
    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), 'Isosceles') # 23
        self.assertEqual(triangle(4, 3, 4), 'Isosceles')
        self.assertEqual(triangle(5, 10, 10), 'Isosceles')
    
    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 3, 4), 'Scalene') # 24
        self.assertEqual(triangle(5, 6, 7), 'Scalene')
    
    # Test case for requirement 6: All sides must be greater than zero
    def test_positive_sides(self):
        with self.assertRaises(ValueError):
            triangle(-1, 2, 2) # 13
        with self.assertRaises(ValueError):
            triangle(1, -2, 2) # 14
        with self.assertRaises(ValueError):
            triangle(1, 2, -2) # 15
        with self.assertRaises(ValueError):
            triangle(0, 2, 2)

    # Test case for requirement 7: Check triangle inequality theorem
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19
        with self.assertRaises(ValueError):
            triangle(1, 4, 2) # 20
        with self.assertRaises(ValueError):
            triangle(6, 2, 2) # 21

if __name__ == '__main__':
    unittest.main()