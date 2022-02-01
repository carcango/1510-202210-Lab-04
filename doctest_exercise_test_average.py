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




    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """
    total = 0
    counter = 0

    for value in values:
        if value is not None:
            total = value + total
            counter += 1
    return total / counter
