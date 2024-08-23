class Student():
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name #object attribute
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def avg_cal(self):
        a = (self.sub1+self.sub2+self.sub3)/3
        print(a)
s1=Student("nas",90,96,93)
s1.avg_cal()


