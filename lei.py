n=int(input("enter a number"))
flag=0
if n<=1:
     print("not prime")
else:
     i=2
     while i<n:
          if i%n==0:
               flag=1
               break
     if flag==0:
        print("prime")
     else:
          print("composite")

