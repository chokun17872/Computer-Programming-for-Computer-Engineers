"""
Author: passa-
Problem: 07 Elevator
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    elev = list(map(int, input().split()))
    st = int(input())
    return elev,st

def solve(elev,st):
    total = 0
    while len(elev) > 0:
        mn_diff = 99999999
        for floor in elev:
            diff = abs(st-floor)
            if diff < mn_diff:
                mn_diff = diff
                new_st = floor
        st = new_st
        total += mn_diff
        elev.remove(st)
    return total

## main ##

elev,st = r_input()
print(solve(elev,st))
