num=int(input("Enter a number: "))
if num ==0:
    print("Factorial of 0 is 1")
else:
    fact=1
    for i in range(1,num+1):
        fact *= i
    print(fact)
