import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_passing_students(self):
        # Test for nominal case
        students = [
            ["Alice", 82, 90, 78],
            ["Bob", 75, 85, 82],
            ["Charlie", 88, 92, 80]
        ]
        result = get_passing_students(students)
        self.assertListEqual(result, ["Alice", "Charlie"])

    def test_empty_input(self):
        # Test for empty list input
        students = []
        result = get_passing_students(students)
        self.assertListEqual(result, [])

    def test_value_error_for_incorrect_student_data(self):
        # Test value error for student data having fewer than 2 elements
        students = [
            ["Alice"]
        ] # 6
        with self.assertRaises(ValueError):
            get_passing_students(students)

    def test_type_error_for_non_string_names(self):
        # Test type error where name is not a string
        students = [
            [123, 97, 95]
        ] # 8
        with self.assertRaises(TypeError):
            get_passing_students(students)

    def test_value_error_for_name_length(self):
        # Test value error for name lengths out of range
        students = [
            ["A" * 21, 100],
            ["", 85]
        ] # 11
        with self.assertRaises(ValueError):
            get_passing_students(students)

    def test_type_error_for_non_integer_scores(self):
        # Test type error for non-integer scores
        students = [
            ["Alice", "90", 88]
        ] # 13
        with self.assertRaises(TypeError):
            get_passing_students(students)

    def test_value_error_for_out_of_range_scores(self):
        # Test value error for out of range scores
        students = [
            ["Alice", -1, 101]
        ] # 15
        with self.assertRaises(ValueError):
            get_passing_students(students)

if __name__ == "__main__":
    unittest.main()