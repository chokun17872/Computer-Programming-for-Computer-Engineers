"""
Author: passa-
Problem: [ClassMatrix] เมตริกซ์
Student Code: 6510503310
Branch: Computer Engineering
"""

class Matrix:
    def __init__(self,data):
        self.data = data

    def show(self):
        for i in range(3):
            for j in range(3):
                print(f'{self.data[i][j]:^6}', end = ' ')
            print()

    def zero_matrix(self):
        matrix = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(0)
            matrix.append(row)
        return matrix

    def plus(self,other):
        matrix = self.zero_matrix()
        for i in range(3):
            for j in range(3):
                matrix[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(matrix)

    def minus(self,other):
        matrix = self.zero_matrix()
        for i in range(3):
            for j in range(3):
                matrix[i][j] = self.data[i][j] - other.data[i][j]
        return Matrix(matrix)

    def multiply(self,other):
        data = self.zero_matrix()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    data[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(data)

    def det(self):
        result = 0
        for i in range(6):
            if i <= 2:
                result += self.data[0][i%3]*self.data[1][(i+1)%3]*self.data[2][(i+2)%3]
            else:
                result -= self.data[2][i%3]*self.data[1][(i+1)%3]*self.data[0][(i+2)%3]
        return result

def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

## main ##

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()