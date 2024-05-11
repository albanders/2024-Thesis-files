import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_valid_inputs_passing_students(self):
        # Equivalence Class: Valid input with scores above threshold
        data = [["Alice", 85, 90, 80], ["Bob", 82, 84, 83]]
        result = get_passing_students(data)
        self.assertEqual(result, ["Alice", "Bob"]) # 1, 3, 5, 7, 9, 12, 14, 17

    def test_valid_inputs_no_passing_students(self):
        # Equivalence Class: Valid input with scores below threshold
        data = [["Charlie", 79, 78, 80], ["David", 70, 72, 75]]
        result = get_passing_students(data)
        self.assertEqual(result, []) # 18

    def test_invalid_structure_raises_value_error(self):
        # Requirement: Each sublist must have at least two elements
        data = [["Eve"]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 6

    def test_type_error_for_nonstring_names(self):
        # Requirement: First element of each list must be a string
        data = [[123, 95, 90, 88]]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 8

    def test_name_length_value_error(self):
        # Requirement: Name length between 1 and 20 characters
        data = [["A" * 21, 85, 86], ["", 80, 75]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 11

    def test_type_error_for_nonscore_elements(self):
        # Requirement: Scores must be integers
        data = [["George", "ninety", 88], ["Helen", 92, 'eighty']]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 13

    def test_score_range_value_error(self):
        # Requirement: Scores between 0 and 100
        data = [["Ian", 101, 90], ["Janet", -1, 89]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 16

if __name__ == '__main__':
    unittest.main()