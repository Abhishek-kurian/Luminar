# a=int(input("enter a number"))
# for i in range(1,a+1):
#     print(i,end=" ")

# for i in range (2,20,2):
#     print(i)

# x=int(input("enter a number"))
# s=0
# for i in range(2,x,2):
#        s=s+i
# print(s)


text=input("enter a word: ").lower()
v="aeiou"
count=0
for i in text:
    if i in v:
        count+=1
print(count)
# n= int(input("enter a number"))
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
# print(fact)