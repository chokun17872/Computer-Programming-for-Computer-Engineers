"""
Author: passa-
Problem: 01 L14 Student
Student Code: 6510503310
Branch: Computer Engineering
"""

import csv
maxx = -1
minn = 1e9

class Std:
    def __init__(self, _id, gender, race, education, lunch, test_course, math_s, reading_s, writing_s):
        self.id = _id
        self.gender = gender
        self.race = race
        self.education = education
        self.lunch = lunch
        self.test_course = test_course
        self.math_s = int(math_s)
        self.reading_s = int(reading_s)
        self.writing_s = int(writing_s)
    
    def show_data(self):
        print(f"gender : {self.gender}")
        print(f"race/ethnicity : {self.race}")
        print(f"parental level of education : {self.education}")
        print(f"lunch : {self.lunch}")
        print(f"test preparation course : {self.test_course}")
        print(f"math score : {self.math_s}")
        print(f"reading score : {self.reading_s}")
        print(f"writing score : {self.writing_s}")
    
    def less_from_max_math_score(self):
        print(f"less than max : {maxx - self.math_s}")
    
    def more_from_min_reading_score(self):
        print(f"more than min : {self.reading_s - minn}")
    
    def can_pass(self):
        if self.math_s + self.reading_s + self.writing_s > 240:
            print("Can pass")
        else: print("Can't pass")
    
    def __repr__(self):
        return f"math score : {self.math_s}, reading score : {self.reading_s}, writing score : {self.writing_s}"

def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data

## main ##

filename = input("Filename : ")
datas = read_csv(filename)
classes = list()
for i in range(1,len(datas)) :
    data = Std(datas[i][0],datas[i][1],datas[i][2],datas[i][3],datas[i][4],datas[i][5],datas[i][6],datas[i][7],datas[i][8])
    classes.append(data)

menu = int(input("Menu : "))
id = input("ID : ")
for i in classes :
    if i.id == id :
        if menu == 1 : # show data
            i.show_data()
        elif menu == 2 : # less_from_max_math_score
            i.less_from_max_math_score()
        elif menu == 3 : # more_from_min_reading_score
            i.more_from_min_reading_score()
        elif menu == 4: # can_pass
            i.can_pass()
        elif menu == 5: # print
            print(i)
        break