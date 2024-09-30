"""CSC148 Assignment 0

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jonathan Calver and Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) Jonathan Calver, Diane Horton, and Sophia Huynh.

=== Module Description ===

This file contains some provided tests for the assignment and is where
you will write additional tests.

To run the tests in this file, right-click here and select the option
that says "Run 'Python tests in test...'"

Note: We will not run pyTA on this file when grading your assignment.

"""
from __future__ import annotations

from four_in_a_row import *
from a0 import *


# TODO add tests for each method and function as indicated in the assignment
#      Note: we have scaffolded some code below for you to add your tests into.
#      Make sure each test has a unique name and that each test starts
#      with test_
#      The tests below are organized into classes to help keep related tests
#      grouped together. In PyCharm you can choose to run all tests in a single
#      class by using the run button beside the class name (just like how you
#      can choose to run a single test). Alternatively, you can run all tests
#      in the file by right-clicking the file name and choosing to run tests.

class TestHelpers:
    """
    These are provided tests related to Task 1, which are meant to remind you
    of the structure of a pytest for later tasks. For Task 1, you are asked
    to write doctests instead.

    While not required, you are welcome to add other pytests here as you
    develop your code.
    """

    def test_within_grid_in_grid(self):
        """Test that (0, 0) is inside a 4-by-4 grid."""
        assert within_grid((0, 0), 4)

    def test_within_grid_outside_grid(self):
        """Test that (4, 4) is outside a 4-by-4 grid."""
        assert not within_grid((4, 4), 4)

    def test_all_within_grid_all_in_grid(self):
        """Test when the four coordinates are all within a 4-by-4 grid."""
        assert all_within_grid([(0, 0), (1, 1), (2, 2), (3, 3)], 4)

    def test_reflect_vertically_above(self):
        """Test reflecting vertically for a coordinate above the middle."""
        assert reflect_vertically((0, 1), 5) == (4, 1)

    def test_reflect_vertically_middle(self):
        """Test reflecting vertically for a coordinate on the middle row."""
        assert reflect_vertically((2, 1), 5) == (2, 1)

    def test_reflect_points(self):
        """Test reflecting a very short line"""
        assert reflect_points([(0, 1), (1, 2)], 5) == [(4, 1), (3, 2)]


class TestLine:
    """
    TODO Task 2: add tests for the Line methods and related functions
                 You must write two tests for each of:
                   - is_row, is_column, and is_diagonal
                   - Line.drop, Line.is_full, and Line.has_fiar
    """
    pass


class TestGrid:
    """
    TODO Task 3.1: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.drop, Grid.is_full
                   - create_rows_and_columns

    TODO Task 3.2: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.has_fiar
                   - create_mapping
    """
    pass


class TestFourInARow:
    """
    TODO TASK 4:
     - run check_coverage.py to get the code coverage report.
     - Using the code coverage report, identify which branches of the code
       are not currently being tested.
     - add tests below in order to achieve 100% code coverage when you run
       check_coverage.py. Your tests should follow a similar structure
       to the test_x_wins test defined below.
    """

    def test_x_wins(self) -> None:
        """
        Provided test demonstrating how you can test FourInARow.play using
        a StringIO object to "script" the input.

        See both the handout and the Task 4 section of the supplemental slides
        for a detailed explanation of this example.
        """
        fiar = play_game(GAME_SCRIPT_X_WINS)

        assert fiar.result == WIN

    # TODO Add your tests for Task 4 here. Make sure each test has a unique name
    #      and that each test starts with test_


if __name__ == '__main__':
    import pytest

    pytest.main(['test_a0.py'])
