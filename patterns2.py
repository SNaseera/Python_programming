# #pyramid Pattern
# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(i+1,0,-1):
#         print(j,end="")
#     print()


#Hollow Diamond Pattern
n=4
#top
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(2*i):
        if j == 1 or j==2*i-1:
             print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n-1,0, -1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,2*i):
        if j == 1 or j==2*i-1:
             print("*", end="")
        else:
            print(" ", end="")
    print()
    
     
        
