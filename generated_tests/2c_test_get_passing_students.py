import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_valid_input(self):
        # Equivalence Partition: Valid input where some students pass
        self.assertEqual(
            get_passing_students([["Alice", 80, 85], ["Bob", 70, 75]]),
            ["Alice"] # 1, 3, 5, 7, 9, 12, 14, 17, 18
        )
        # Equivalence Partition: Valid input where all students pass
        self.assertEqual(
            get_passing_students([["Chris", 85, 90], ["Dana", 80, 100]]),
            ["Chris", "Dana"]
        )
        # Equivalence Partition: Valid input where no students pass
        self.assertEqual(
            get_passing_students([["Eve", 70, 75], ["Fred", 65, 60]]),
            []
        )

    def test_input_student_with_scores_out_of_bounds(self):
        # Boundary Partitioning: Score below 0 and above 100
        with self.assertRaises(ValueError):
            get_passing_students([["Gus", 101, 99]]) # 16
        with self.assertRaises(ValueError):
            get_passing_students([["Hank", -1, 50]]) # 15

    def test_input_invalid_student_name_length(self):
        # Boundary Value tests: Name length out of bounds 1-20
        with self.assertRaises(ValueError): # 10
            get_passing_students([["", 85, 90]])  # Empty name
        with self.assertRaises(ValueError): # 11
            get_passing_students([["Isabella" * 3, 85, 90]])  # Excessively long name

    def test_input_invalid_student_scores_type(self):
        # Type checks: Scores must be integers
        with self.assertRaises(TypeError): # 13
            get_passing_students([["Jill", "eighty", 85]])
        with self.assertRaises(TypeError):
            get_passing_students([["Joe", 85.0, 90]])  # Floats instead of integers

    def test_input_invalid_name_type(self):
        # Type checks: Names must be strings
        with self.assertRaises(TypeError):
            get_passing_students([[123, 85, 90]]) # 8

    def test_input_wrong_structure(self):
        # Test invalid structure of the list
        with self.assertRaises(ValueError): # 6
            get_passing_students([["Kate"]])  # No scores
        with self.assertRaises(ValueError):
            get_passing_students([["Luke", 99]])  # Only one score, although this could be valid depending on interpretation

if __name__ == "__main__":
    unittest.main()