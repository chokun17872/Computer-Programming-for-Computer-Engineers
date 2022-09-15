"""
Author: passa-
Problem: 05 Paint Brush
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    m,n = map(int, input().split("*"))
    board = []
    for i in range(n):
        board.append(input())
    brush = input().split(" ")
    x,y,size,color = [int(brush[i]) if i < 3 else brush[i] for i in range(4)]
    return board,m,n,x,y,size,color

def solve(board,m,n,x,y,size,color):
    st_x = x-size if x-size >= 1 else 1
    en_x = x+size if x+size <= m else m
    st_y = y-size if y-size >= 1 else 1
    en_y = y+size if y+size <= n else n
    target = board[y-1][x-1]
    new_board = []
    for i in range(1,n+1):
        row = []
        for j in range(1,m+1):
            if i >= st_y and i <= en_y and j >= st_x and j <= en_x and board[i-1][j-1] == target:
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

board,m,n,x,y,size,color = r_input()
new_board = solve(board,m,n,x,y,size,color)
print_board(new_board,m,n)