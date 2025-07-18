def dot_product(vector_1, vector_2):
    """Returns the dot product."""
    
    if len(vector_1) != len(vector_2):
        raise ValueError(f"Vectors are not same length, {len(vector_1)} and {len(vector_2)} was given.")

    sum = 0
    for number_1, number_2 in zip(vector_1, vector_2):
        sum += number_1 * number_2
    return sum