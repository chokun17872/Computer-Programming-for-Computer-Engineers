"""
Author: passa-
Problem: 15 Flatten List (cloned)
Student Code: 6510503310
Branch: Computer Engineering
"""

def flatten_list(lst):
  if len(lst) == 0: return lst
  if isinstance(lst,list) and isinstance(lst[0],list) and len(lst) == 1:
    return flatten_list(lst[0])
  if not isinstance(lst[0],list) and len(lst) == 1: return lst ## base case
  return flatten_list(lst[:1]) + flatten_list(lst[1:])
  
# lst = [1,[2,3]]
# lst = [[[3]]]
# lst = [1, 3, 5, 7]
lst = [1, 2, [[2], [3, 4], 5], 4, [3], [[4]]]
# lst = []
  
print(flatten_list(lst))