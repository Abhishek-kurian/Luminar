# a=input("Enter a number: "))
# b=sum(int(digit) for digit in str(a))
# print(b)

a=int(input("Enter a number: "))
digit_sum=0
while a>0:
    digit_sum+=a%10
    a//=10
print(digit_sum)
