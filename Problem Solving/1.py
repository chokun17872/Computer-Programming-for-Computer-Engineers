"""
Author: passa-
Problem: 01 Lost Number
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
  num = list(map(int, input().split(",")))
  return num

def solve(lst):
  lst.sort()
  ch = [i for i in range(lst[0], lst[-1]+1)]
  lst = set(lst)
  return sum(ch) - sum(lst)
  
## main ##

n = int(input())
for i in range(n):
  num = r_input()
  ans = solve(num)
  print(ans)
