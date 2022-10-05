"""
Author: passa-
Problem: 06 Count All Characters
Student Code: 6510503310
Branch: Computer Engineering
"""

def gen_dict(txt):
    dct = {}
    found = []
    for letter in txt:
        if letter == " ":
            continue
        if letter not in found:
            found.append(letter)
            dct[letter] = txt.count(letter)
        else:
            continue
    return dct

def print_res(dct):
    print(dct)
    for key, value in dct.items():
        print(f"There are {value} " + key + "'s")

## main ##

txt = input("Enter text: ")
dct = gen_dict(txt)
print_res(dct)