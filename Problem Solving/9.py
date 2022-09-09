"""
Author: passa-
Problem: 09 CSV Decorate
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    txt = input()
    return txt

def solve(txt):
    txt = txt.split(",")
    new_txt = ""
    for i in range(len(txt)):
        new_txt += f"\"{txt[i].strip()}\""
        if i != len(txt)-1:
            new_txt += ","
    return new_txt

## main ##

txt = r_input()
print(solve(txt))