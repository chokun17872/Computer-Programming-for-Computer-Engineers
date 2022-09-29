"""
Author: passa-
Problem: 10 L12 Buy list
Student Code: 6510503310
Branch: Computer Engineering
"""

def read_file():
    file_name = input("File name: ")
    lines = open(file_name).read().splitlines()
    price = {}
    lst = {}
    get_price = True

    for line in lines:
        if line in "":
            continue
        if line == "Price":
            get_price = True
        elif line == "List":
            get_price = False
        elif get_price:
            name, cost = line.split()
            price[name] = int(cost)
        elif not get_price:
            name, qty = line.split()
            lst[name] = int(qty)
        print(line)

    return price, lst

def solve(price, lst):
    total = 0
    for item in lst:
        if item in price:
            total += price[item] * lst[item]
    return total

## main ##

price, lst = read_file()
print(f"Total price: {solve(price, lst)}")