total=0
items=[]
while total<=5000:
    a=input("enter item ")
    b=int(input("price "))
    if b <= 0:
        continue
    else:
        total+=b
        items.append(a)
print(f"bill amount exceeds 5000 current items are{items} total amount {total}")

