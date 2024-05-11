import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_passing_students(self):
        # Test typical case where students are passing
        students = [["John", 85, 90], ["Jane", 78, 82], ["Doe", 88, 90]]
        result = get_passing_students(students)
        self.assertListEqual(result, ["John", "Doe"])

    def test_input_with_low_scores(self):
        # Test students with low scores
        students = [["John", 60, 70], ["Jane", 75, 79]]
        result = get_passing_students(students)
        self.assertListEqual(result, []) # 1, 3, 5, 7, 9, 12, 14, 18

    def test_input_length_exception(self):
        # Test input with incorrect list lengths
        students = [["John"]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 6

    def test_non_string_name_exception(self):
        # Test non-string names
        students = [[123, 80, 90]]
        with self.assertRaises(TypeError): # 8
            get_passing_students(students)

    def test_invalid_name_length_exception(self):
        # Test names that are too long or too short
        students = [["", 80, 90], ["A" * 21, 80, 90]]
        with self.assertRaises(ValueError): # 10
            get_passing_students(students)
    
    def test_non_integer_scores_exception(self):
        # Test entries with non-integer scores
        students = [["John", 85.5, "90"]]
        with self.assertRaises(TypeError): # 13
            get_passing_students(students)

    def test_scores_out_of_range_exception(self):
        # Test scores that are out of the acceptable range
        students = [["John", 110, 90], ["Jane", -5, 90]]
        with self.assertRaises(ValueError): # 16
            get_passing_students(students)

# This allows the test to be run from the command line
if __name__ == "__main__":
    unittest.main()