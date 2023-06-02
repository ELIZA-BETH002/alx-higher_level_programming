#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix containing integers or floats.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of lists: A new matrix with elements divided by the given number,
                      rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_rows = len(matrix)
    if num_rows == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    num_cols = len(matrix[0])

    for row in matrix:
        if len(row) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
