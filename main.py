def is_valid_board(board):
    def valid(unit):
        unit = [num for num in unit if num != 0] #Remove zeros
        return len(unit) == len(set(unit)) #Remove duplicates

    def valid_row(board):
        for row in board:
            if not valid(row):
                return False
            return True

    def valid_col(board):
        for col in zip(*board):
            if not valid(col):
                return False
            return True

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(board[row + i][col + j])
            if not valid(subgrid):
                return False
    return True


def is_valid(board, row, col, num):
    # Checks if num is in row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Checks if num is in that 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True 

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0 

    return False

def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()

# Test board
board = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if is_valid_board(board):
    if solve_sudoku(board):
        print("Sudoku solved successfully:")
        print_board(board)
else:
    print("Given board is not valid. Please try again")

