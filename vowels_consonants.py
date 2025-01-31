string=input("Enter the string: ")
vowels=0
consonents=0
for i in string:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        vowels+=1
    elif i.isalpha():
         consonents+=1
print("vowels=",vowels,"consonents=",consonents)


      