# a= int(input("enter marks out of 100: "))
# if a>90 and a<=100:
#     print("Grade A")
# elif a>80 and a<=90:
#     print("Grade B")
# elif a>70 and a<=80:
#     print("Grade C")
# elif a>50 and a<=70:
#     print("Grade D")
# elif a>100 or a<0:
#     print("Invalid marks")
# elif a>0 and a<=50:
#     print("fail")

# uname= input("enter username: ")
# pwd= input("enter password: ")
# if uname=="admin":
#     if pwd=="admin123":
#         print("login successful")
#     else:
#         print("invalid password")

# i= int(input("enter a number1: "))
# j= int(input("enter a number2: "))
# k= int(input("enter a number3: "))
# if i>j and i>k:
#     print(f"{i} is greater")
# elif j>i and j>k:
#     print(f"{j} is greater")
# elif k>i and k>j:
#     print(f"{k} is greater")
# elif i==j and i>k:
#     print(f"{i} and {j} both are greater")
# elif i==k and i>j:
#     print(f"{i} and {k} both are greater")
# elif j==k and j>i:
#     print(f"{j} and {k} both are greater")
# else:
# #     print(f"{i} is greater but all are equal")

# s= float(input("enter salary: "))
# e= int(input("enter experience: "))
# if e>10:
#     print(f"salary: {s+(s*0.1)}")
# elif  e>5:
#         print(f"salary: {s+(s*0.05)}")
# else:
#     print(f"salary: {s+(s*0.02)}")


print("welcome to resturant choose from the menu")
print("1. pizza")
print("2. burger")
m= int(input("enter your choice: "))
if m==1:
    print("you have selected pizza")
    print("1. small, 2.medium, 3.large")
    a=input("enter your choice: ")
    if a=="1":
        print("you have selected small pizza")
        print("price: 150")
    elif a=="2":
        print("you have selected medium pizza")
        print("price: 250")
    elif a=="3":
        print("you have selected large pizza")
        print("price: 350")
    else:
        print("invalid choice")
elif m==2:
    print("you have selected burger")
    print("1. veg, 2.non-veg")
    n=input("enter your choice: ")
    if n=="1":
        print("you have selected veg burger")
        print("price: 100")
    elif n=="2":
        print("you have selected non-veg burger")
        print("price: 150")
    else:
        print("invalid choice")
else:
    print("invalid choice")