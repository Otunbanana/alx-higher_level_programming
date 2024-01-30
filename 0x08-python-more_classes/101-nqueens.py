#!/usr/bin/python3
"""
Module to solve the N-Queens problem and print solutions.
"""

import sys


class NQueensSolver:
    """
    Class to solve the N-Queens problem and print solutions.

    Attributes:
        N (int): The size of the chessboard and the number of queens.
        solutions (list): A list to store the solutions.
    """

    def __init__(self, N):
        """
        Initialize an instance of NQueensSolver.

        Args:
            N (int): The size of the chessboard and the number of queens.
        """
        self.N = N
        self.solutions = []

    def is_safe(self, board, row, col):
        """
        Check if it's safe to place a queen in the specified position.

        Args:
            board (list): Current state of the chessboard.
            row (int): Row to check.
            col (int): Column to check.

        Returns:
            bool: True if it's safe, False otherwise.
        """
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve_nqueens_util(self, board, col):
        """
        Utility function to solve the N-Queens problem.

        Args:
            board (list): Current state of the chessboard.
            col (int): Current column.

        Returns:
            None
        """
        if col == self.N:
            self.solutions.append(list(enumerate(board)))
            return

        for row in range(self.N):
            if self.is_safe(board, row, col):
                board[col] = row
                self.solve_nqueens_util(board, col + 1)
                board[col] = -1

    def solve_nqueens(self):
        """
        Solve the N-Queens problem and store solutions in the solutions list.

        Returns:
            None
        """
        board = [-1] * self.N
        self.solve_nqueens_util(board, 0)

    def print_solutions(self):
        """
        Print all solutions to the N-Queens problem.

        Returns:
            None
        """
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens_solver = NQueensSolver(N)
    nqueens_solver.solve_nqueens()
    nqueens_solver.print_solutions()
