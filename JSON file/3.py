"""
Author: passa-
Problem: 03 L14 Racing
Student Code: 6510503310
Branch: Computer Engineering
"""

import json

def read_file():
    file_name = input("Enter json filename : ")
    data = json.loads(open(file_name).read())
    return data["racer"]

def cal_time(racer, dist):
    time = 0
    for i in range(len(racer["_range"])):
        if i == len(racer["_range"]) - 1 or dist < racer["_range"][i+1]:
            time += (dist - racer["_range"][i]) / racer["velocity"][i]
            break
        else:
            time += (racer["_range"][i+1] - racer["_range"][i]) / racer["velocity"][i]
    print(time)
    return float(f"{time:.2f}")

def add_time(data, dist):
    for racer in data:
        racer["time"] = cal_time(racer, dist)
    return data

def sort_racer(data):
    data = sorted(data, key = lambda x:x["time"])
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            if data[i]["time"] == data[j]["time"]:
                if data[i]["response"] < data[j]["response"]:
                    data[i], data[j] = data[j], data[i]
                elif data[i]["response"] == data[j]["response"]:
                    if data[i]["name"] > data[j]["name"]:
                        data[i], data[j] =  data[j], data[i]
    return data

def print_res(data):
    for racer in data:
        time = racer["time"]
        print(racer["name"], f"{time:.2f}")

## main ##

data = read_file()
dist = int(input("Enter distance (meter) : "))
data = sort_racer(add_time(data, dist))
print_res(data)