#single inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoped..")
class Toyoto(Car):
    def __init__(self,name):
        self.name=name
c1 = Toyoto("fortuner")
print(c1.start())
print(c1.stop())
print(c1.name)
print(c1.color)

#Multi-Level inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoped..")
class Toyoto(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(Toyoto):
    def __init__(self,type):
        self.type = type
c1 = Toyoto("fortuner")
c2=Fortuner("Diesel")
c3=Fortuner("electric")
print(c1.brand)
print(c2.type)
print(c1.start())

#multiple inheritance
class A:
    varA = "Welcome to A class"
class B:
    varB = "Welcome to B class"
class C(A,B):
    varC = "Welcome to C class"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
