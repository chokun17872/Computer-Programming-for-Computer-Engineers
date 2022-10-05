"""
Author: passa-
Problem: 08 Cloth Size
Student Code: 6510503310
Branch: Computer Engineering
"""

def cloth_size(width_list):
    dct = {"S": 0, "M": 0, "L": 0}
    for width in width_list:
        if width <= 36:
            dct["S"] += 1
        elif width <= 44:
            dct["M"] += 1
        else:
            dct["L"] += 1
    return dct