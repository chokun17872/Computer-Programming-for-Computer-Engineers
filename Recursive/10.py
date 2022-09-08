"""
Author: passa-
Problem: 10 หารากที่สาม
Student Code: 6510503310
Branch: Computer Engineering
"""


def newton_cuberoot(x,y):
    new_x = ((y/x**2) + 2*x) / 3
    if abs(new_x**3-y) <= 10**(-6):
        return ((y/x**2) + 2*x) / 3
    return newton_cuberoot(((y/x**2) + 2*x) / 3, y)

def cuberoot(y):
  return newton_cuberoot(1.0, y)

print(cuberoot(7514))