"""
Author: passa-
Problem: 07 L12 Exam2
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    name, score = input().split()
    return name, int(score)

def is_exist(all_data, name):
    for data in all_data:
        if data["name"] == name:
            return True
    return False

def solve():
    pass

## main ##

# all_data = []
# n = int(input("Number of inputs: "))
# for i in range(n):
#     name, score = r_input()
#     if is_exist(all_data, name) == False:
#         data = {
#             "name": name,
#             "score": score,
#             "count": 1
#         }
#     else:
        
        