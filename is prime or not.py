n=int(input("Enter a num: "))
if n<2:
    print("Not a Prime")
else:
    is_prime=True
    for i in range(2,n):
        if (n%i==0):
            is_prime=False
            break
    if is_prime:
        print("It is a Prime Number")
    else:
        print("It is Not a Prime Number")



