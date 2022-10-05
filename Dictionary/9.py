"""
Author: passa-
Problem: 09 Count English Characters
Student Code: 6510503310
Branch: Computer Engineering
"""

def count_char(word):
    dct = {}
    for letter in word.lower():
        if not letter.isalpha():
            continue
        if letter not in dct.keys():
            dct[letter] = 1
        else:
            dct[letter] += 1
    return dct