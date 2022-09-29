"""
Author: passa-
Problem: 13 L12 Computer5
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("filename: ")
    lines = open(file_name).read().splitlines()
    data = [line.lower().split() for line in lines if line != ""]
    return data

def gen_target():
    target = []
    for word in ["computer", "computers"]:
        for mark in ["!","?",".",""]:
            target.append(word+mark)
    return target

def solve(data):
    target = gen_target()
    count = 0
    for line in data:
        for word in line:
            if word in target:
                count += 1
    return count

## main ##

data = read_file()
print(f"Count = {solve(data)}")