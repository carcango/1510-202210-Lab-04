"""
Your name: Carson Olafson
Your student number: A01221217
"""


def is_longer(first_list, second_list):
    """'
    Return True if and only if the length of first_list
    is longer than the length of second_list.

    :param first_list: a list of course!
    :param second_list: a list of course!
    :postcondition: first_list is not changed
    :postcondition: second_list is not changed
    :return: True if first_list is longer than second_list, else False

    Test 1: Default test, returns true if first list is longer than the second. It did.

    Test 2: Default test, tested if it would return false for lists with elements split up. It did.

    Test 3. Default test, tested to see if it works to compare integers and strings. It did.

    Test 4. Tested to see if it values floats as a single element. It did

    Test 5. Tested to see if it would value elements with exponents as a single element. It did

    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    >>> is_longer([1, 2, 3], [4.5, 5.0])
    True
    >>> is_longer([1, 2, 3], [4^9, -5])
    True
    """
    if len(first_list) > len(second_list):
        return True
    else:
        return False
