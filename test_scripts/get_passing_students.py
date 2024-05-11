"""
Import "get_passing_students" from get_passing_students.py and create unit tests in Python using the unittest module to verify these requirements:

1. The function "get_passing_students" receives a list of lists containing a name and scores (numbers) as input. It returns a list of students' names who have an average score equal to or greater than 80, or an empty list.
2. Each list in the input list must contain at least two elements, else a ValueError is raised.
3. The first element of each list is a name that must be a string, else a TypeError is raised.
4. All names' length must be between 1 and 20, inclusive, else a ValueError is raised.
5. All elements following the name in each list must be integers, else a TypeError is raised.
6. All elements following the name in each list must be a number between 0 and 100, inclusive, else a ValueError is raised.
"""

def get_passing_students(student_scores):
    if type(student_scores) is not list:
        raise TypeError("Incorrect input type")

    passing_students = []

    for student in student_scores:

        if type(student) is not list:
            raise TypeError("Invalid element type")

        if len(student) < 2:
            raise ValueError("Incorrect list length, must have at least two elements")

        if type(student[0]) is not str:
            raise TypeError("Invalid name type")

        if len(student[0]) == 0:
            raise ValueError("Invalid zero-length name")

        if len(student[0]) > 20:
            raise ValueError("Invalid too long name")

        if any([type(number) is not int for number in student[1:]]):
            raise TypeError("Student scores must contain only int-type values")

        if any([number < 0 or number > 100 for number in student[1:]]):
            raise ValueError("Student scores must be between 0 and 100")

        name = student[0]
        scores = student[1:]

        if sum(scores) / len(scores) >= 80:
            passing_students.append(name)

    return passing_students
