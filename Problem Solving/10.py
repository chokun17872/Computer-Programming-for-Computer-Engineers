"""
Author: passa-
Problem: 10 Blackjack
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    n = int(input())
    decks = []
    for i in range(n):
        decks.append(input().split())
    return n,decks

def solve(deck):
    score = 0
    broadways = ["J","Q","K"]
    for i in range(5):
        if deck[i] == "A":
            score += 1
        elif deck[i] in broadways:
            score += 10
        else:
            score += int(deck[i])
        if score > 21:
            return "busted"
        elif score > 16:
            return score
    return score

## main ##

n,decks = r_input()
for i in range(n):
    print(solve(decks[i]))