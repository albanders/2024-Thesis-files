import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    
    # Test for type of inputs
    def test_triangle_input_type(self):
        # Testing with correct type should not raise TypeError
        self.assertIsInstance(triangle(3, 4, 5), str) # 1, 4, 7, 10, 11, 12, 16, 17, 18, 24
        # Testing with incorrect types
        with self.assertRaises(TypeError): # 3
            triangle('3', 4, 5)
        with self.assertRaises(TypeError): # 6
            triangle(3, '4', 5)
        with self.assertRaises(TypeError): # 9
            triangle(3, 4, '5')

    # Test for equal sides (Equilateral)
    def test_equilateral_triangle(self):
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 22

    # Test for two equal sides (Isosceles)
    def test_isosceles_triangle(self):
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(3, 2, 2), "Isosceles")
        self.assertEqual(triangle(2, 3, 2), "Isosceles")

    # Test for no sides equal (Scalene)
    def test_scalene_triangle(self):
        self.assertEqual(triangle(2, 3, 4), "Scalene")

    # Test for side lengths greater than zero
    def test_positive_sides(self):
        with self.assertRaises(ValueError): # 13
            triangle(0, 1, 2)
        with self.assertRaises(ValueError): # 14
            triangle(1, 0, 2)
        with self.assertRaises(ValueError): # 15
            triangle(1, 2, 0)
        with self.assertRaises(ValueError):
            triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            triangle(1, -2, 3)
        with self.assertRaises(ValueError):
            triangle(1, 2, -3)

    # Test for triangle inequality
    def test_triangle_inequality(self):
        with self.assertRaises(ValueError): # 19
            triangle(1, 2, 3)
        with self.assertRaises(ValueError): # 21
            triangle(3, 1, 2)
        with self.assertRaises(ValueError): # 20
            triangle(1, 3, 2)

if __name__ == '__main__':
    unittest.main()