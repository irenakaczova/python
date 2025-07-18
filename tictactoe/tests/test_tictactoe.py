import pytest
from tictactoe.tictactoe import TicTacToe
from tictactoe.tictactoe import Stone

@pytest.fixture
def test_game():
    return TicTacToe()

def test_tictactoe(test_game):
    assert test_game.board == [[" "] * 3 for _ in range(3)]
    assert test_game.turn == 1
    assert True == (test_game.active_stone == Stone.X) or (test_game.active_stone == Stone.O)
    assert test_game.winner == None

def test_all_active_stones(test_game):
    test_game.play(0, 0).play(0, 1).play(1,1).play(2, 0).play(2, 2)
    diagonal = (test_game.board[idx][idx] for idx in range(3))

    assert test_game._all_active_stones(diagonal) == True
    
def test_repr_(test_game):
    assert repr(test_game) == f"{test_game.__class__.__name__}(3x3, turn={test_game.turn}, active_stone={test_game.active_stone}, winner={test_game.winner})"

def test_str_(test_game):
    board = "\n––––––––––\n".join([" | ".join(map(str, row)) for row in test_game.board])
    round = f"Turn: {test_game.turn}"
    stone = f"Stone on turn: {test_game.active_stone}"
    winner = f"Winner: {test_game.winner if test_game.winner else ''}"

    assert str(test_game) == "\n".join([board, round, stone, winner])

def test_play_turn(test_game):
    active_stone = test_game.active_stone

    test_game.play(0, 0)
    
    assert test_game.turn == 2
    assert test_game.board[0][0] == active_stone

def test_play_winner(test_game):
    active_stone = test_game.active_stone

    test_game.play(0, 0).play(0, 1).play(1,1).play(2, 0).play(2, 2)

    assert test_game.winner == active_stone

def test_play_return_value(test_game):
    assert test_game.play(0,0) == test_game

def test_play_invalid_coords(test_game):
    with pytest.raises(ValueError):
        test_game.play(4,8)

def test_play_game_over(test_game):
    test_game.winner = Stone.X

    with pytest.raises(ValueError):
        test_game.play(0,0)

def test_play_position_ocupied(test_game):
    test_game.play(0,0)

    with pytest.raises(ValueError):
        test_game.play(0,0)

@pytest.mark.parametrize(
    "coords",
    [([[0, 0],[1, 1],[0, 1],[2, 0],[0, 2]]),
     ([[1, 0],[0, 1],[1, 1],[2, 0],[1, 2]]),
     ([[2, 0],[1, 1],[2, 1],[0, 0],[2, 2]]),
     ([[0, 0],[1, 1],[1, 0],[2, 1],[2, 0]]),
     ([[0, 1],[1, 2],[1, 1],[2, 0],[2, 1]]),
     ([[0, 2],[1, 1],[1, 2],[2, 0],[2, 2]]),
     ([[0, 0],[1, 2],[1, 1],[2, 0],[2, 2]]),
     ([[0, 2],[1, 2],[1, 1],[2, 1],[2, 0]])],
)

def test_eval(test_game, coords):
    active_stone = test_game.active_stone
    test_game.play(coords[0][0], coords[0][1]).play(coords[1][0], coords[1][1]).play(coords[2][0], coords[2][1]).play(coords[3][0], coords[3][1]).play(coords[4][0], coords[4][1])
    assert test_game.eval() == active_stone
    