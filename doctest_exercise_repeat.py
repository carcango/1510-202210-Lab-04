"""
Your name:
Your student number:
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

    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    ''
    >>> repeat('no', -2)
    ''
    >>> repeat('yesnomaybe', 3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
