"""CSC148 Lab 7: Recursion

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice recursion.
"""
from python_ta.contracts import check_contracts


@check_contracts
def greater_than_all(obj: int | list, n: int) -> bool:
    """Return True iff there is no int in <obj> that is larger than or
    equal to <n> (or, equivalently, <n> is greater than all ints in <obj>).

    >>> greater_than_all(10, 3)
    False
    >>> greater_than_all([1, 2, [1, 2], 4], 10)
    True
    >>> greater_than_all([], 0)
    True
    """
    if isinstance(obj, int):
        if obj >= n:
            return False
        else:
            pass
    else:
        for sublist in obj:
            greater_than_all(sublist, n)

    return True


@check_contracts
def add_n(obj: int | list, n: int) -> int | list:
    """Return a new nested list where <n> is added to every item in <obj>.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    """
    new_list = []
    if isinstance(obj, int):
        return obj + n
    else:
        for sublist in obj:
            new_list.append(add_n(sublist, n))
    return new_list


@check_contracts
def nested_list_equal(obj1: int | list, obj2: int | list) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.
    You should only use == in the base case. Do NOT use it to compare
    otherwise (as that defeats the purpose of this exercise)!

    >>> nested_list_equal(17, [1, 2, 3])
    False
    >>> nested_list_equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> nested_list_equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    """
    # HINT: You'll need to modify the basic pattern to loop over indexes,
    # so that you can iterate through both obj1 and obj2 in parallel.
    if isinstance(obj1, int) or isinstance(obj2, int):
        return obj1 == obj2
    else:
        i = 0
        for sublist in obj1:
            if not nested_list_equal(sublist, obj2[i]):
                return False
            i += 1
    return True


@check_contracts
def duplicate(obj: int | list) -> list:
    """Return a new nested list with all numbers in <obj> duplicated.

    Each integer in <obj> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <obj> is an int, return a list containing two copies of it.

    Note: this function is always guaranteed to return a list (so the return type
    annotation is just "list" instead of "int | list").

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    # HINT: in the recursive case, you'll need to distinguish between
    # a <sublist> that is an int and a <sublist> that is a list
    # (put an isinstance check inside the loop).
    if isinstance(obj, int):
        return [obj, obj]
    else:
        result = []
        for sublist in obj:
            if isinstance(sublist, int):
                result.extend(duplicate(sublist))
            else:
                result.append(duplicate(sublist))
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all(config={'max-line-length': 100})
