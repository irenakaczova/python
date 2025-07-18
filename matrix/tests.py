import pytest
from typing  import Iterator

from matrix import rows_even_numbers


matrix = [[1, 2, 3, 4], [6, 7, 8, 9], [4, 5, 6, 7]]


@pytest.mark.parametrize(
    "matrix, mask, result",
    [
        (matrix, [True, False, True], [2, 4, 4, 6]), 
        (matrix, [False, False, False], []),
        (matrix, [True, False, False], [2, 4])],
)
def test_rows_even_numbers(matrix, mask, result):
    iterator = rows_even_numbers(matrix, mask)
    assert isinstance(iterator, Iterator)
    assert list(iterator) == result


def test_docstring():
    assert rows_even_numbers.__doc__
