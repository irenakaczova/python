from enum import Enum
from tictactoe.tictactoe import Stone

def test_stone():
    assert isinstance(Stone.X, Enum)
    assert isinstance(Stone.O, Enum)
    assert str(Stone.X) == "X"
    assert str(Stone.O) == "O"
    