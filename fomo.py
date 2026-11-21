# a=int(input("enter a number: "))
# count=0
# for i in range (1,a+1):
#     if i%3==0 and i%5==0:
#         print(i,end=" ")
#         count+=1
# print("\ncount=",count)


# a=int(input("enter a number"))
# for i in range(2,a):
#     if i%a!=0:
#         print("prime")
#     elif a<=1:
#         print("invalid input")
#     else:
#         print("composite")

def is_prime(n):
    if n<2:
        return False
        for i in range (2,int(n**0.5)+1): 
            if n%1==0:
                return False
        return True
def get_prime(n):
        return[n for number in range(2,n+1) if is_prime(n)]

print(get_prime(10))

# n=int(input("enter a number"))
# flag=0
# if n<=1:
#      print("not prime")
# else:
#      for i in range (2,n):
#           if i%n==0:
#                flag=1
#                break
#      if flag==0:
#         print("prime")
#      else:
#           print("composite")

     










