class Student():
    name="Naseera"
s1=Student()
print(s1.name)

class Car:
    color="Black"
    brand="kia"
c1=Car()
print(c1.color)
print(c1.brand)

#Using constructor
class Student():
    name="Naseera"
    def __init__(self):
        print(self)
        print("Adding new student into the database")
s1=Student()
print(s1.name)
print(s1)

#parameterized constructors
class Student():
    def __init__(self,fullname):
        self.name=fullname
s1=Student("naseera")
print(s1.name)
