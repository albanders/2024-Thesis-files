"""
Import "triangle" from triangle.py and create unit tests in Python using the unittest module to verify these requirements:

1. The function "triangle" receives three numbers as inputs, representing the sides of a triangle. It returns a name of the type of triangle: "Equilateral", "Isosceles" or "Scalene".
2. All input numbers must be either integer or float, else a TypeError is raised.
3. If all input numbers are of equal length, the function returns "Equilateral".
4. If two input numbers are of equal length, the function returns "Isosceles".
5. If no input numbers are of equal length, the function returns "Scalene".
6. All input numbers must be greater than zero, else a ValueError is raised.
7. If one number is equal to or greater than the sum of the other two, a ValueError is raised. (Hint: look-up "triangle inequality")
"""

def triangle(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError(f"{a!r} must be int or float")

    if not isinstance(b, (int, float)):
        raise TypeError(f"{b!r} must be int or float")

    if not isinstance(c, (int, float)):
        raise TypeError(f"{c!r} must be int or float")

    if not a > 0:
        raise ValueError(f"{a!r} must be greater than zero")
    if not b > 0:
        raise ValueError(f"{b!r} must be greater than zero")
    if not c > 0:
        raise ValueError(f"{c!r} must be greater than zero")

    # Triangle inequality theorem
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Values cannot form a valid triangle")

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    elif a != b != c:
        return "Scalene"
