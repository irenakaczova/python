def arithmetic_progression(begin, step, end=None):
    """Generates arithmetic progression."""

    n = 1
    nth = begin

    while not end or nth < end:
        yield nth
        n = n + 1
        nth = begin + (n - 1) * step