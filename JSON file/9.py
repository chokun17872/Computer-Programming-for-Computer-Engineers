"""
Author: passa-
Problem: 09 L14 World population
Student Code: 6510503310
Branch: Computer Engineering
"""

import json

def read_file():
    file_name = input("File Name: ")
    data = json.loads(open(file_name).read())
    return data

def country_count(data):
    print(len(data))

def population_count(data):
    total = 0
    for country in data:
        total += int(country["population"])
    print(total)

def conditional_country(data):
    count_1, count_2 = 0, 0
    for country in data:
        if country["country"][0] == "C":
            count_1 += 1
        if len(country["country"]) > 5:
            count_2 += 1
    print(count_1)
    print(count_2)

def conditional_population(data):
    count_1, count_2, count_3 = 0, 0, 0
    for country in data:
        population = int(country["population"])
        if population > 500000000:
            count_1 += 1
        if population > 250000000 and population < 750000000:
            count_2 += 1
        if population < 10000000:
            count_3 += 1
    print(count_1)
    print(count_2)
    print(count_3)

def most_population(data):
    percent_1, percent_2, = 0, 0
    for country in data:
        rank = int(country["Rank"])
        percent = float(country["World"]) * 100
        if rank <= 20:
            percent_1 += percent
        if rank >= 50 and rank <= 150:
            percent_2 += percent
    print(f"{percent_1:.2f}")
    print(f"{percent_2:.2f}")

## main ##

data = read_file()
option = int(input("Input : "))

if option == 1:
    country_count(data)
elif option == 2:
    population_count(data)
elif option == 3:
    conditional_country(data)
elif option == 4:
    conditional_population(data)
elif option == 5:
    most_population(data)