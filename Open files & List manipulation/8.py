"""
Author: passa-
Problem: 08 L12 best quiz upgrade
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("File name: ")
    lines = open(file_name).readlines()
    name_lst = []
    score_lst = []

    for line in lines:
        if line == "":
            continue
        name_lst.append(line.split()[0])
        score_lst.append([int(score) for score in line.split()[1:]])

    return name_lst, score_lst

def find_max(name_lst, score_lst):
   new_score_lst = [sum(sorted(score)[1:-1]) for score in score_lst]
   max_score = max(new_score_lst)
   print(max_score)
   
   for i in range(len(name_lst)):
        if new_score_lst[i] == max_score:
            print(name_lst[i])

## main ##

name_lst, score_lst = read_file()
find_max(name_lst, score_lst)