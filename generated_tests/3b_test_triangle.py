import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral_triangle(self):
        # Equivalence Partition: Equal, valid side lengths
        self.assertEqual(triangle(1, 1, 1), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22

    def test_isosceles_triangle(self):
        # Equivalence Partition: Two sides equal, third different but valid
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
        self.assertEqual(triangle(4, 5, 4), "Isosceles")

    def test_scalene_triangle(self):
        # Equivalence Partition: All sides different and valid
        self.assertEqual(triangle(4, 5, 6), "Scalene") # 24

    def test_invalid_input_type(self):
        # Equivalence Partition: At least one side not an integer or float
        with self.assertRaises(TypeError):
            triangle("a", 1, 1) # 3
            triangle(1, "b", 2) # 6
            triangle(3, 4, [5]) # 9

    def test_invalid_side_length(self):
        # Equivalence Partition: At least one side zero or negative
        with self.assertRaises(ValueError):
            triangle(0, 1, 2) # 13
            triangle(-1, 2, 3)

    def test_triangle_inequality(self):
        # Equivalence Partition: Triangle inequality violation
        with self.assertRaises(ValueError): # 19, 20
            triangle(1, 2, 3)  # 1 + 2 not greater than 3
            triangle(1, 10, 5) # 1 + 5 not greater than 10

if __name__ == "__main__":
    unittest.main()