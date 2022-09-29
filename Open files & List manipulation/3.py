"""
Author: passa-
Problem: 03 GPA Calculator
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("Enter grade file: ")
    lines = open(file_name).read().splitlines()
    subj_lst = []
    cred_lst = []
    grade_lst = []

    for line in lines:
        if line == "":
            continue
        subj, cred, grade = line.split(",")
        subj_lst.append(subj)
        cred_lst.append(int(cred))
        grade_lst.append(grade)

    return subj_lst, cred_lst, grade_lst

def get_point(grade):
    if grade == "A":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D":
        return 1.0
    elif grade == "F":
        return 0.0

def print_data(subj_lst, cred_lst, grade_lst):
    for i in range(len(subj_lst)):
        print(f"subject: {subj_lst[i]} credits: {cred_lst[i]} grade: {grade_lst[i]:^2} point: {get_point(grade_lst[i])}")

    total =  0
    for i in range(len(subj_lst)):
        total += cred_lst[i] * get_point(grade_lst[i])

    print(f"Total credits = {sum(cred_lst)}")
    print(f"GPA = {total/sum(cred_lst):.2f}")

## main ##

subj_lst, cred_lst, grade_lst = read_file()
print_data(subj_lst, cred_lst, grade_lst)