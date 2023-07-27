#!/usr/bin/python3
"""0-nqueens module that solves the N queens problem
"""
import sys

def print_solution(board, N):
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append(j+1)
    print(", ".join(str(x) for x in solution))

def is_attack(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return True

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True

    return False

def solve_NQ(board, col, N):
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if not is_attack(board, i, col, N):
            board[i][col] = 1

            res = solve_NQ(board, col + 1, N) or res

            board[i][col] = 0  # backtrack

    return res

def solveNQ(N):
    board = [[0]*N for _ in range(N)]

    if not solve_NQ(board, 0, N):
        print("Solution does not exist")
        return False

    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQ(N)

if __name__ == "__main__":
    main()
