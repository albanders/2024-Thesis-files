"""
Import "make_even" from make_even.py and create unit tests in Python using the unittest module to verify these requirements:

1. The function "make_even" receives a list of numbers as input. It changes the input list by adding 1 to every odd number, and then returns None.
2. The input list must not be empty, else a ValueError is raised.
3. All numbers in the input list must be integers, else a TypeError is raised.
4. All numbers in the input list must be non-negative (>= 0), else a ValueError is raised.
"""

def make_even(input_list):
    if type(input_list) is not list:
        raise TypeError("Incorrect input type")

    if len(input_list) == 0:
        raise ValueError("List must not be empty")

    if any([type(number) is not int for number in input_list]):
        raise TypeError("List must contain only int-type values")

    if any([number < 0 for number in input_list]):
        raise ValueError("List must contain only non-negative values")

    for i in range(len(input_list)):
        number = input_list[i]

        if number % 2 != 0:
            input_list[i] = number + 1
