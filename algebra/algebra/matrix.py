from .vector import dot_product

def matrix_multiplication(matrix_1, matrix_2):
    """Returns result matrix of matrix multiplication."""

    if len(matrix_1[0]) != len(matrix_2):
        raise ValueError(f"Dimensions of given matrices are incompatible, {len(matrix_1[0])} and {len(matrix_2)} was given.")

    result_matrix = []
    for idx_row, row_matrix_1 in enumerate(matrix_1):
        result_matrix.append([])
        for row_matrix_2 in zip(*matrix_2):
            result_matrix[idx_row].append(dot_product(row_matrix_1, row_matrix_2))
            
    return result_matrix
        

def new_matrix(shape, fill):
    """Returns new matrix."""

    matrix = []
    row, column = shape
    for _ in range(row):
        matrix.append([fill] * column)

    return matrix
           

def submatrix(matrix, drop_rows=[], drop_columns=[]):
    """Returns submatrix."""
    
    new_submatrix = []
    for idx_row, row in enumerate(matrix):
        new_row = []
        for idx_column, column in enumerate(row):
            if idx_column not in drop_columns and idx_row not in drop_rows:
                new_row.append(matrix[idx_row][idx_column])
        if new_row:
            new_submatrix.append(new_row)

    return new_submatrix