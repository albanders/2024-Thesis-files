import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_passing_students_success(self):
        students = [
            ["Alice", 85, 92, 88], 
            ["Bob", 78, 74, 77], 
            ["Clara", 90, 95, 93]
        ]
        result = get_passing_students(students)
        self.assertEqual(result, ["Alice", "Clara"]) # 1, 3, 5, 7, 9, 12, 14, 17, 18

    def test_empty_list(self):
        students = []
        result = get_passing_students(students)
        self.assertEqual(result, [])

    def test_fails_if_not_enough_elements(self):
        students = [["Alice"]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 6
            
    def test_fails_if_name_not_string(self):
        students = [[123, 90, 92, 88]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 8

    def test_fails_if_name_length_invalid(self):
        students = [["A" * 21, 85, 92, 88]]  # 21 characters
        with self.assertRaises(ValueError):
            get_passing_students(students) # 11

        students = [["", 90, 95, 93]]  # Empty name
        with self.assertRaises(ValueError):
            get_passing_students(students) # 10

    def test_fails_if_scores_not_integers(self):
        students = [["Alice", 85.5, 92, 88]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 13

    def test_fails_if_scores_out_of_range(self):
        students = [["Alice", 101, 92, 88]]  # Score above 100
        with self.assertRaises(ValueError):
            get_passing_students(students) # 16

        students = [["Alice", -1, 92, 88]]  # Score below 0
        with self.assertRaises(ValueError):
            get_passing_students(students) # 15

if __name__ == '__main__':
    unittest.main()