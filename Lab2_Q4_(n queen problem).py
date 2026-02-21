
# N-Queen Problem using Backtracking (DFS Search)

def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queen(n):
    board = [-1] * n

    def backtrack(row):
        if row == n:
            print_solution(board, n)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    backtrack(0)


def print_solution(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()



    solve_n_queen(n)
