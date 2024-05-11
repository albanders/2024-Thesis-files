import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):
    def test_passing_students(self):
        # Requirement 1: Check if the average is correctly calculated
        data = [["John", 80, 80, 80], ["Jane", 90, 90, 90]]
        result = get_passing_students(data)
        self.assertEqual(result, ["John", "Jane"]) # 1, 3, 5, 7, 9, 12, 14, 17
        
    def test_empty_list_return(self):
        # Requirement 1: Return an empty list when no students have average >= 80
        data = [["John", 70, 70], ["Jane", 75, 75]]
        result = get_passing_students(data)
        self.assertEqual(result, []) # 18
        
    def test_minimum_list_length(self):
        # Requirement 2: Each list must contain at least 2 elements
        data = [["John"]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 6
            
    def test_type_of_name(self):
        # Requirement 3: First element must be a string
        data = [[123, 90, 90], ["Jane", 80, 80]]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 8
        
    def test_name_length(self):
        # Requirement 4: Name length 1 to 20 characters
        data = [["J" * 21, 90, 90], ["Jane", 80, 80]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 11
        
        data = [["", 90, 90], ["Jane", 80, 80]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 10
        
    def test_type_of_scores(self):
        # Requirement 5: All scores must be integers
        data = [["John", "90", 80], ["Jane", 80, 70]]
        with self.assertRaises(TypeError):
            get_passing_students(data) # 13
        
    def test_range_of_scores(self):
        # Requirement 6: Scores between 0 and 100 inclusive
        data = [["John", 101, 90], ["Jane", 80, 70]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 16
        
        data = [["John", -1, 90], ["Jane", 80, 70]]
        with self.assertRaises(ValueError):
            get_passing_students(data) # 15

    # def test_valid_scores(self):
        # # Requirement 5 & 6: Check valid integer scores 0-100
        # data = [["John", 0, 100], ["Jane", 50, 100]]
        # result = get_passing_students(data)
        # self.assertEqual(result, ["John", "Jane"])

# Main block to execute the tests
if __name__ == '__main__':
    unittest.main()