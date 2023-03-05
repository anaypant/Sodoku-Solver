import random


def generate_board():
    # Start with a blank board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill in the diagonal boxes with random permutations of 1-9
    for i in range(0, 9, 3):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for j in range(3):
            for k in range(3):
                board[i + j][i + k] = nums.pop()

    # Use backtracking to fill in the rest of the board
    solve(board)

    # Randomly remove some values to create a puzzle
    for i in range(81):
        row = i // 9
        col = i % 9
        if random.randint(0, 8) < 6:
            board[row][col] = 0

    return board


def solve(board):
    # Find the next empty cell to fill
    row, col = find_empty(board)
    if row is None:
        return True

    # Try each possible value in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    # Backtrack if none of the values worked
    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


def is_valid(board, row, col, num):
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True
