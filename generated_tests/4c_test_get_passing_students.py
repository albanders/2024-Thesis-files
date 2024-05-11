import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_normal_passing_students(self):
        # Equivalence Class: Proper input with one or more passing students
        students_scores = [
            ['John', 85, 90],
            ['Doe', 70, 75, 80],
            ['Alice', 90, 95]
        ]
        result = get_passing_students(students_scores)
        self.assertEqual(result, ['John', 'Alice']) # 1, 3, 5, 7, 9, 12, 14, 17, 18

    def test_no_passing_students(self):
        # Equivalence Class: Proper input with no passing students
        students_scores = [
            ['Jane', 70, 75],
            ['Bob', 60, 65],
        ]
        result = get_passing_students(students_scores)
        self.assertEqual(result, [])

    def test_invalid_length_list(self):
        # Equivalence Class: Input list with less than two elements
        students_scores = [
            ['Alice'],
            ['Bob', 100]
        ]
        with self.assertRaises(ValueError):
            get_passing_students(students_scores) # 6

    def test_name_type_error(self):
        # Equivalence Class: Non-string name
        students_scores = [
            [123, 85, 90],
            ['Alice', 90, 95]
        ]
        with self.assertRaises(TypeError):
            get_passing_students(students_scores) # 8

    def test_name_invalid_length(self):
        # Equivalence Class: Name length invalid
        students_scores = [
            ['A' * 21, 90, 95],
            ['B', 90, 95]
        ]
        with self.assertRaises(ValueError):
            get_passing_students(students_scores) # 11

    def test_scores_type_error(self):
        # Equivalence Class: Non-integer scores
        students_scores = [
            ['Alice', '90', 95],
            ['Bob', 85, '100']
        ]
        with self.assertRaises(TypeError):
            get_passing_students(students_scores) # 13

    def test_score_range_error(self):
        # Equivalence Class: Scores out of valid range
        students_scores = [
            ['Alice', 101, 90],
            ['Bob', 85, -1]
        ]
        with self.assertRaises(ValueError):
            get_passing_students(students_scores) # 16

if __name__ == '__main__':
    unittest.main()