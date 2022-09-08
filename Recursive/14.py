"""
Author: passa-
Problem: 14 ฟังก์ชันยกกำลังแบบรีเคอร์ซีฟ
Student Code: 6510503310
Branch: Computer Engineering
"""

def power(n,k):
    if k == 0: return 1
    return n * power(n,k-1)