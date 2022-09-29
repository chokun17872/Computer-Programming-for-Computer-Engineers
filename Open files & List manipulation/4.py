"""
Author: passa-
Problem: 04 Oldest People
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("Enter age file: ")
    lines = open(file_name).readlines()
    name_lst = []
    age_lst = []

    for line in lines:
        if line == "":
            continue
        name, age = line.split(",")
        name_lst.append(name)
        age_lst.append(int(age))

    return name_lst, age_lst

def find_oldest(name_lst, age_lst):
    oldest = max(age_lst)
    print(f"Oldest person(s) with the age of {oldest}:")

    for i in range(len(name_lst)):
        if age_lst[i] == oldest:
            print(f"- {name_lst[i]}")

## main ##

name_lst, age_lst = read_file()
find_oldest(name_lst, age_lst)