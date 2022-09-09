"""
Author: passa-
Problem: 11 Labsident Evil
Student Code: 6510503310
Branch: Computer Engineering
"""

from math import ceil

def r_input():
    dmg = int(input())
    zombies = list(map(int, input().split()))
    return dmg,zombies

def solve(dmg,zombies):
    bullet_lst = [ceil(zombie/dmg) for zombie in zombies]
    total_bullet = sum(bullet_lst)
    for i in range(1,len(bullet_lst)):
        bullet_lst[i] = bullet_lst[i] + bullet_lst[i-1]
    return bullet_lst,total_bullet

def print_ans(bullet_lst, total_bullet):
    print(total_bullet)
    for bullet in bullet_lst:
        print(bullet, end=" ")

## main ##

dmg,zombies = r_input()
bullet_lst,total_bullet = solve(dmg,zombies)
print_ans(bullet_lst,total_bullet)