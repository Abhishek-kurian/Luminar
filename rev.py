# a=input("Enter a number: ")
# print("Reversed number is: ", str(a)[::-1]) 
#  

# a=int(input("Enter a number: "))
# while a>0:
#     b=a%10
#     print(b, end=" ")
#     a//=10


# a=int(input("Enter a number: "))
# n=a
# b=0
# while a>0:
#     b=b*10+a%10
#     a//=10
# if b==n:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palidrome")

a=input()
b=''
for i in range(len(a)):
    b=a[i]+b
if b==a:
    print("yeh")
else:
    print("nah")




