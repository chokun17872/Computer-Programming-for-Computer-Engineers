"""
Author: passa-
Problem: 04 Data Hash
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    return input().split()

def solve(word):
    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    word = word.upper()
    val = 0
    for i in range(len(word)):
        val += alpha.index(word[i]) + i
    return val

## main ##

txt = r_input()
ans = 0

for word in txt:
    ans += solve(word)

print(ans)