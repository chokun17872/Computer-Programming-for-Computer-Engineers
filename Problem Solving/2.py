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
  is_up = string[0].isupper()
  new_string = ""
  for i in range(len(string)):
    if i == 0 or string[i] == " ":
      new_string += string[i]
    else:
      if is_up == True:
        new_string += string[i].lower()
      else:
        new_string += string[i].upper()
      is_up = not is_up
  return new_string
  
## main ##

n = int(input())
for i in range(n):
  num = r_input()
  ans = solve(num)
  print(ans)

