"""
Author: passa-
Problem: 04 L14 Item
Student Code: 6510503310
Branch: Computer Engineering
"""

class Item:
  def __init__(self, id, type, price):
    self.id = id
    self.type = type
    self.price = price

  def show_id(self):
    print(self.id)

  def show_type(self):
    print(self.type)

  def show_price(self):
    print(self.price)

def r_input():
  item = input().split()
  return item
    
## main ##

n = int(input("How many products are there? : "))
items = []
ids = []

for i in range(n):
  arg1,arg2,arg3 = r_input()
  ids.append(arg1)
  items.append(Item(arg1,arg2,arg3))
  
while True:
  id = input("Id : ")
  if id not in ids:
    print("This id doesn't exist.")
    continue
  q = input("Q : ")
  if q == "0":
    break
  while True:
    if q == "1":
      print(items[ids.index(id)].type)
    if q == "2":
      print(items[ids.index(id)].price)
    if q == "3" or q == "0":
      break
    q = input("Q : ")
  if q == "0":
    break