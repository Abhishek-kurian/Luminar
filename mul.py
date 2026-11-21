a=int(input("Enter a lower limit: "))
b=int(input("Enter an upper limit: "))
sum=0
sumo=0
while b>=a:
    if a%2==0:
        sum+=a
    else:
        sumo+=a
    a+=1
print("The sum of even numbers between the given range is:",sum)
print("The sum of odd numbers between the given range is:",sumo)
print("total=",sum+sumo)
    

