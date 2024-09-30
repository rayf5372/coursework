"""CSC148 Assignment 2

CSC148 Winter 2024
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, David Liu, Mario Badr, Sophia Huynh, Misha Schwartz,
Jaisie Sin, and Joonho Kim

All of the files in this directory and all subdirectories are:
Copyright (c) Diane Horton, David Liu, Mario Badr, Sophia Huynh,
Misha Schwartz, Jaisie Sin, and Joonho Kim

Module Description:

This file contains the hierarchy of Goal classes and related helper functions.
"""
from __future__ import annotations
import random
from block import Block
from settings import colour_name, COLOUR_LIST


def generate_goals(num_goals: int) -> list[Goal]:
    """Return a randomly generated list of goals with length <num_goals>.

    All elements of the list must be the same type of goal, but each goal
    must have a different randomly generated colour from COLOUR_LIST. No two
    goals can have the same colour.

    Preconditions:
    - num_goals <= len(COLOUR_LIST)
    """
    random_colours = random.sample(COLOUR_LIST, num_goals)
    result = []
    for colour in random_colours:
        goal = random.choice([BlobGoal, PerimeterGoal])
        result.append(goal(colour))
    return result


def flatten(block: Block) -> list[list[tuple[int, int, int]]]:
    """Return a two-dimensional list representing <block> as rows and columns of
    unit cells.

    Return a list of lists L, where,
    for 0 <= i, j < 2^{max_depth - self.level}
        - L[i] represents column i and
        - L[i][j] represents the unit cell at column i and row j.

    Each unit cell is represented by a tuple of 3 ints, which is the colour
    of the block at the cell location[i][j].

    L[0][0] represents the unit cell in the upper left corner of the Block.
    """
    if not block.children:
        board = []
        size = 2 ** (block.max_depth - block.level)
        for i in range(size):
            column = []
            for _ in range(size):
                column.append(block.colour)
            board.append(column)
        return board
    else:
        result = []
        for child in block.children:
            result.append(flatten(child))
        first = []
        second = []
        for i in range(len(result[1])):
            first.append(result[1][i] + result[2][i])
        for i in range(len(result[0])):
            second.append(result[0][i] + result[3][i])
        return first + second


class Goal:
    """A player goal in the game of Blocky.

    This is an abstract class. Only child classes should be instantiated.

    Instance Attributes:
    - colour: The target colour for this goal, that is the colour to which
              this goal applies.
    """

    colour: tuple[int, int, int]

    def __init__(self, target_colour: tuple[int, int, int]) -> None:
        """Initialize this goal to have the given <target_colour>."""
        self.colour = target_colour

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given <board>.

        The score is always greater than or equal to 0.
        """
        raise NotImplementedError

    def description(self) -> str:
        """Return a description of this goal."""
        raise NotImplementedError


class PerimeterGoal(Goal):
    """A goal to maximize the presence of this goal's target colour
    on the board's perimeter.
    """

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given board.

        The score is always greater than or equal to 0.

        The score for a PerimeterGoal is defined to be the number of unit cells
        on the perimeter whose colour is this goal's target colour. Corner cells
        count twice toward the score.
        """
        flattened_board = flatten(board)
        score = 0
        size = len(flattened_board)

        for cell in flattened_board[0] + flattened_board[-1]:
            if cell == self.colour:
                score += 1

        for i in range(0, size):
            if flattened_board[i][0] == self.colour:
                score += 1
            if flattened_board[i][-1] == self.colour:
                score += 1

        return score

    def description(self) -> str:
        """Return a description of this goal."""
        return (
            f'Fill in the most {colour_name(self.colour)} in the perimeter '
            f'of the board.'
        )


class BlobGoal(Goal):
    """A goal to create the largest connected blob of this goal's target
    colour, anywhere within the Block.
    """

    def update_blob(
        self,
        row: int,
        column: int,
        flat_board: list[list[tuple[int, int, int]]],
        connected: list[list[int]],
    ) -> int:
        """Check if part of blob size and then update blob size."""
        if 0 <= row < len(flat_board) and 0 <= column < len(flat_board[0]):
            if (
                connected[row][column] == -1
                and flat_board[row][column] == self.colour
            ):
                return self._undiscovered_blob_size(
                    (row, column), flat_board, connected
                )
        return 0

    def score(self, board: Block) -> int:
        """Return the current score for this goal on the given board.

        The score is always greater than or equal to 0.

        The score for a BlobGoal is defined to be the total number of
        unit cells in the largest connected blob within this Block.
        """
        flat_board = flatten(board)
        max_blob_size = 0
        visited = [
            [-1 for _ in range(len(flat_board[0]))]
            for _ in range(len(flat_board))
        ]

        for row in range(len(flat_board)):
            for col in range(len(flat_board[0])):
                if (
                    flat_board[row][col] == self.colour
                    and visited[row][col] == -1
                ):
                    blob_size = self._undiscovered_blob_size(
                        (row, col), flat_board, visited
                    )
                    max_blob_size = max(max_blob_size, blob_size)

        return max_blob_size

    def _undiscovered_blob_size(
        self,
        pos: tuple[int, int],
        board: list[list[tuple[int, int, int]]],
        visited: list[list[int]],
    ) -> int:
        """Return the size of the largest connected blob in <board> that (a) is
        of this Goal's target <colour>, (b) includes the cell at <pos>, and (c)
        involves only cells that are not in <visited>.

        <board> is the flattened board on which to search for the blob.
        <visited> is a parallel structure (to <board>) that, in each cell,
        contains:
            -1 if this cell has never been visited
            0  if this cell has been visited and discovered
               not to be of the target colour
            1  if this cell has been visited and discovered
               to be of the target colour

        Update <visited> so that all cells that are visited are marked with
        either 0 or 1.

        If <pos> is out of bounds for <board>, return 0.
        """
        row, col = pos
        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or visited[row][col] != -1
        ):
            return 0
        visited[row][col] = 0
        if board[row][col] != self.colour:
            return 0

        visited[row][col] = 1
        size = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d_row, d_col in directions:
            next_pos = (row + d_row, col + d_col)
            size += self._undiscovered_blob_size(next_pos, board, visited)

        return size

    def description(self) -> str:
        """Return a description of this goal."""

        return (
            f'Generate the largest blob of the target color which '
            f'{colour_name(self.colour)} '
            f'is connected and anywhere within the Block.'
        )


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(
        config={
            'allowed-import-modules': [
                'doctest',
                'python_ta',
                'random',
                'typing',
                'block',
                'settings',
                'math',
                '__future__',
            ],
            'max-attributes': 15,
        }
    )
