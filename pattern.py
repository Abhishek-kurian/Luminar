# for i in range(3):
#     for j in range (1,6):
#         print(j,end=" ")
#     print()
    
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print()

# for i in range(5):
#     for j in range(1+i):
#         print("*", end=' ')
#     print()

    
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print()

# for i in range(5):
#     for j in range(1+i):
#         print("*", end=' ')
#     print()

# for i in range(1,6):
#     for j in range (6-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# for i in range (5):
#         for j in range(5):
#             if i==0 or i==4:
#                 print("-",end=" ")
#             elif j==0 or j==4:
#                  print("*",end=" ")
#             else:
#                  print(" ",end=" ")
#         print()

# a = 5
# for i in range(1, a+1):
#     print(*([i] * (a-i+1)))


#print(*[value]*count)
#value - what do you want to print
#count - how many times/

# a=5
# for i in range(5):
#     print(*["*"]*(a))
    
# a=5
# b=3
# for i in range(b):
#     print(*["*"]*(a))

# a=5
# for i in range(a):
#     print(*[i]*(i))

# a=5
# for i in range (a):
#     for j in range(a-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# a=5
# for i in range(a):
#     if i == 0 or i == a-1:
#         print(*["*"] * a)
#     else:
#         print("*", *[" "] * (a-2), "*")

# a = 5
# for i in range(1, a+1):
#     print(" " * (i), end=" ")
#     print(*["*"] * (a-i+1))

n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end=" ")
    print("*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end=" ")
    print("*" * (2 * i - 1))
