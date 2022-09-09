"""
Author: passa-
Problem: Parentheses ครบคู่ไหมนะ
Student Code: 6510503310
Branch: Computer Engineering
"""

class py_solution:
    def __init__(self,paren):
        self.paren = paren

    def is_valid_parentheses(self):
        stack = []
        o_bracket = ["(","[","{"]
        c_bracket = [")","]","}"]
        
        if len(self.paren) == 1: return False

        for i in range(len(self.paren)):
            if len(stack) == 0:
                stack.append(self.paren[i])
            elif self.paren[i] in o_bracket:
                stack.append(self.paren[i])
            elif self.paren[i] in c_bracket:
                if c_bracket.index(self.paren[i]) == o_bracket.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        return True

## main ##

paren = py_solution(input("input: "))

if paren.is_valid_parentheses():
    print("valid parentheses")
else:
    print("invalid parentheses")