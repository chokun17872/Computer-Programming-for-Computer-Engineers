"""
Author: passa-
Problem: 06 L14 Question #2
Student Code: 6510503310
Branch: Computer Engineering
"""

import csv

def read_file():
    file_name = input("Enter file name: ")
    with open(file_name) as file:
        datas = csv.reader(file)
        data = [i for i in datas]
    return data

def solve(data):
    temp_list = [float(city[4]) for city in data if data.index(city) != 0]
    avg = sum(temp_list) / len(temp_list)
    temp_list.sort()
    minn, maxx = temp_list[0], temp_list[-1]
    return avg, minn, maxx

## main ##

data = read_file()
avg, minn, maxx = solve(data)

print(f"Minimum: {minn:.2f}")
print(f"Maximum: {maxx:.2f}")
print(f"Average temperature: {avg:.4f}")