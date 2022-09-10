"""
Author: passa-
Problem: 02 Dancing Sentence
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
  string = input()
  return string

def solve(string):
  is_up = True
  new_string = ""
  for i in range(len(string)):
    if string[i] == " ":
      new_string += string[i]
    else:
      if is_up == True:
        new_string += string[i].upper()
      else:
        new_string += string[i].lower()
      is_up = not is_up
  return new_string
  
## main ##

n = int(input())
for i in range(n):
  num = r_input()
  ans = solve(num)
  print(ans)

