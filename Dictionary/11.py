"""
Author: passa-
Problem: 11 การประมูล
Student Code: 6510503310
Branch: Computer Engineering
"""

from unittest.util import sorted_list_difference


def r_input():
    bids_info = []
    while True:
        info = input()
        if info == "end":
            return bids_info
        else:
            bids_info.append(info.split())

def gen_dct(bids_info):
    dct = {}
    turn = 1
    for name, bid in bids_info:
        if name not in dct.keys():
            dct[name] = [float(bid), 1, turn]
        else:
            dct[name] = [float(bid), dct[name][1]+1, turn]
        turn += 1
    return dct

def print_contestant(dct):
    for key, value in dct.items():
        if value[1] == 1: 
            print(key, f"bid at the price of {value[0]} baht in {value[1]} time.")
        else: print(key, f"bid at the price of {value[0]} baht in {value[1]} times.")

def print_winner(dct):
    sorted_contestant = sorted(dct.items(), key = lambda x:(x[1][0], x[1][2]), reverse = True)
    highest_bid = sorted_contestant[0][1][0]
    for i in range(len(sorted_contestant)-1,-1,-1):
        if sorted_contestant[i][1][0] == highest_bid:
            print(f"The winner is {sorted_contestant[i][0]}.")
            break

## main ##

bids_info = r_input()
dct = gen_dct(bids_info)
dct = dict(sorted(dct.items()))
print_contestant(dct)
print_winner(dct)