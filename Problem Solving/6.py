"""
Author: passa-
Problem: 06 Largest Rectangle in a Histogram
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    n = int(input())
    histo = []
    for i in range(n):
        histo.append(int(input()))
    return histo

def solve(histo):
    area_lst = []
    for i in range(len(histo)):
        for j in range(i,len(histo)):
            height = min(histo[i:j+1])
            length = j-i+1
            area = height * length
            area_lst.append(area)
    return max(area_lst)

## main ##

histo = r_input()
print(solve(histo))