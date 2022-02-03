"""
Your name: Carson Olafson
Your student number: A01221217
"""


def repeat(some_string, number):
    """
    Return some_string repeated number times.

    If n is negative or zero, return an empty string.

    :param some_string: a string, of course, possibly empty
    :param number: an integer, possibly negative or zero
    :precondition: some_string is a string
    :precondition: number is an integer
    :postcondition: return a correctly multipled string
    :return: a string, possibly empty (length zero)

    Test 1 - 4. Default tests to see if function works as a string repeater. It does

    Test 5. Tested to see numbers worked if defined in the strings. It did.

    Test 6. Tested to see if floats could be used if type converted in number input. It did (truncated)

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    >>> repeat('yes123456789', 2)
    'yes123456789yes123456789'
    >>> repeat('yes', int(4.7))
    'yesyesyesyes'
    """

    return some_string * number
