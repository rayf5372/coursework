"""Assignment 1 - Tests for class PriorityQueue  (Task 3a)

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module will contain tests for class PriorityQueue.
"""
from container import PriorityQueue


def test_priority_queue_is_empty() -> None:
    """Test that a newly created PriorityQueue is empty."""
    pq = PriorityQueue()
    assert pq.is_empty()


def test_priority_queue_add_remove_one_element() -> None:
    """Test that a newly created PriorityQueue contains one element."""
    pq = PriorityQueue()
    pq.add(1)
    assert not pq.is_empty()
    assert pq.remove() == 1


def test_priority_queue_add_remove_many_element() -> None:
    """Test that a newly created PriorityQueue contains many element."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(3)
    assert pq.remove() == 1
    assert pq.remove() == 2
    assert pq.remove() == 3


def test_priority_queue_add_remove_many_element_with_priority() -> None:
    """Test that a newly created PriorityQueue contains many element with
    priority."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(3)
    assert pq.remove() == 1
    assert pq.remove() == 2
    assert pq.remove() == 3


def test_remove_item_present_multiple() -> None:
    """Test that remove removes the first item added (FIFO)."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(1)

    pq.remove()
    assert pq._items == [1, 2]


def test_add_item_duplicate_end() -> None:
    """Test that PriorityQueue adds duplicate items in end with
    the correct order."""
    pq = PriorityQueue()
    pq.add(2)
    pq.add(2)
    pq.add(1)
    assert pq._items == [1, 2, 2]


def test_add_item_duplicate_middle() -> None:
    """Test that PriorityQueue adds duplicate items in the middle with
    correct order."""
    pq = PriorityQueue()
    pq.add(2)
    pq.add(2)
    pq.add(1)
    pq.add(3)
    assert pq._items == [1, 2, 2, 3]


def test_add_item_duplicate_start() -> None:
    """Test that PriorityQueue adds duplicate items in the start
    with correct order."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(2)
    pq.add(1)
    assert pq._items == [1, 1, 2]


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
