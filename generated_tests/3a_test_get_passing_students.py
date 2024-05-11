import unittest
from get_passing_students import get_passing_students

class TestGetPassingStudents(unittest.TestCase):

    def test_passing_students(self):
        # Test case to check normal behavior with students passing
        students = [["John", 80, 85], ["Jane", 90, 95]]
        result = get_passing_students(students)
        self.assertEqual(result, ["John", "Jane"]) # 1, 3, 5, 7, 9, 12, 14, 17

        # Check behavior when no students are passing
        students = [["Mark", 75, 70], ["Lucy", 65, 79]]
        result = get_passing_students(students)
        self.assertEqual(result, []) # 18
    
    def test_input_list_length(self):
        # List must contain at least two elements, name and one score
        students = [["Sarah"]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 6

    def test_input_name_type(self):
        # Name must be a string
        students = [[42, 80, 90]]
        with self.assertRaises(TypeError):
            get_passing_students(students) # 8

    def test_name_length(self):
        # Name length should be between 1 and 20
        students = [["", 85, 90], ["J" * 21, 85, 90]]
        with self.assertRaises(ValueError):
            get_passing_students(students) # 10

    def test_name_length_valid(self):
        # Valid name lengths
        students = [["J", 85, 90], ["J" * 20, 85, 90]]
        result = get_passing_students(students)
        self.assertListEqual(result, ["J", "J" + "J" * 19])

    def test_score_types(self):
        # Scores must be integers
        students = [["Emily", "80", 90]]
        with self.assertRaises(TypeError): # 13
            get_passing_students(students)

    def test_score_values(self):
        # Scores must be between 0 and 100
        students = [["Tom", -1, 101], ["Jerry", 85, 199]]
        with self.assertRaises(ValueError): # 15
            get_passing_students(students)

    def test_score_values_valid(self):
        # Valid score ranges
        students = [["Jake", 0, 100], ["Bob", 50, 50]]
        result = get_passing_students(students)
        self.assertEqual(result, ["Jake"])

if __name__ == '__main__':
    unittest.main()