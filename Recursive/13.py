"""
Author: passa-
Problem: 13 อนุพันธ์
Student Code: 6510503310
Branch: Computer Engineering
"""

def differentiate(fn):
  return lambda x:(fn(x+0.00001) - fn(x)) / 0.00001
