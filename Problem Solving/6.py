"""
Author: passa-
Problem: 06 Largest Rectangle in a Histogram
Student Code: 6510503310
Branch: Computer Engineering
"""

## not finished yet ##

def r_input():
    n = int(input())
    histo = []
    for i in range(n):
        histo.append(int(input()))
    return n,histo

def solve(n,histo):
    area = []
    for i in range(n):
        length = 0
        for j in range(i,n):
            if histo[j] >= histo[i]:
                length += 1
            else: break
        area.append(histo[i] * length)
    return sorted(area)[-1]

## main ##

n,histo = r_input()
print(solve(n,histo))