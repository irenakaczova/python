from itertools import compress, chain

def rows_even_numbers(matrix, row_mask):
    """Returns iterator that creats all even numbers selected from rows corresponding with given mask."""
    return filter(lambda x: x % 2 == 0, chain.from_iterable(compress(matrix, row_mask)))