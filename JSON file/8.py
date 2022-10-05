"""
Author: passa-
Problem: 08 L14 Question #4
Student Code: 6510503310
Branch: Computer Engineering
"""

import csv

def read_file():
    city_file = input("Enter city file: ")
    country_file = input("Enter country file: ")
    with open(city_file) as file:
        datas = csv.reader(file)
        data = [i for i in datas]
    with open(country_file) as file:
        datas = csv.reader(file)
        data2 = [i for i in datas]
    return data, data2

def gen_dct(db):
    dct = {}
    db = db[1:]
    for city in db:
        if city[1] not in dct.keys():
            dct[city[1]] = {
                "temp": float(city[4]),
                "count": 1
            }
        else:
            dct[city[1]]["temp"] += float(city[4])
            dct[city[1]]["count"] += 1
    return dct

def print_res(city_dct, country_db):
    print("Average temperature of countries having coastline, but not in EU:")
    for country in country_db:
        if country[2] == "no" and country[3] == "yes" and country[0] in city_dct.keys():
            avg = city_dct[country[0]]["temp"] / city_dct[country[0]]["count"]
            print(f"{country[0]} {avg:.2f}")

## main ##

city_db, country_db = read_file()
city_dct = gen_dct(city_db)
print_res(city_dct, country_db)