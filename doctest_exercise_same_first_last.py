"""
Your name: Carson Olafson
Your student number: A01221217
"""


def same_first_last(a_list):
    """
    Return True if and only if first item of the list
    is the same as the last item in the list.

    :param a_list: a list of course!
    :precondition: len(a_list) >= 2
    :postcondition: return true if the first/last elements are the same
    :postcondition: a_list is unchanged
    :return: True if the first/last elements are the same, else False

    Test 1 - 3: Default test, finds if the first and last elements in a list are the same. It did

    Test 4: finds if floats are accepted in function. They are.

    Test 5: finds if function can take negative integers as elements. It did

    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    >>> same_first_last([4.5, 4.5])
    True
    >>> same_first_last([4.5, -4.5])
    False
    """
    item = a_list[0]
    if item == a_list[-1]:
        return True
    else:
        return False
