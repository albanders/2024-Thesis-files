import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    
    def test_passing_students(self):
        # Equivalence Class: Valid Names and Valid Scores
        self.assertListEqual(get_passing_students([["John", 85, 92], ["Jane", 78, 84]]), ["John"])
        self.assertListEqual(get_passing_students([["Alice", 90, 91]]), ["Alice"])
    
    def test_empty_input(self):
        # Equivalence Class: Empty List
        self.assertEqual(get_passing_students([]), [])

    def test_empty_return(self):
        # Students Average Below 80
        self.assertEqual(get_passing_students([["Bob", 79, 80], ["Tim", 75, 70]]), []) # 1, 3, 5, 7, 9, 12, 14, 18
    
    def test_invalid_name_length(self):
        # Boundary Value Analysis: Name Length
        with self.assertRaises(ValueError): # 11
            get_passing_students([["J" * 21, 95, 95]])  # Name too long
        with self.assertRaises(ValueError): # 10
            get_passing_students([["", 90, 85]])  # Name too short
    
    def test_type_error_name_and_scores(self):
        # Type Check For The First Element (Name)
        with self.assertRaises(TypeError): # 8
            get_passing_students([[123, 90, 85]])
        # Type Check For Scores
        with self.assertRaises(TypeError): # 13
            get_passing_students([["John", "not_a_number", 85]])

    def test_invalid_score(self):
        # Boundary Value Analysis: Scores
        with self.assertRaises(ValueError): # 16
            get_passing_students([["Lucy", 101, 99]])  # Score too high
        with self.assertRaises(ValueError): # 15
            get_passing_students([["Sam", -1, 89]])  # Score too low

    def test_scores_type_error(self):
        # Scores Must Be Integers
        with self.assertRaises(TypeError):
            get_passing_students([["Ella", 95.5, 90]])

if __name__ == '__main__':
    unittest.main()