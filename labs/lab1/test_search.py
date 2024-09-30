"""CSC148 Lab 1: Introduction to CSC148!

=== CSC148 Fall 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1


def test_empty_list() -> None:
    """Test binary_search on an empty list."""
    assert binary_search([], 1) == -1


def test_list_with_repeated_elements() -> None:
    """Test binary_search on a list with repeated elements."""
    assert binary_search([1, 2, 2, 2, 4], 2) == 1


def test_single_item_list() -> None:
    """Test binary_search on a list with a single item."""
    assert binary_search([5], 5) == 0


def test_single_item_not_in_list() -> None:
    """Test binary_search on a list with a single item not in list."""
    assert binary_search([5], 1) == -1


def test_first_item_in_list() -> None:
    """Test binary_search on a list with item in first index."""
    assert binary_search([2, 4, 6, 8, 10], 2) == 0


def test_last_item_in_list() -> None:
    """Test binary_search on a list with item in last index."""
    assert binary_search([2, 4, 6, 8, 10], 10) == 4


def test_t_not_in_list() -> None:
    """Test binary_search with a value of t not in lst."""
    assert binary_search([2, 4, 6], 10) == -1


if __name__ == '__main__':
    import pytest

    pytest.main(['test_search.py'])
