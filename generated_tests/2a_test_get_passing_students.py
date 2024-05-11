import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    def test_passing_students(self):
        # Test with regular input, expect normal output
        students = [
            ["John Doe", 82, 90, 78],
            ["Jane Smith", 75, 88, 80],
            ["Alice Johnson", 92, 95, 89]
        ]
        result = get_passing_students(students)
        self.assertEqual(result, ["John Doe", "Alice Johnson"])

    def test_empty_input(self):
        # Test with an empty list, expect empty list output
        students = []
        result = get_passing_students(students)
        self.assertEqual(result, []) # 1

    def test_no_passing_students(self):
        # Test with all students failing, expect empty output list
        students = [
            ["John Doe", 70, 60, 50]
        ]
        result = get_passing_students(students)
        self.assertEqual(result, []) # 3, 5, 7, 9, 12, 14, 18
    
    def test_invalid_input_data_structure(self):
        # Test with invalid data structure, expect ValueError
        with self.assertRaises(ValueError): # 6
            get_passing_students([["John Doe"]])  # not enough elements
    
    def test_invalid_name_type(self):
        # Test with invalid name type, expect TypeError
        with self.assertRaises(TypeError):
            get_passing_students([[10, 90, 80, 70]]) # 8

    def test_invalid_name_length(self):
        # Test with invalid name length, expect ValueError
        with self.assertRaises(ValueError):
            get_passing_students([["J"*21, 80, 85, 90]]) # 11

    def test_invalid_score_type(self):
        # Test with non-integer score, expect TypeError
        with self.assertRaises(TypeError):
            get_passing_students([["John Doe", "eighty", 90, 78]]) # 13
    
    def test_invalid_score_range(self):
        # Test with scores out of range, expect ValueError
        with self.assertRaises(ValueError):
            get_passing_students([["John Doe", 150, 90, 78]]) # 16
        
    def test_inconsistent_list_structures(self):
        # Test with lists having inconsistent structures, expect errors
        with self.assertRaises(ValueError):
            get_passing_students([["Jane", 88, 90], ["Invalid", 77]])  # second list lacks enough scores
        with self.assertRaises(TypeError): # 4
            get_passing_students([["Valid", 100], 9999])  # second item not a list

if __name__ == "__main__":
    unittest.main()