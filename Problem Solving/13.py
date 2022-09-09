"""
Author: passa-
Problem: 13 String Is Immutable
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    string = input()
    idx = int(input())
    char = input()
    return string,idx,char

def solve(string,idx,char):
    new_string = ""
    for i in range(len(string)):
        if i == idx:
            new_string += char
        else:
            new_string += string[i]
    return new_string

## main ##

string,idx,char = r_input()
print(solve(string,idx,char))