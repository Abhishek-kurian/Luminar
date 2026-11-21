# jumping statement

# break -- stops the loop forcefully
#continue -- skips the current iteration of the loop
#pass -- do nothing


# for i in range(5):
#     if i==3:
#         continue
#     print(i)
    

#  continuesly enter value

# e=input("enter names of students enter 'stop' to exit ")
# d=[]
# while True:
#     w=input()
#     if w=='kk':
#         print("fee adak kuttaa")
#     elif w=='stop':
#         break
#     d.append(w)
# print(d)

# for i in range (10):
#     if i==5:
#         continue
#     print(i)

# a='aeiou'
# while True:
#     w=input("enter vowel to exit ").lower()
#     if w in a:
#         break

# for i in range (26):
#     if i%5==0:
#         continue
#     print(i*i)

# for i in range(4):
#     if i==2:
#         pass
#     print(i)

# for i in range(20):
#     if i%3==0:
#         continue

for i in range(1,500):
    if i%7==0 and i%9==0:
        print(i)
        break

