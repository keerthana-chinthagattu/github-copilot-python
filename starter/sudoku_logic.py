import random
from copy import deepcopy


class SudokuEngine:
    def __init__(self):
        self.size = 9
        self.box = 3

    def create_puzzle(self, blanks=40):
        board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self._generate(board)
        solution = deepcopy(board)
        self._hide_numbers(board, blanks)
        return board, solution

    def validate(self, board):
        copied = deepcopy(board)
        return self._solve(copied)

    # ---------- Puzzle Generation ----------

    def _generate(self, board):
        empty = self._next_empty(board)
        if empty is None:
            return True

        row, col = empty
        values = list(range(1, 10))
        random.shuffle(values)

        for value in values:
            if self._can_place(board, row, col, value):
                board[row][col] = value
                if self._generate(board):
                    return True
                board[row][col] = 0

        return False

    # ---------- Sudoku Solver ----------

    def _solve(self, board):
        position = self._next_empty(board)
        if position is None:
            return True

        row, col = position

        for value in range(1, 10):
            if self._can_place(board, row, col, value):
                board[row][col] = value
                if self._solve(board):
                    return True
                board[row][col] = 0

        return False

    # ---------- Helpers ----------

    def _next_empty(self, board):
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == 0:
                    return (r, c)
        return None

    def _can_place(self, board, row, col, value):
        if value in board[row]:
            return False

        for r in range(self.size):
            if board[r][col] == value:
                return False

        start_row = (row // self.box) * self.box
        start_col = (col // self.box) * self.box

        for r in range(start_row, start_row + self.box):
            for c in range(start_col, start_col + self.box):
                if board[r][c] == value:
                    return False

        return True

    def _hide_numbers(self, board, blanks):
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)

        for row, col in cells[:blanks]:
            board[row][col] = 0


# ---------- Public Functions ----------

engine = SudokuEngine()


def generate_sudoku(empty_cells=40):
    puzzle, solution = engine.create_puzzle(empty_cells)
    return {
        "board": puzzle,
        "solution": solution
    }


def check_solution(board):
    return engine.validate(board)
