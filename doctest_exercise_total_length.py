"""
Your name: Carson Olafson
Your student number: A01221217
"""


def total_length(first_string, second_string):
    """
    Return the sum of the lengths of first_string and second_string.

    :param first_string: a string, of course
    :param first_string: a string, of course
    :precondition: some_string is a string, possibly empty
    :precondition: second_string is a string, possibly empty
    :postcondition: correctly sums the lengths of the strings
    :return: the sum of the lengths, an integer

    Test 1 - 3: Default tests, test if length counter works with two strings or blank spaces. It did

    Test 4. Test if numbers work as valid string. It did

    Test 5. Test if floats work as valid string, and if it counted the period and the floating number as individual
            elements. It did


    >>> total_length('yes', 'no')
    5
    >>> total_length('yes', '')
    3
    >>> total_length('YES!!!!', 'Noooooo')
    14
    >>> total_length('1234567890', 'no')
    12
    >>> total_length('1.0', 'no')
    5
    """
    length_total = len(first_string) + len(second_string)
    return length_total
