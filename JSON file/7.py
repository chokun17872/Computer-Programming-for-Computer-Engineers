"""
Author: passa-
Problem: 07 L14 Question #3
Student Code: 6510503310
Branch: Computer Engineering
"""

import csv

def read_file():
    file_name = input("Enter file name: ")
    with open(file_name) as file:
        datas = csv.reader(file)
        data = [i for i in datas]
    return data

def gen_dict(data):
    dct = {}
    data = data[1:]
    for city in data:
        if city[1] not in dct.keys():
            dct[city[1]] = {
                "temp": float(city[4]),
                "count": 1
            }
        else:
            dct[city[1]]["temp"] += float(city[4])
            dct[city[1]]["count"] += 1
    return dct

def print_res(dct):
    for country, value in dct.items():
        temp = value["temp"]
        count = value["count"]
        print(f"{country} {temp/count:.2f}")

## main ##

data = read_file()
dct = gen_dict(data)
print_res(dct)