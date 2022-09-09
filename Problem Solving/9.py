"""
Author: passa-
Problem: 09 CSV Decorate
Student Code: 6510503310
Branch: Computer Engineering
"""

## not finished yet ##

def r_input():
    txt = input()
    return txt

def solve(txt):
    new_txt = ""
    word = ""
    for i in range(len(txt)):
        if txt[i] == "," and i == len(txt)-1:
            new_txt += "\"" + word.strip() + "\"," + "\"" + "" + "\""
        elif txt[i] == ",":
            new_txt += "\"" + word.strip() + "\","
            word = ""
        elif i == len(txt)-1:
            word += txt[i]
            new_txt += "\"" + word.strip() + "\""
        else:
            word += txt[i]
    return new_txt

## main ##

txt = r_input()
print(solve(txt))