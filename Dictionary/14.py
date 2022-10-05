"""
Author: passa-
Problem: 14 L13 Dictionary
Student Code: 6510503310
Branch: Computer Engineering
"""

dct = {
    "arm": {
        "1": "n",
        "2": "แขน"
    },
    "hello": {
        "1": "v",
        "2": "สวัสดี"
    },
    "beautiful": {
        "1": "adj",
        "2": "สวย"
    },
    "arm": {
        "1": "n",
        "2": "แขน"
    },
    "toilet": {
        "1": "n",
        "2": "ห้องน้ำ"
    },
    "kick": {
        "1": "v",
        "2": "เตะ"
    },
        "handsome": {
        "1": "adj",
        "2": "หล่อ"
    },
}

while True:
    word = input()
    if word == "0":
        break
    if word not in dct.keys():
        print("Word not in dictionary.")
        continue
    while True:
        option = input()
        if option not in ["1", "2"]:
            print("Invalid option.")
            continue
        else:
            break
    print(dct[word][option])