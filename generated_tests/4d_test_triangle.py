import unittest
from triangle import triangle

class TestTriangleFunction(unittest.TestCase):
    def test_equilateral_triangle(self):
        """Test that three equal sides are classified as 'Equilateral'."""
        self.assertEqual(triangle(2, 2, 2), "Equilateral") # 1, 4, 7, 10, 11, 12, 16, 17, 18, 22
    
    def test_isosceles_triangle(self):
        """Test that two equal sides are classified as 'Isosceles'."""
        self.assertEqual(triangle(2, 2, 3), "Isosceles") # 23
     
    def test_scalene_triangle(self):
        """Test that three unequal sides are classified as 'Scalene'."""
        self.assertEqual(triangle(2, 3, 4), "Scalene") # 24
    
    def test_invalid_type_inputs(self):
        """Test that a type error is raised when inputs are not numbers."""
        with self.assertRaises(TypeError):
            triangle("a", 2, 3) # 3
    
    def test_non_positive_inputs(self):
        """Test that a value error is raised for non-positive side lengths."""
        with self.assertRaises(ValueError):
            triangle(-1, 2, 2) # 13
    
    def test_triangle_inequality_violation(self):
        """Test that a value error is raised when triangle inequality is violated."""
        with self.assertRaises(ValueError):
            triangle(1, 2, 3) # 19

if __name__ == "__main__":
    unittest.main()