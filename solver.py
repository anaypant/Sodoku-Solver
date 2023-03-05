def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using a backtracking algorithm.

    Args:
        board (list of lists): a 2D list representing the Sudoku puzzle

    Returns:
        list of lists: the solved Sudoku puzzle or -1 if the puzzle is unsolvable
    """

    def find_empty_cell():
        """
        Finds the next empty cell in the Sudoku puzzle.

        Returns:
            tuple: the row and column of the next empty cell, or None if there are no more empty cells
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(row, col, num):
        """
        Determines whether the given number is valid for the given cell in the Sudoku puzzle.

        Args:
            row (int): the row of the cell to check
            col (int): the column of the cell to check
            num (int): the number to check

        Returns:
            bool: True if the number is valid, False otherwise
        """
        # Check row
        if num in board[row]:
            return False

        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False

        # Check box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve():
        """
        Recursively solves the Sudoku puzzle using a backtracking algorithm.

        Returns:
            bool: True if the puzzle is solvable, False otherwise
        """
        cell = find_empty_cell()

        if cell is None:
            return True

        row, col = cell

        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num

                if solve():
                    return True

                board[row][col] = 0

        return False

    if not solve():
        return -1

    return board
