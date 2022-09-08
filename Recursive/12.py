"""
Author: passa-
Problem: 12 ปริพันธ์จำกัดขอบเชค
Student Code: 6510503310
Branch: Computer Engineering
"""

def integral(f,a,b):
  b = round(b,10)
  if b > a and "d" not in globals():
    global d
    d = (b-a)/500  # default delta value
    b = (b-a)/500  # init delta value
  if b == 999*d:
    return f(a+b/2)*d
  return f(a+b/2)*d + integral(f,a,b+2*d)

fn = lambda x:2*x**2

print(integral(fn,2,4))