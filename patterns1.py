# #square pattern
# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end=" ")
#     print()


# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# n=int(input("Enter the number: "))
# for i in range(n):
#     for j in ["A","B","C","D"]:
#         print(j,end=" ")
#     print()

# #printing uppercase alphabets
# n=int(input("Enter a number: "))
# for i in range(n):
#     i=0
#     ascii=65
#     while i<n:
#         char=chr(ascii)
#         print(char,end=" ")
#         ascii+=1
#         i+=1
#     print()
#or
# n=int(input("Enter a number: "))
# for i in range(n):
#     ascii=65
#     for j in range(n):
#         char=chr(ascii)
#         print(char,end=" ")
#         ascii+=1
#     print()

# #printing lowercase alphabets
# n=int(input("Enter a number: "))
# for i in range(n):
#     i=0
#     ascii=97
#     while i<n:
#         char=chr(ascii)
#         print(char,end=" ")
#         ascii+=1
#         i+=1
#     print()

# #square pattern with increasing numbers
# n=int(input("Enter the number: "))
# num=1
# for i in range(n):
#     for j in range(n):
#         print(num,end=" ")
#         num+=1
#     print()

# #square pattern with increasing alphabets
# n=int(input("Enter the number: "))
# ascii=65
# for i in range(n):
#     for j in range(n):
#         char=chr(ascii)
#         print(char,end=" ")
#         ascii+=1
#     print()

#Triangle pattern
# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#Triangle pattern
n=int(input("Enter a num: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

# #Triangle pattern
# n=int(input("Enter a num: "))
# for i in range(1,n+1):
#     for j in range(i):
#         ascii=64
#         char=chr(ascii+i)
#         print(char,end=" ")
#     print()

# #Triangle pattern
# n=int(input("Enter a num: "))
# for i in range(1,n+1):
#     num=1
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

# #Reverse Triangle Pattern
# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i+1,0,-1):
#         print(j,end=" ")
#     print()

# #Floyds Triangle Pattern
# num=1
# n=int(input("Enter a num: "))
# for i in range(n):
#     for j in range(i+1):
#         print(num,end=" ")
#         num+=1
#     print()

#inverted triangle pattern
n=int(input("Enter a num: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(j,end="")   
    print()








