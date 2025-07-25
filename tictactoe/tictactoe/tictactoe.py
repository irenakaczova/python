import random
import typing
from collections.abc import Iterable
from .stone import Stone

class TicTacToe:
    """Represents the TicTacToe game."""

    def __init__(self) -> None:
        """Game set up: creats the board, sets turn number, randomly picks first stone, sets winner to none. """

        self.board = [[" "] * 3 for _ in range(3)]
        self.turn = 1
        # randomly picks first stone
        self.active_stone = random.choice([Stone.X, Stone.O])
        self.winner = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(3x3, turn={self.turn}, active_stone={self.active_stone}, winner={self.winner})"

    def __str__(self) -> str:
        board = "\n––––––––––\n".join([" | ".join(map(str, row)) for row in self.board])
        round = f"Turn: {self.turn}"
        stone = f"Stone on turn: {self.active_stone}"
        winner = f"Winner: {self.winner if self.winner else ''}"

        return "\n".join([board, round, stone, winner])

    def play(self, x: int, y: int) -> 'TicTacToe':
        """Places stone on the board according to given coordinates.

        Args:
            x (int): number on horizontal axis
            y (int): number on vertical axis

        Raises:
            ValueError: if coords are out of range
            ValueError: if game already has a winner
            ValueError: if coords already contain a stone
        """
        # if coords are out of range
        if not ((0 <= abs(x) <= 2) and (0 <= abs(y) <= 2)):
            raise ValueError(f"Coordinates must be from [0, 2] interval, x: {x} y: {y} were given.")

        # if game already has a winner
        if self.winner:
            raise ValueError(f"Game is over (winner is: {self.winner}).")

        # if coords already contain a stone
        if self.board[x][y] != " ":
            raise ValueError(f"Position {x},{y} is already occupied.")

        # place stone
        self.board[x][y] = self.active_stone
        # increment turn number
        self.turn += 1
        # eval game
        self.winner = self.eval()

        # move to next turn (when there is no winner)
        if not self.winner:
            self.active_stone = Stone.X if self.active_stone is Stone.O else Stone.O

        return self

    def _all_active_stones(self, iterable: Iterable) -> bool:
        # test if iterable contains only active stones
        return all((stone is self.active_stone for stone in iterable))

    def eval(self) -> typing.Optional[str]:
        """Test for winner.

        Returns:
            typing.Optional[str]: returns winner or None
        """
        board_T = tuple(zip(*self.board))

        diagonal = (self.board[idx][idx] for idx in range(3))
        diagonal_T = (self.board[0][2], self.board[1][1], self.board[2][0])

        # test if some row contains winning possition
        test_rows = any((self._all_active_stones(row) for row in self.board))
        # test if some column contains winning possition
        test_columns = any((self._all_active_stones(column) for column in board_T))
        # test if diagonal contains winning possition
        test_diagonal = self._all_active_stones(diagonal)
        # test if another diagonal contains winning possition
        test_diagonal_T = self._all_active_stones(diagonal_T)

        # eval winner
        if test_rows or test_columns or test_diagonal or test_diagonal_T:
            return self.active_stone

        return None

