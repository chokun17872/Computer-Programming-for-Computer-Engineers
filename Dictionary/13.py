"""
Author: passa-
Problem: 13 Chemical Formula (version 2)
Student Code: 6510503310
Branch: Computer Engineering
"""

def split_string(formula):
    formula_lst = []
    chem = formula[0]
    for i in range(1, len(formula)):
        if i == len(formula) - 1:
            if formula[i].isupper():
                formula_lst.append(chem)
                chem = formula[i]
            else:
                chem += formula[i]
            formula_lst.append(chem)
        elif formula[i].isupper():
            formula_lst.append(chem)
            chem = formula[i]
        else:
            chem += formula[i]
    return formula_lst

def gen_dict(formula_lst):
    dct = {}
    for i in formula_lst:
        chem = ""
        num = ""
        is_chem = True
        for j in i:
            if j.isalpha() == False:
                is_chem = False
            if is_chem:
                chem += j
            else:
                num += j
        if len(num) == 0: num = 1
        num = int(num)
        if chem not in dct.keys():
            dct[chem] = num
        else:
            dct[chem] += num
    return dct

## main ##

formula = input()
formula_lst = split_string(formula)
formula_dct = gen_dict(formula_lst)
find = input()

if find not in formula_dct.keys():
    print(0)
else: print(formula_dct[find])