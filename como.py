# strong number checker
# a=int(input("Enter a number to check: "))
# sum=0
# t=a
# while t>0:
#     n=t%10
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     sum+=fact
#     t//=10
# if sum==a:
#     print(f"{a} is a Strong number")
# else:
#     print(f"{a} is Not a Strong number")

# fibionacci series

n=int(input("Enter a number: "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
