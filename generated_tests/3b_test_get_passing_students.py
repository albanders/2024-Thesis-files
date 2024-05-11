import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    
    def test_passing_students(self):
        # Test with a normal case
        students = [
            ['Alice', 90, 80, 70],
            ['Bob', 85, 82, 87],
            ['Charlie', 70, 75, 60]
        ] # 1, 3, 5, 7, 9, 12, 14, 17, 18
        self.assertEqual(get_passing_students(students), ['Alice', 'Bob'])
    
    def test_empty_list_input(self):
        # Test with an empty list
        self.assertEqual(get_passing_students([]), [])
    
    def test_insufficient_data_raises_error(self):
        # Test with insufficient data in a sublist
        students = [['Alice']]
        with self.assertRaises(ValueError): # 6
            get_passing_students(students)
    
    def test_non_string_name_raises_error(self):
        # Test with non-string name
        students = [[123, 80, 90]]
        with self.assertRaises(TypeError): # 8
            get_passing_students(students)
    
    def test_invalid_name_length_raises_error(self):
        # Test with invalid name length
        students = [['A'*21, 80, 90]]
        with self.assertRaises(ValueError): # 11
            get_passing_students(students)
    
    def test_non_integer_scores_raises_error(self):
        # Test with non-integer scores
        students = [['Alice', '80', 90]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 13
    
    def test_out_of_range_scores_raises_error(self):
        # Test with out-of-range scores
        students = [['Alice', 180, 90]]
        with self.assertRaises(ValueError): # 16
            get_passing_students(students)

    def test_name_at_bounds_valid(self):
        # Test name length at lower and upper bounds
        students = [['A', 80, 90], ['A'*20, 85, 90]]
        self.assertEqual(get_passing_students(students), ['A', 'A'*20])
    
    def test_score_at_bounds_valid(self):
        # Test score at lower and upper bounds
        students = [['Alice', 0, 100], ['Bob', 100, 100]]
        self.assertEqual(get_passing_students(students), ['Bob'])


if __name__ == '__main__':
    unittest.main()