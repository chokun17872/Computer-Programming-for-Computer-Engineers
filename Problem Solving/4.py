"""
Author: passa-
Problem: 05 Paint Brush
Student Code: 6510503310
Branch: Computer Engineering
"""

## not finished yet ##

def r_input():
    m,n = map(int, input().split("*"))
    board = []
    for i in range(n):
        row = input()
        board.append(row)
    brush = input().split()
    M,N,size,color = [int(brush[i]) if i < 3 else brush[i] for i in range(len(brush))]
    return board,m,n,M,N,size,color

def solve(board,m,n,M,N,size,color):
    if size == 0: return board
    st_x = M-size if M-size >= 1 else 1
    en_x = M+size if M+size <= m else m
    st_y = N-size if N-size >= 1 else 1
    en_y = N+size if N+size <= n else n
    old_color = board[N-1][M-1]
    new_board = []
    for i in range(1,n+1):
        row = []
        for j in range(1,m+1):
            if i >= st_y and i <= en_y and j >= st_x and j <= en_x and board[i-1][j-1] == old_color:
                row.append(color)
            else:
                row.append(board[i-1][j-1])
        new_board.append(row)
    return new_board

def print_board(board,m,n):
    for i in range(n):
        for j in range(m):
            print(board[i][j], end="")
        print()

## main ##

board,m,n,M,N,size,color = r_input()
new_board = solve(board,m,n,M,N,size,color)
print_board(new_board,m,n)