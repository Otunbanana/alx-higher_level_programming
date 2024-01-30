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
        board (list): A list of lists representing the chessboard.
        solutions (list): A list of lists containing solutions.
    """

    def __init__(self, N):
        """
        Initialize an instance of NQueensSolver.

        Args:
            N (int): The size of the chessboard and the number of queens.
        """
        self.N = N
        self.board = self.init_board()
        self.solutions = []

    def init_board(self):
        """Initialize an `N`x`N` sized chessboard with empty spots."""
        return [[' ' for _ in range(self.N)] for _ in range(self.N)]

    def is_safe(self, row, col):
        """
        Check if it's safe to place a queen in the specified position.

        Args:
            row (int): Row to check.
            col (int): Column to check.

        Returns:
            bool: True if it's safe, False otherwise.
        """
        for i in range(col):
            if self.board[i] == row or \
               self.board[i] - i == row - col or \
               self.board[i] + i == row + col:
                return False
        return True

    def x_out(self, row, col):
        """X out spots on the chessboard."""
        for c in range(col + 1, self.N):
            self.board[row][c] = 'x'
        for c in range(col - 1, -1, -1):
            self.board[row][c] = 'x'
        for r in range(row + 1, self.N):
            self.board[r][col] = 'x'
        for r in range(row - 1, -1, -1):
            self.board[r][col] = 'x'
        c = col + 1
        for r in range(row + 1, self.N):
            if c >= self.N:
                break
            self.board[r][c] = 'x'
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            self.board[r][c] = 'x'
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= self.N:
                break
            self.board[r][c] = 'x'
            c += 1
        c = col - 1
        for r in range(row + 1, self.N):
            if c < 0:
                break
            self.board[r][c] = 'x'
            c -= 1

    def solve_nqueens_util(self, col):
        """
        Utility function to solve the N-Queens problem.

        Args:
            col (int): Current column.

        Returns:
            None
        """
        if col == self.N:
            self.solutions.append([row[:] for row in self.board])
            return

        for row in range(self.N):
            if self.board[row][col] == ' ' and self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.x_out(row, col)
                self.solve_nqueens_util(col + 1)
                self.board[row][col] = ' '
                # Note: No need to undo x_out since we are backtracking

    def solve_nqueens(self):
        """
        Solve the N-Queens problem and store solutions in the solutions list.

        Returns:
            None
        """
        self.solve_nqueens_util(0)

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
