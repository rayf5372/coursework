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

    def test_all_within_grid_not_all_in_grid(self):
        """Test when not all four coordinates are within a 4-by-4 grid."""
        assert not all_within_grid([(0, 0), (5, 5), (2, 2), (3, 3)], 4)

    def test_reflect_vertically_above(self):
        """Test reflecting vertically for a coordinate above the horizontal."""
        assert reflect_vertically((0, 1), 5) == (4, 1)

    def test_reflect_vertically_middle(self):
        """Test reflecting vertically for a coordinate on the horizontal."""
        assert reflect_vertically((2, 1), 5) == (2, 1)

    def test_reflect_points(self):
        """Test reflecting a short line"""
        assert reflect_points([(0, 1), (1, 2)], 5) == [(4, 1), (3, 2)]


class TestLine:
    """
    TODO Task 2: add tests for the Line methods and related functions
                 You must write two tests for each of:
                   - is_row, is_column, and is_diagonal
                   - Line.drop, Line.is_full, and Line.has_fiar
    """

    def test_is_row_is_valid_row(self):
        """Test that [(0,0),(0,1),(0,2),(0,3)] is a valid row"""
        test_row = [
            Square((0, 1)),
            Square((0, 2)),
            Square((0, 3)),
            Square((0, 4)),
        ]
        assert is_row(test_row) == True

    def test_is_row_not_same_row_coor(self):
        """Test is_row on Squares that do not have the same row coordinates"""
        test_row2 = [
            Square((0, 1)),
            Square((1, 2)),
            Square((0, 3)),
            Square((0, 4)),
        ]
        assert is_row(test_row2) == False

    def test_is_row_not_increase_one(self):
        """Test is_row on Squares whose columns do not increase by 1"""
        test_row3 = [
            Square((0, 1)),
            Square((0, 2)),
            Square((0, 4)),
            Square((0, 3)),
        ]
        assert is_row(test_row3) == False

    def test_is_column_is_valid_column(self):
        """Test that [(0,1),(1,1),(2,1),(3,1)] is a valid column"""
        test_column = [
            Square((0, 1)),
            Square((1, 1)),
            Square((2, 1)),
            Square((3, 1)),
        ]
        assert is_column(test_column) == True

    def test_is_column_not_same_column_coor(self):
        """
        Test is_column on Squares that do not have the same column coordinates
        """
        test_column2 = [
            Square((0, 1)),
            Square((1, 1)),
            Square((3, 3)),
            Square((2, 1)),
        ]
        assert is_column(test_column2) == False

    def test_is_column_not_increase_one(self):
        """Test is_column on Squares whose rows do not increase by 1"""
        test_column3 = [
            Square((0, 1)),
            Square((1, 1)),
            Square((3, 1)),
            Square((5, 1)),
        ]
        assert is_column(test_column3) == False

    def test_is_diagonal_down_valid(self):
        """Test that [(0,0), (1,1), (2,2), (3,3)] is a valid down diagonal"""
        diagonal_down = [
            Square((0, 0)),
            Square((1, 1)),
            Square((2, 2)),
            Square((3, 3)),
        ]
        assert is_diagonal(diagonal_down) == True

    def test_is_diagonal_up_valid(self):
        """Test a valid diagonal"""
        diagonal_up = [
            Square((3, 1)),
            Square((2, 2)),
            Square((1, 3)),
            Square((0, 4)),
        ]
        assert is_diagonal(diagonal_up) is True

    def test_is_diagonal_not_valid(self):
        """Test is_diagonal on Squares that is not a valid diagonal"""
        not_diagonal = [
            Square((0, 0)),
            Square((1, 1)),
            Square((4, 3)),
            Square((2, 2)),
        ]
        assert is_diagonal(not_diagonal) == False

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

    def test_drop_empty_column(self):
        """Test dropping into an empty column"""
        g = Grid(4)
        assert g.drop(1, 'X') == 3

    def test_drop_on_top_of_existing(self):
        """Test dropping on top of an existing item"""
        g = Grid(4)
        g.drop(1, 'X')
        assert g.drop(1, 'X') == 2

    def test_is_full_empty_grid(self):
        """Test is_full on an empty grid"""
        g = Grid(4)
        assert not g.is_full()

    def test_is_full_partial_fill(self):
        """Test is_full on a partially filled grid"""
        g = Grid(4)
        g.drop(1, 'X')
        g.drop(2, 'O')
        assert not g.is_full()

    def test_is_full_full_columns(self):
        """Test is_full when all columns are full"""
        g = Grid(4)
        for c in range(4):
            for r in range(4):
                g.drop(c, 'X')
        assert g.is_full()

    def test_create_rows_and_columns_square_aliasing(self):
        """Test aliasing between rows, columns, and squares"""
        squares = create_squares(4)
        rows, columns = create_rows_and_columns(squares)

        assert rows[0][0] is squares[0][0]
        assert columns[0][0] is squares[0][0]

    def test_create_rows_and_columns_correct_length(self):
        """Test that rows and columns have the correct lengths"""
        squares = create_squares(4)
        rows, columns = create_rows_and_columns(squares)

        assert len(rows) == len(squares)
        assert len(columns) == len(squares[0])

    def test_create_mapping_correct_lines(self):
        """Test that the lines in the mapping are correct"""
        squares = create_squares(6)
        mapping = create_mapping(squares)
        lines = mapping[(2, 0)]

        assert len(lines) == 3
        assert is_row(lines[0].cells)
        assert is_column(lines[1].cells)
        assert is_diagonal(lines[2].cells)

    def test_create_mapping_small(self):
        """Test create_mapping on a small example"""
        squares = create_squares(4)
        mapping = create_mapping(squares)
        lines = mapping[(2, 0)]
        assert len(lines) == 2

    def test_has_fiar_empty_grid(self):
        """Test has_fiar on an empty grid"""
        grid = Grid(4)
        assert not grid.has_fiar((0, 0))

    def test_has_fiar_horizontal_four_in_a_row(self):
        """Test has_fiar with a horizontal four-in-a-row"""
        grid = Grid(4)

        for i in range(4):
            i = grid.drop(0, 'X')

        assert grid.has_fiar((0, 0))

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

    def test_x_loses(self) -> None:
        """
        Provided test demonstrating how you can test FourInARow.play using
        a StringIO object to "script" the input.
        """
        s = '4 True True\n' '1\n' '0\n' '1\n' '0\n' '1\n' '0\n' '3\n' '0\n'
        fiar = play_game(s)

        assert fiar.result == LOSS

    def test_x_draws(self) -> None:
        """
        Provided test demonstrating how you can test FourInARow.play using
        a StringIO object to "script" the input.
        """
        s = (
            '4 True True\n'
            '0\n'
            '1\n'
            '0\n'
            '1\n'
            '2\n'
            '3\n'
            '2\n'
            '3\n'
            '1\n'
            '0\n'
            '1\n'
            '0\n'
            '3\n'
            '2\n'
            '3\n'
            '2\n'
        )
        fiar = play_game(s)

        assert fiar.result == DRAW

    def test_bot_playing(self) -> None:
        """
        Test a game where both players are not human
        """
        fiar = play_game("20 False False")
        assert fiar.result in (WIN, LOSS, DRAW)


if __name__ == '__main__':
    import pytest

    pytest.main(['test_a0.py'])
