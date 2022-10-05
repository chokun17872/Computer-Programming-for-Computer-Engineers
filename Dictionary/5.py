"""
Author: passa-
Problem: 05 Simple Scores
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_name():
    name = input("Enter name: ")
    return name

def r_input(dct, name):
    score = float(input("Enter scores: "))
    dct[name] = score
    return dct

def avg_score(dct):
    total = 0
    count = 0
    for value in dct.values():
        if value < 60:
            total += value
            count += 1
    if count == 0: return count
    return total/count

def print_res(dct):
    print(dct)
    for key, value in dct.items():
        print(key, "got" , f"{value:.2f}")
    if avg_score(dct) != 0 :
        print(f"Average scores of students who got below 60 = {avg_score(dct):.2f}")
    else: print("No one got below 60.")
    
## main ##

dct = {}

while True:
    name = r_name()
    if name == "Q":
        break
    dct = r_input(dct, name)

print_res(dct)