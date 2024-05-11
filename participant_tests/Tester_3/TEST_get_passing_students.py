import unittest

from get_passing_students import get_passing_students

"""
Import "get_passing_students" from get_passing_students.py and create unit tests
in Python using the unittest module to verify these requirements:

1. The function "get_passing_students" receives a list of lists containing a name and scores (numbers) as input. 
   It returns a list of students' names who have an average score equal to or greater than 80, or an empty list.

2. Each list in the input list must contain at least two elements, else a ValueError is raised.

3. The first element of each list is a name that must be a string, else a TypeError is raised.

4. All names' length must be between 1 and 20, inclusive, else a ValueError is raised.

5. All elements following the name in each list must be integers, else a TypeError is raised.

6. All elements following the name in each list must be a number between 0 and 100, inclusive, else a ValueError is raised.
"""

class TestGetPassingStudents(unittest.TestCase):
   def TestCorrect(self):
      ScoreList = [["Axel",80,100,80],["Albin",80,80,0]]
      self.assertEqual(get_passing_students(ScoreList), ["Axel"])
   
   def TestWrongelementamount(self):
      with self.assertRaises(ValueError):
         get_passing_students(["Axel"])
   
   def TestWrongNameLenthLong(self):
      with self.assertRaises(ValueError):
         get_passing_students(["abcdefghijklmnopqrstuvwxyz",80,80,80])
   
   def TestWrongNameLenthShotrt(self):
      with self.assertRaises(ValueError):
         get_passing_students(["",80,80,80])
   
   def TestWrongBigNumber(self):
      with self.assertRaises(ValueError):
         get_passing_students(["Axel",180,80,80])
      
   def TestWrongSmallNumber(self):
      with self.assertRaises(ValueError):
         get_passing_students(["",-1,80,80])

   def TestNameNotFirst(self):
      with self.assertRaises(TypeError):
         get_passing_students([80,"Axel",80])
   
   def TestStringAfterFirst(self):
      with self.assertRaises(TypeError):
         get_passing_students(["Axel", 80,"Albin",80])


if __name__ == "__main__":
    unittest.main()
