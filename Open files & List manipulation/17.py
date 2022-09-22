"""
Author: passa-
Problem: 17 L12 plusNamNuk
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    cow_weight = {}
    n = int(input("N : "))
    for i in range(n):
        name, weight = input().split()
        cow_weight[name] = int(weight)
    question = input().split("+")
    striped_question = []
    for q in question:
        striped_question.append(q.strip())
    return cow_weight,striped_question

def solve(cow_weight,question):
    total_weight = 0
    for q in question:
        total_weight += cow_weight[q]
    return total_weight

## main ##

n,cow_weight,question = r_input()
print(solve(cow_weight,question))