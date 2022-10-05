"""
Author: passa-
Problem: 19 L13 sibling
Student Code: 6510503310
Branch: Computer Engineering
"""

def gen_dct(n):
    dct = {}
    for i in range(n):
        info = input().split()
        a = info[0]
        b = info[4]
        if info[2] in ["father", "mother"]:
            if b not in dct.keys():        
                dct[b] = [a]
            else:
                dct[b].append(a) 
        else:
            dct[b] = []
    return dct

def is_sibling(dct,a,b):
    if a not in dct.keys() or b not in dct.keys():
        return "No"
    for parent_a in dct[a]:
        for parent_b in dct[b]:
            if parent_a == parent_b:
                return "Yes"
    else: return "No"

## main ##

n = int(input())
dct = gen_dct(n)
info = input().split()
a,b = info[1], info[3]
print(is_sibling(dct, a, b))