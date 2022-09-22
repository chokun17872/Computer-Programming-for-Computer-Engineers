"""
Author: passa-
Problem: 06 L12 Zoo
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    animal, food = input().split()
    return animal, food

def print_res(data, animal):
    if animal not in data:
        print("Sorry we don't have that animal.")
    else:
        print(f"{data[animal]}")

## main ##

data = {}
n = int(input("How many animals are there in the zoo? : "))
for i in range(n):
    animal, food = r_input()
    data[animal] = food

q = int(input("How many questions do you want to ask? : "))
for i in range(q):
    animal = input()
    print_res(data, animal)