num=145
digit_sum=0
while num>0:
    last_digit=num%10
    num=num//10
    digit_sum+=last_digit

print(digit_sum)