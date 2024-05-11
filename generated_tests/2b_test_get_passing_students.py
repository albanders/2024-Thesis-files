import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    def test_passing_students_threshold(self):
        """Test students who are right at the 80% average mark should be included."""
        data = [["Alice", 80, 80], ["Bob", 79, 80], ["Cathy", 80, 81]]
        result = get_passing_students(data)
        self.assertListEqual(result, ["Alice", "Cathy"]) # 1, 3, 5, 7, 9, 12, 14, 17, 18

    def test_no_students(self):
        """Test an empty list input."""
        data = []
        result = get_passing_students(data)
        self.assertListEqual(result, [])

    def test_non_list_input(self):
        """Test that list contains sublist."""
        data = "not-a-list"
        with self.assertRaises(TypeError):
            get_passing_students(data) # 2

    def test_empty_student_record(self):
        """Test input list with less than two elements raises ValueError."""
        data = [["Alice"]]  # Only name and no scores
        with self.assertRaises(ValueError):
            get_passing_students(data) # 6

    def test_invalid_name_type(self):
        """Test non-string names raise TypeError."""
        data = [[123, 85, 90], ["Bob", 80, 90]]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 8

    def test_name_length(self):
        """Test names' length boundaries."""
        data = [["A" * 21, 100, 100], ["A", 100, 100]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 11

    def test_score_type(self):
        """Test for score element types, expecting integers."""
        data = [["Alice", "eighty", 85], ["Bob", 85, 90]]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 13

    def test_score_range(self):
        """Test score values must be 0 to 100."""
        data = [["Alice", 101, 80], ["Bob", -1, 90], ["Cathy", 0, 100]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 16

if __name__ == "__main__":
    unittest.main()