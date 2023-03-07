def solve_sudoku(board):
    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(row, col, num):
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
