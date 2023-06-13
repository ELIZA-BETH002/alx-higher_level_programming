#!/usr/bin/python3

"""Module to multiply matrices using NumPy

"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):

    """Function to multiply two matrices using NumPy

    Args:

        m_a (list): First matrix

        m_b (list): Second matrix

    Returns:

        numpy.ndarray: Resultant matrix after multiplication

    Raises:

        ValueError: If the matrices cannot be multiplied

    """

    if not isinstance(m_a, list):

        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):

        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):

        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):

        raise TypeError("m_b must be a list of lists")

    if m_a == [] or any(row == [] for row in m_a):

        raise ValueError("m_a can't be empty")

    if m_b == [] or any(row == [] for row in m_b):

        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):

        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):

        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):

        raise ValueError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):

        raise ValueError("each row of m_b must be of the same size")

    try:

        result = np.dot(np.array(m_a), np.array(m_b))

    except ValueError as e:

        raise ValueError("m_a and m_b can't be multiplied") from e

    return result.tolist()
