"""
Author: passa-
Problem: [calculate] เครื่องคิดเลขใช้ถ่ายรูปไม่ได้นะรู้เปล่า?
Student Code: 6510503310
Branch: Computer Engineering
"""

class MyMath:
    
    def __init__(self):
        ans = 3
        for i in range(50):
            n1 = (i+1)*2
            n2,n3 = n1+1,n1+2
            if i % 2 == 0:
                ans += (4/n1/n2/n3)
            else:
                ans -= (4/n1/n2/n3)
        self.pi = ans

    def divide_by(self,num,k):
        return num % k == 0
    
    def is_even(self,num):
        return num % 2 == 0
    
    def fac(self,num):
        ans = 1
        for n in range(2,num+1):
            ans *= n
        return ans
    
    def is_prime(self,num):
        sqrt_num = num**(0.5)
        if num == 1: return False
        if num == 2: return True
        for i in range(2,int(sqrt_num)+1):
            if num % i == 0:
                return False
        return True
    
    def ten_to_bi(self,num):
        ans = []
        while num != 0:
            remainder = num % 2
            num //= 2
            ans.insert(0,str(remainder))
        return "".join(ans)
    
    def ten_to_oct(self,num):
        ans = []
        while num != 0:
            remainder = num % 8
            num //= 8
            ans.insert(0,str(remainder))
        return "".join(ans)

    def ten_to_sixteen(self,num):
        ans = []
        alpha = ["A","B","C","D","E","F"]
        while num != 0:
            remainder = num % 16
            if remainder >= 10:
                ans.insert(0,alpha[remainder-10])
            else:
                ans.insert(0,str(remainder))
            num //= 16  
        return "".join(ans)

    def int_to_roman(self,num):
        ans = []
        while num > 0:
            if num >= 1000:
                ans.append("M"*(num//1000))
                num -= 1000 * (num//1000)
            elif num >= 900:
                ans.append("CD")
                num -= 900
            elif num >= 500:
                ans.append("D")
                num -= 500
            elif num >= 400:
                ans.append("CD")
                num -= 400
            elif num >= 100:
                ans.append("C"*(num//100))
                num -= 100 * (num//100)
            elif num >= 90:
                ans.append("XC")
                num -= 90
            elif num >= 50:
                ans.append("L")
                num -= 50
            elif num >= 40:
                ans.append("XL")
                num -= 40
            elif num >= 10:
                ans.append("X"*(num//10))
                num -= 10 * (num//10)
            elif num == 9:
                ans.append("IX")
                num -= 9
            elif num >= 5:
                ans.append("V")
                num -= 5
            elif num == 4:
                ans.append("IV")
                num -= 4
            else:
                ans.append("I"*(num))
                num = 0
        return "".join(ans)

## main ##

my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')