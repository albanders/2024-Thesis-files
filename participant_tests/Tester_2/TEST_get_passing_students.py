import unittest

from get_passing_students import get_passing_students

"""
Import "get_passing_students" from get_passing_students.py and create unit tests
in Python using the unittest module to verify these requirements:

1. The function "get_passing_students" receives a list of lists containing a
   name and scores (numbers) as input. It returns a list of students' names who
   have an average score equal to or greater than 80, or an empty list.
2. Each list in the input list must contain at least two elements, else a
   ValueError is raised.
3. The first element of each list is a name that must be a string, else a
   TypeError is raised.
4. All names' length must be between 1 and 20, inclusive, else a ValueError is
   raised.
5. All elements following the name in each list must be integers, else a
   TypeError is raised.
6. All elements following the name in each list must be a number between
   0 and 100, inclusive, else a ValueError is raised.
"""

class TestGetPassingStudents(unittest.TestCase):
    def test_students(self):
        studs = [["Aja", 20], ["Marko", 65], ["Nika", 99], ["Lucia", 100], ["Koko", 80]]

        self.assertEqual(get_passing_students(studs), ["Nika", "Lucia", "Koko"])
        self.assertEqual(get_passing_students([["Aja", 20], ["Marko", 65]]), [])

    def test_elements(self):
        with self.assertRaises(ValueError):
            get_passing_students([["Aja"], ["Marko", 65], ["Nika", 100]])
            get_passing_students([["Aja"], ["Marko"], ["Nika"]])
    
    def test_name(self):
        with self.assertRaises(TypeError):
            get_passing_students([[20, "Aja"], ["Marko", 65], ["Nika", 100]])
            get_passing_students([[20, "Aja"], [65, "Marko"], ["Nika", 100]])

    def test_len(self):
        with self.assertRaises(ValueError):
            get_passing_students([["", 20], ["Marko", 65], ["N", 100]])

    def test_ints(self):
        with self.assertRaises(TypeError):
            get_passing_students([["Aja", "20"], ["Marko", 65], ["Nika", 99], ["Lucia", "100"], ["Koko", 80]])

    def test_scores(self):
        with self.assertRaises(ValueError):
            get_passing_students([["Aja", 20], ["Marko", 65], ["Nika", 99], ["Lucia", 125], ["Koko", 80]])

if __name__ == "__main__":
    unittest.main()
