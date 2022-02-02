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
    minimum = 0
    two_smallest = []
    for minimum in some_list:
        if len(two_smallest) >= 2:
            return two_smallest
        else:
            minimum = min(some_list)
            minimum2 = x for x in some_list if minimum

            minimum_index = some_list.index(minimum)
            two_smallest.append(minimum_index)


""" how do I ignore the first minimum numer when trying to get the second lowest number? Current program removes 
    the first minimum, however I know this method will not work because it changes the initial list.
    
    1st strategy: find minimum in some list, then filter for minimum with boolean logic excluding first one. 
    2nd strategy: copy list and sort numbers, use the sorted list to get smallest numbers to get index values for
    original list
"""