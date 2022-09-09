"""
Author: passa-
Problem: 08 closed k points
Student Code: 6510503310
Branch: Computer Engineering
"""

def r_input():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    n_point = list(map(int, input().split()))
    k = int(input())
    return n,points,n_point,k

def solve(n,points,n_point,k):
    dist = [((n_point[1] - points[i][1]) ** 2 + (n_point[0] - points[i][0]) ** 2 ) ** (0.5) for i in range(len(points))]
    dist.sort()
    return dist[:k]

def print_ans(ans):
    for dist in ans:
        print(f"{dist:.2f}")

## main ##

n,points,n_point,k = r_input()
ans = solve(n,points,n_point,k)
print_ans(ans)

