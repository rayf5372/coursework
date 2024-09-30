"""CSC148 Lab 3: Inheritance

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the implementation of a simple number game.
The key class design feature here is *inheritance*, which is used to enable
different types of players, both human and computer, for the game.
"""
from __future__ import annotations
import random

from python_ta.contracts import check_contracts


################################################################################
# Below is the implementation of NumberGame.
#
# You do not have to modify this class, but you should read through it and
# understand how it uses the Player class (and its subclasses) that you'll
# be implementing.
#
# As you read through, make note of any methods or attributes a Player will
# need.
################################################################################
@check_contracts
class NumberGame:
    """A number game for two players.

    A count starts at 0. On a player's turn, they add to the count an amount
    between a set minimum and a set maximum. The player who brings the count
    to a set goal amount is the winner.

    The game can have multiple rounds.

    Attributes:
    - goal:
        The amount to reach in order to win the game.
    - min_step:
        The minimum legal move.
    - max_step:
        The maximum legal move.
    - current:
        The current value of the game count.
    - players:
        The two players.
    - turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    Representation Invariants:
    - self.turn >= 0
    - 0 <= self.current <= self.goal
    - 0 < self.min_step <= self.max_step <= self.goal
    """

    goal: int
    min_step: int
    max_step: int
    current: int
    players: tuple[Player, Player]
    turn: int

    def __init__(
        self, goal: int, min_step: int, max_step: int, players: tuple[Player, Player]
    ) -> None:
        """Initialize this NumberGame.

        Preconditions:
        - 0 < min_step <= max_step <= goal
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.current = 0
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        loser = self.whose_turn(self.turn)
        winner = self.whose_turn(self.turn - 1)
        winner.record_win()
        loser.record_loss()
        return winner.name

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number."""
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def play_one_turn(self) -> None:
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.
        Print the move and the new total.
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(self.current, self.min_step, self.max_step, self.goal)
        self.current += amount

        # We set a hard limit on self.current
        # (This is a strange corner case: don't worry about it!)
        if self.current > self.goal:
            self.current = self.goal

        self.turn += 1

        print(f'{next_player.name} moves {amount}.')
        print(f'Total is now {self.current}.')


################################################################################
# Implement your Player class and it subclasses below!
################################################################################
# TODO: Write classes Player, RandomPlayer, UserPlayer, and StrategicPlayer.


class Player:
    """The parent class of players for the NumberGame
    This is an abstract class, only subclasses should be initiated

    Attributes:
    - name:
        The name of the Player
    - num_of_wins:
        The number of wins of the Player
    - num_of_losses
        The number of losses of the Player

    Representation Invariants:
    - num_of_wins >= 0
    - num_of_losses >= 0
    - len(name) > 0
    """

    name: str
    num_of_wins: int
    num_of_losses: int

    def __init__(self, name) -> None:
        """Initialize this Player.

        Preconditions:

        """
        self.name = name
        self.is_turn = False
        self.num_of_wins = 0
        self.num_of_losses = 0
        self.move = 0

    def move(self) -> int:
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self) -> None:
        Player.__init__(self)

    def move(self) -> int:
        top = min(NumberGame.max_step, (NumberGame.goal - NumberGame.current))
        return random.randint(NumberGame.min_step, top)


class UserPlayer(Player):
    def __init__(self) -> None:
        Player.__init__(self)

    def move(self) -> int:
        move_num = int(input('Enter a move between 1 and 3: ').strip())
        return move_num


# class StrategicPlayer(Player):
#
#     def __init__(self) -> None:
#         Player.__init__()
#
#     def move(self) -> int:


@check_contracts
def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    return RandomPlayer(name)


################################################################################
# The main game program
################################################################################
k

    # Uncomment to check your work with python_ta!
    import python_ta

    python_ta.check_all(
        config={
            'extra-imports': ['random'],
            'allowed-io': ['main', 'make_player', 'UserPlayer.move', 'NumberGame.play_one_turn'],
            'max-line-length': 100,
        }
    )
