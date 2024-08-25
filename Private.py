class Account:
    def __init__(self,acc_num,acc_pas):
        self.acc_num=acc_num
        self.__acc_pas = acc_pas
    def reset_pass(self):
        print(self.__acc_pas)
a = Account(123456,"abcdef")
print(a.acc_num)
#print(a.acc_pas)
print(a.reset_pass())


class Person:
    __name = "Nase"

    def __hello(self):
        print("Hello Person!")
    def welcome(self):
        self.__hello()
p1=Person()
print(p1.welcome())


class Insta:
    def __init__(self,username,acc_pas):
        self.username=username
        self.__acc_pas=acc_pas

    def reset_pas(self):
        print(self.__acc_pas)
a1 = Insta("abc_123",123456)
print(a1.username)

print(a1.reset_pas())