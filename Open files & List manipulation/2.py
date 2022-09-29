"""
Author: passa-
Problem: 02 Score Statistics from File
Student Code: 6510503310
Branch: Computer Engineering
"""

file_name = input("Enter score file: ")
lines = open(file_name).read().splitlines()
scores = [int(line) for line in lines if line != ""]

for i in range(len(scores)):
    print(f"Student #{i+1} score: {scores[i]}")

print(f"Average score is {sum(scores)/len(scores):.2f}")
print(f"Minimum score is {min(scores)}")
print(f"Maximum score is {max(scores)}")