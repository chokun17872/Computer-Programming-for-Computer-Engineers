"""
Author: passa-
Problem: 05 L14 Question #1
Student Code: 6510503310
Branch: Computer Engineering
"""

import csv

def read_file():
    file_name = input("Enter File name: ")
    with open(file_name) as file:
        datas = csv.reader(file)
        data = [i for i in datas]
    return data

def print_res(data):
    for country in data:
        if country[2] == "no" and country[3] == "yes":
            print(f"{country[0]} {country[1]}")

## main ##

data = read_file()
print_res(data)