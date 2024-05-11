# def triangle(a, b, c):
    # if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        # raise TypeError("All sides must be integers or floats")
    # if not all(x > 0 for x in [a, b, c]):
        # raise ValueError("All sides must be greater than zero")
    # if a >= b + c or b >= a + c or c >= a + b:
        # raise ValueError("The sum of any two sides must be greater than the third")
    
    # if a == b == c:
        # return "Equilateral"
    # elif a == b or b == c or a == c:
        # return "Isosceles"
    # else:
        # return "Scalene"
import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        # Equivalence Partition: a = b = c
        self.assertEqual(triangle(6, 6, 6), 'Equilateral') # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22

    def test_isosceles_triangle(self):
        # Equivalence Partitions: a = b != c, b = c != a, a = c != b
        self.assertEqual(triangle(5, 5, 3), 'Isosceles') # 23
        self.assertEqual(triangle(3, 5, 5), 'Isosceles')
        self.assertEqual(triangle(5, 3, 5), 'Isosceles')

    def test_scalene_triangle(self):
        # Equivalence Partition: a != b != c
        self.assertEqual(triangle(4, 5, 6), 'Scalene') # 24

    def test_invalid_type_triangle(self):
        # Edge cases for invalid type
        with self.assertRaises(TypeError):
            triangle("a", 2, 3) # 3
        with self.assertRaises(TypeError):
            triangle(1, "b", 3) # 6
        with self.assertRaises(TypeError):
            triangle(1, 2, [3]) # 9

    def test_non_positive_values(self):
        # Equivalence Partitions for non-positive values
        with self.assertRaises(ValueError):
            triangle(-1, 1, 1) # 13
        with self.assertRaises(ValueError):
            triangle(1, 0, 1) # 14
        with self.assertRaises(ValueError):
            triangle(2, 2, -2) # 15
    
    def test_triangle_inequality(self):
        # Checking the triangle inequality theorem
        with self.assertRaises(ValueError):
            triangle(1, 1, 3) # 19
        with self.assertRaises(ValueError):
            triangle(1, 3, 1) # 20
        with self.assertRaises(ValueError):
            triangle(3, 1, 1) # 21

if __name__ == '__main__':
    unittest.main()