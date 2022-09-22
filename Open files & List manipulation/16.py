"""
Author: passa-
Problem: 16 L12 word_chain
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    return input("Text: ").split()

def check_chain(chain, other):
    count = 0
    for i in range(len(chain)):
        if chain[i] != other[i]:
            count += 1
    if count <= 2:
        return True
    return False

def solve(text):
    chain_cnt = 1
    mx_length = 0
    length = 1
    for i in range(len(text)-1):
        if check_chain(text[i], text[i+1]) == False:
            chain_cnt += 1
            length = 1
        else:
            length += 1
            mx_length = max(mx_length, length)
    return chain_cnt, mx_length

## main ##

text = r_input()
chain_cnt, mx_length = solve(text)
print(f"{chain_cnt} Chain(s). Maximum length is {mx_length} word(s).")