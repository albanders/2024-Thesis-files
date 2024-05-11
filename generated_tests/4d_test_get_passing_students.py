import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    
    def test_valid_inputs(self):
        """Test with valid inputs where some students have average >= 80 and others don't."""
        students = [["Alice", 90, 85, 88], ["Bob", 70, 75, 72], ["Carol", 80, 80, 80]]
        expected = ["Alice", "Carol"]
        result = get_passing_students(students)
        self.assertEqual(result, expected) # 1, 3, 5, 7, 9, 12, 14, 17, 18
    
    def test_name_length_error(self):
        """Test errors with names that are too short or too long."""
        students = [["", 90, 85], ["A" * 21, 90, 85]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 10
    
    def test_invalid_name_type(self):
        """Test errors with invalid name types."""
        students = [[123, 90, 85], [None, 80, 80]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 8
    
    def test_score_type_error(self):
        """Test errors when scores are not integers."""
        students = [["Alice", "90", 85], ["Bob", 76, 85.5]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 13
    
    def test_score_range_error(self):
        """Test errors when scores are outside the 0-100 range."""
        students = [["Alice", 90, 101], ["Bob", -1, 85]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 16
    
    def test_incorrect_structure_error(self):
        """Test errors with incorrectly structured inputs."""
        students = [["Alice"], ["Bob", 85]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 6
    
    def test_boundary_scores(self):
        """Test boundary cases for the score average."""
        students = [["Alice", 80, 80, 80], ["Bob", 79, 79, 79]]
        expected = ["Alice"]
        result = get_passing_students(students)
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        """Test the case with an empty input list."""
        students = []
        result = get_passing_students(students)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()