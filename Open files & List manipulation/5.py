"""
Author: passa-
Problem: 05 L12 Exam1
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    name, score = input().split()
    return name, score

def print_res(data, name):
    print(f"{name}'s score is {data[name]}")

## main ##

data = {}
n = int(input("Number of inputs: "))
for i in range(n):
    name, score = r_input()
    data[name] = score

while True:
    name = input("student: ")
    if len(name) == 0:
        print("End")
        break
    print_res(data,name)