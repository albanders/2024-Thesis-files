import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    def test_valid_passing_students(self):
        # Equivalence class: valid inputs with passing averages
        test_data = [
            ["Alice", 82, 90],
            ["Bob", 80, 88]
        ] # 1, 3, 5, 7, 9, 12, 14, 17
        self.assertEqual(get_passing_students(test_data), ["Alice", "Bob"])

    def test_valid_non_passing_students(self):
        # Equivalence class: valid inputs with non-passing averages
        test_data = [
            ["Carol", 79, 80],
            ["Dave", 70, 75]
        ] # 18
        self.assertEqual(get_passing_students(test_data), [])

    def test_empty_input_list(self):
        # Equivalence class: empty list as input
        self.assertEqual(get_passing_students([]), [])

    def test_invalid_list_length(self):
        # Equivalence class: input list with fewer than two elements
        with self.assertRaises(ValueError):
            get_passing_students([["Eve"]]) # 6

    def test_invalid_name_type(self):
        # Equivalence class: incorrect name type
        test_data = [
            [123, 85],
            ["Frank", 90] # 8
        ]
        with self.assertRaises(TypeError):
            get_passing_students(test_data)

    def test_invalid_name_length(self):
        # Equivalence class: name length outside 1-20 characters
        test_data = [
            ["G" * 21, 88, 92],
            ["H" * 0, 95, 96]
        ] # 11
        with self.assertRaises(ValueError):
            get_passing_students(test_data)

    def test_invalid_score_type(self):
        # Equivalence class: non-integer score
        test_data = [
            ["Ivan", 89.5, 87], # 13
            ["Jenny", 92, "ninety-three"]
        ]
        with self.assertRaises(TypeError):
            get_passing_students(test_data)

    def test_invalid_score_range(self):
        # Equivalence class: scores out of the 0-100 range
        test_data = [
            ["Kate", 101, 99], # 16
            ["Leo", -1, 88]
        ]
        with self.assertRaises(ValueError):
            get_passing_students(test_data)

# Running the tests
if __name__ == "__main__":
    unittest.main()