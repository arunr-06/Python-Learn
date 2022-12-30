"""
Purpose of the program is to display the report card of students
Report card contains name, rollno, marks and status 
status: Pass, fail, NA

Marks posted separately by teachers in the science and non_science departments 
Displaying the report card prior to marks being posted by both departments will display status: NA
All marks posted and scores above 50 in all subjects will display status: Pass 
"""
class mark:
    def __init__(self,name,rollno):
        self.rno=rollno
        self.name=name
        self.maths=0
        self.physics=0
        self.lang=0
        self.eng=0
    def science(self,math,phy):
        self.maths=math
        self.physics=phy
    def non_science(self,lang,english):
        self.lang=lang
        self.eng=english
    def display(self):
        print("rollno: ",self.rno)
        print("name: ",self.name)
        print("maths : ",self.maths)
        print("language : ",self.lang)
        print("physics : ",self.physics)
        print("english : ",self.eng)
        if (self.maths>0 and self.physics>0 and self.eng>0 and self.lang>0):
            if (self.maths<50 or self.physics<50 or self.eng<50 or self.lang<50):
                print("status : Fail")
            else:
                print("status : Pass")
        else:
            print("status : NA")

#Creating an object s1 and providing the parameters Name and Rollno
s1 = mark("Arun",66)

#Providing the values for the methods - science and non_science
s1.science(99,89)
s1.non_science(87,96)

#Calling the method to display the values
s1.display()