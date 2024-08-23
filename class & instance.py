class Student():
    college_name = "SRIT"
    name="naseera" #class attribute
    def __init__(self,name,age):
        self.name=name #object attribute
        self.age=age
s1=Student("nas",20)
print(s1.college_name)
#object attribute has more precedence than class attribute
print(s1.name)
print(Student.college_name)

s2=Student("naz",24)
print(s2.age)


#using methods

class Student():
    college_name = "SRIT"
    def __init__(self,name,marks):
        self.name=name #object attribute
        self.marks=marks
    def get_marks(self):
        print(self.marks)
    def welcome(self):
        print("Welcome",self.name)

s1=Student("nas",20)
s1.get_marks()
s1.welcome()