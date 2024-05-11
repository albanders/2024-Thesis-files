import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    
    def test_valid_passing_students(self):
        # Test a general valid case with a mix of passing and failing students
        students = [["Alice", 85, 90, 87], ["Bob", 75, 80, 79], ["Charlie", 90, 92, 88]]
        result = get_passing_students(students)
        expected = ["Alice", "Charlie"]
        self.assertEqual(result, expected) # 1, 3, 5, 7, 9, 12, 14, 17, 18

    def test_empty_input_list(self):
        # Test empty list input
        students = []
        result = get_passing_students(students)
        expected = []
        self.assertEqual(result, expected)
        
    def test_all_fail(self):
        # All students have averages below 80
        students = [["Harry", 70, 75, 65], ["Sam", 78, 77, 79]]
        result = get_passing_students(students)
        expected = []
        self.assertEqual(result, expected)

    def test_length_too_short_or_long_name(self):
        # Test for. name length > 20 and < 1
        students = [["", 85, 88, 86], ["a" * 21, 90, 92]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 10

    def test_invalid_name_type(self):
        # Element 0 is not a string type
        students = [[123, 90, 89, 88]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 8
        
    def test_invalid_scores_not_integers(self):
        # Scores are not integers
        students = [["David", "92", 88, 86]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 13

    def test_invalid_score_range(self):
        # Score is below 0 or above 100
        students = [["Eve", 95, -1], ["Fay", 101, 99]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 15

    def test_single_student_insufficient_elements(self):
        # List has fewer than two elements
        students = [["Gina"]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 6

# To execute the test cases
if __name__ == "__main__":
    unittest.main()