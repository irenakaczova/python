matrix = ((1, -2, 5, 20), (0, 2, 3, 400), (100, 2, 3, 4))
summation = 0
maximal = None

for row_number, row in enumerate(matrix):
    print(row_number, row)
    summation += sum(row)

    if maximal:
        maximal = max(maximal, max(row))
    else:
        maximal = max(row)

print(f"maximal={maximal}, summation={summation}")