class Player:
    """A player of a game.

    Attributes:
    - name: name of the player
    - history: a list of the last 100 scores
    """

    # Attribute types
    name: str
    history: list[int]

    def __init__(self, name: str):
        """Initialize this Player"""
        self.name = name
        self.history = []

    def add_score(self, score: int) -> None:
        """Add a new score to the Player history"""
        self.history.append(score)

    def top_score(self) -> int:
        """Returns the top score of the Player"""
        return max(self.history)

    def recent_average(self, n: int) -> int:
        total = 0
        for i in range(len(self.history) - 1, len(self.history) - n, -1):
            total += i

        return total / n
