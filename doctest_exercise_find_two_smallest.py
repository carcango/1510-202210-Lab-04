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

    Test 1: Default test, returns the indices of the two smallest values in some_list. It did.

    Test 2: Default test, confirms that sine_list is unchanged in the function.

    Test 3. Tried using zero as an element in the list to see if it worked. It did.

    Test 4. Tried using a negative integer and a float to see if it worked. It did.

    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    [6, 7]
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    >>> items = [809, 834, 477, 0, 307, 122, 96, 129, 324, 476]
    >>> find_two_smallest(items)
    [3, 6]
    >>> items = [809, 1.1, 477, 478, 307, 122, 96, 102, 324, -960]
    >>> find_two_smallest(items)
    [9, 1]
    """

    lowest = some_list[0]
    lowest2 = None
    smallest_list = []
    for item in some_list[1:]:
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 is None or lowest2 > item:
            lowest2 = item

        index1 = some_list.index(lowest)
        index2 = some_list.index(lowest2)
        smallest_list = [index1, index2]
    return smallest_list
