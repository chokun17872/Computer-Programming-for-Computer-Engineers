"""
Author: passa-
Problem: 03 Gibberish
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    txt = input()
    return txt[:int(len(txt)/2)],txt[int(len(txt)/2):]

def solve(txt):
    rev_txt = [txt[i] for i in range(len(txt)-1,-1,-1)]
    return "".join(rev_txt)

## main ##

n = int(input())
for i in range(n):
    txt1,txt2 = r_input()
    print(solve(txt1)+solve(txt2))