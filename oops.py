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
print()
class Maggi():
    color="Yellow"
    type="Noodles"
    def __init__(self,color,taste):
        self.color=color
        self.taste=taste
        print("calling")
s1=Maggi("Yell","Super")
print(s1.color)
print(Maggi.type)
print(Maggi.color)
print(s1.taste)
s2=Maggi("Yell","Super")
print(s1.taste)
