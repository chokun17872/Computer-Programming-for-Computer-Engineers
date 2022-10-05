"""
Author: passa-
Problem: 09 L12 Matrix
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("File name: ")
    lines = open(file_name).read().splitlines()
    matrix_lst = []
    op_lst = []
    row = []

    for i in range(len(lines)):
        if lines[i] == "":
            continue
        if lines[i] in ["+","-","*"]:
            op_lst.append(lines[i])
            matrix_lst.append(row)
            row = []
        else:
            row.append(list(map(int, lines[i].split())))
        if i == len(lines)-1:
            matrix_lst.append(row)

    print(matrix_lst)
    return matrix_lst, op_lst

def zero_matrix(r,c):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        matrix.append(row)
    return matrix

def plus(matA, matB):
    matrix = zero_matrix(len(matA),len(matA[0]))
    for i in range(len(matA)):
        for j in range(len(matB)):
            matrix = matA[i][j] + matB[i][j]
    return matrix

def minus(matA, matB):
    matrix = zero_matrix(len(matA),len(matA[0]))
    for i in range(len(matA)):
        for j in range(len(matB)):
            matrix = matA[i][j] - matB[i][j]
    return matrix

def multiply(matA, matB):
    matrix = zero_matrix(len(matA),len(matB[0]))
    ## result r=len(matA) c=len(matB[0])
    for i in range(len(matA)):
        for j in range(len(matB)):
            total = 0
            for k in range(len(matA)):
                total += matA[j][k] * matB[k][j]
            matrix[i][j] = total
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:^5}",end=" ")
        print()

def solve(matrix_lst, op_lst):
    matrix = matrix_lst[0]
    for i in range(len(op_lst)):
        if op_lst[i] == "+":
            print(matrix)
            print(matrix[i+1])
            matrix = plus(matrix, matrix_lst[i+1])
        elif op_lst[i] == "-":
            matrix = minus(matrix, matrix_lst[i+1])
        elif op_lst[i] == "*":
            matrix = multiply(matrix, matrix_lst[i+1])
    return matrix

## main ##

matrix_lst, op_lst = read_file()
res_matrix = solve(matrix_lst, op_lst)
print(res_matrix)
# print_matrix(res_matrix)