a=int(input("enter a number"))
b=str(a)
l=len(b)
s=0
for i in b:
    s+=int(i)**l

if s==a:
    print("amstrong")
else:
    print("not amstrong")

# a=int(input("enter a lower limit "))
# b=int(input("enter a upper limit "))
# k=0
# for i in range(a,b+1):
#     l=len(str(i))
#     s=0
#     t=i
#     while t>0:
#         digit=t%10
#         s+=digit**l
#         t//=10
#     if s==i:
#         k=i
# print(k)
