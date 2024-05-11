import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    
    def test_successful_passing_students(self):
        # Test with students who have an average above or exactly 80
        input_data = [
            ['John', 85, 90],
            ['Jane', 80, 80],
            ['Doe', 70, 90]
        ]
        expected_output = ['John', 'Jane']
        self.assertEqual(get_passing_students(input_data), expected_output)
    
    def test_no_students_passing(self):
        # Input with students all having averages below 80
        input_data = [
            ['Bob', 70, 70],
            ['Alice', 75, 75]
        ]
        self.assertEqual(get_passing_students(input_data), []) # 1, 3, 5, 7, 9, 12, 14, 18
    
    def test_empty_input_list(self):
        # Input list is empty
        self.assertEqual(get_passing_students([]), [])
    
    def test_invalid_input_no_students_data(self):
        # Test raising ValueError if student entry has less than two elements
        with self.assertRaises(ValueError):
            get_passing_students([['Bob']]) # 6
    
    def test_invalid_name_type(self):
        # Name not a string raises TypeError
        with self.assertRaises(TypeError):
            get_passing_students([[123, 85, 90]]) # 8
    
    def test_name_length_violation(self):
        # Test raising ValueError if name length not between 1 and 20
        with self.assertRaises(ValueError):
            get_passing_students(['a'*21, 85, 90])
        with self.assertRaises(ValueError):
            get_passing_students(['', 85, 90])
    
    def test_invalid_scores_type(self):
        # Test raising TypeError if scores are not integers
        with self.assertRaises(TypeError):
            get_passing_students([['John', '85', '90']]) # 13
    
    def test_invalid_scores_range(self):
        # Test raising ValueError if scores aren't between 0 to 100
        with self.assertRaises(ValueError):
            get_passing_students([['Bob', -1, 101]]) # 15
        with self.assertRaises(ValueError):
            get_passing_students([['Alice', 101, 100]]) # 16
    
if __name__ == '__main__':
    unittest.main()