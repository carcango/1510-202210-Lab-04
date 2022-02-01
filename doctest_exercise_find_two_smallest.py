"""
Your name: Carson Olafson
Your student number: A01221217
"""


def find_two_smallest(some_list):
    """
    Return a list containing the indices of the two smallest values
    in some_list. The indices are not in sorted order.

    :param some_list: a list of things that can be small and large
    :precondition: len(some_list) >= 2
    :precondition: some_list is a homogenous list of elements that can be compared
    :postcondition: some_list is unchanged
    :return: a list that contains two non-negative integers

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    [6, 7]
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    two_smallest = []
    for minimum in some_list:
        if len(two_smallest) >= 2:
            return two_smallest
        else:
            two_smallest += min(some_list)
