"""
Your name: Carson Olafson
Your student number: A01221217
"""


def average(values):
    """
    Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    :param values: a list of numbers that may contain None
    :precondition: values is a list of numbers and/or None
    :postcondition: values is unchanged
    :return: the average of the non-None numbers in values

    Test 1: Default test, finds the average of two numbers. It did.

    Test 2: Default test, tried finding the average of two numbers with None being an included element. It did.

    Test 3. Tried using a negative integer to see if it worked in the function. It did.

    Test 4. Tried using a float and a negative to see if it worked. It did.


    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    >>> average([-20, 30])
    5.0
    >>> average([None, 0.5, -30])
    -14.75
    """
    total = 0
    counter = 0

    for value in values:
        if value is not None:
            total = value + total
            counter += 1
    return total / counter
