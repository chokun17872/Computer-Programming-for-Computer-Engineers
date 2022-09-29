"""
Author: passa-
Problem: 11 L12 Sequence draw
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("File name: ")
    lines = open(file_name).read().splitlines()
    data = {}
    picture = []
    num = lines[0]

    for i in range(1, len(lines)):
        if len(lines[i]) == 1:
            data[num] = picture
            num = lines[i]
            picture = []
        else:
            picture.append(lines[i])

    return data

def solve(data):
    data = dict(sorted(data.items(), key = lambda x:x[0]))
    for picture in data.values():
        for part in picture:
            print(part)

## main ##

data = read_file()
solve(data)