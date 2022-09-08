"""
Author: passa-
Problem: 05 2 4 6 8 10 12
Student Code: 6510503310
Branch: Computer Engineering
"""

def divnums(n, d):
    if n == 1:
        return ""
    if n%d == 0:
        return f"{divnums(n-1,d)}{str(n)} "
    else:
        return f"{divnums(n-1,d)}"

print(divnums(10,3))
print(len(divnums(10,3)))