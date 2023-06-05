#!/usr/bin/python3

"""

nqueens backtracks program to print the coordinates of n queens

on an nxn grid so that they are all in non-attacking positions

"""

import sys

def is_safe(board, row, col):

    # Check if it is safe to place a queen at board[row][col]

    # Check the left side of the current column

    for i in range(col):

        if board[row][i] == 1:

            return False

    # Check the upper diagonal on the left side

    i, j = row, col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:

            return False

        i -= 1

        j -= 1

    # Check the lower diagonal on the left side

    i, j = row, col

    while i < len(board) and j >= 0:

        if board[i][j] == 1:

            return False

        i += 1

        j -= 1

    return True

def solve_nqueens(board, col, solutions):

    # Base case: If all queens are placed, append the current solution

    if col == len(board):

        solution = []

        for i in range(len(board)):

            for j in range(len(board)):

                if board[i][j] == 1:

                    solution.append([i, j])

        solutions.append(solution)

        return

    # Recursive case: Try placing a queen in each row of the current column

    for i in range(len(board)):

        if is_safe(board, i, col):

            board[i][col] = 1

            solve_nqueens(board, col + 1, solutions)

            board[i][col] = 0

def print_solutions(solutions):

    for solution in solutions:

        print(solution)

def nqueens(n):

    if not isinstance(n, int):

        print("N must be a number")

        sys.exit(1)

    if n < 4:

        print("N must be at least 4")

        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    solutions = []

    solve_nqueens(board, 0, solutions)

    print_solutions(solutions)

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: nqueens N")

        sys.exit(1)

    try:

        n = int(sys.argv[1])

        nqueens(n)

    except ValueError:

        print("N must be a number")

        sys.exit(1)
