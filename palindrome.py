str =input("str : ")
processed_str=str.replace(" ", "").lower()
if processed_str == processed_str[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
