"""
Author: passa-
Problem: 04 L10 Shape
Student Code: 6510503310
Branch: Computer Engineering
"""

PI = 3.14

class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width

  def perimeter(self):
    return (self.length + self.width) * 2

  def is_square(self):
    if self.length == self.width:
      return "This rectangle is square too."
    return "This rectangle is not square."

class Triangle:
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def area(self):
    s = (self.side1 + self.side2 + self.side3) / 2
    return (s * (s-self.side1) * (s-self.side2) * (s-self.side3))**(0.5)

  def perimeter(self):
    return self.side1 + self.side2 + self.side3

  def is_right_triangle(self):
    sides = [self.side1, self.side2, self.side3]
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
      return "This triangle is right triangle too."
    return "This triangle is not right triangle."

class Circle:
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return PI*self.radius**2

  def perimeter(self):
    return 2*PI*self.radius

## main ##

l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)  
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)  
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

r = int(input("Enter circle radius : "))  
p3 = Circle(r)  
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.')  