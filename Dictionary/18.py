"""
Author: passa-
Problem: 18 L13 Jong Tao
Student Code: 6510503310
Branch: Computer Engineering
"""

class Flight:
    def __init__(self, code, start, end, peop, cap):
        self.code = code
        self.start = start
        self.end = end
        self.peop = int(peop)
        self.cap = int(cap)
    
    def __repr__(self):
        return f"{self.code} is from {self.start} to {self.end}, number of people booking is {self.peop}/{self.cap}"
    
    def update_peop(self):
        self.peop += 1

def add_flight():
    data = input("Add data : ").split()
    code, start, end, peop, cap = data[0], data[1], data[3], data[4], data[6]
    return code, Flight(code, start, end, peop, cap)

def show_all(flight_dct):
    print("All flight data")
    for flight in flight_dct.values():
        print(flight)

## main ##

print("Select menu :")
print("1. add flight data")
print("2. flight data by code")
print("3. show all flight data")
print("4. flight booking")
print("5. show people flight data")
print("6. exit")

flight_dct,reserve_dct = {}, {}
while True:
    menu = int(input("menu : "))
    if menu == 6:
        print("EXIT!!!!!!!!!!!!!!!")
        break
    elif menu == 1:
        code, flight = add_flight()
        flight_dct[code] = flight
    elif menu == 2:
        code = input("Enter code : ")
        print(flight_dct[code])
    elif menu == 3:
        show_all(flight_dct)
    elif menu == 4:
        name = input("Enter your name : ")
        code = input("Enter flight code : ")
        if flight_dct[code].peop < flight_dct[code].cap:
            if name not in reserve_dct.keys():          
                reserve_dct[name] = f"{code}" 
            else:
                reserve_dct[name] += f" {code}"
            flight_dct[code].update_peop()
            print("Success")
        else:
            print("The flight is full, Sorry")
    elif menu == 5:
        name = input("Enter your name : ")
        print(f"{name} is booking flight code = {reserve_dct[name]}")