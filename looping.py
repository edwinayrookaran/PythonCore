# For loop

# 100,200,300,...,1000
# for i in range(100,1001,100):
#     print(i)

# 1,8,27,64,125

# for i in range(1,6):
#     print(i**3)

# find all 3digit numbers divisible by 3

# for i in range(100,1000):
#     if i%3 == 0:
#         print(i)

# colors=[red,green,blue,yellow,black]
# print reverse of ech color

# colors = ['red','green','blue','yellow','black']
# for i in colors:
#     print(i[::-1])

# print each digit in a number
# n=1234
# for i in str(n):
#     print(i)

# sum of each digit of a number

# n=1234
# sum=0
# for i in str(n):
#     sum +=int(i)
# print(sum)

# l = [1,2,3,4]
# new = []
# for i in l:
#     new.append(i**2)
# print(new)

# l = [1,2,3,4]
# new = set()
# for i in l:
#     new.add(i**2)
# print(new)

# given a string s=hello world create a new string with only vowels
# s="hello world"
# new=""
# vowels="aeiouAEIOu"
# for i in s:
#     if i in vowels:
#         new=new+i
# print(new)

# create a new dictionary where keys are numbers and values ae square of each number
# given a list = [1,2,3,4]

# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#reverse of a string
#
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# reverse of a number

# n=1234
# rev=""
# for i in str(n):
#     rev=i+rev
# print(rev)

# using break

# s="hello"
# for i in s:
#     if i=='l':
#         break
#     print(i)

# using continue

# s="hello"
# for i in s:
#     if i=='l':
#         continue
#     print(i)

# l=[25,67,34,78,17,44,82]
# print all numbers
# for i in l:
#     print(i)

#stops the loop when i>50
# for i in l:
#     if i>50:
#         break;
#     print(i)

# skip all even numbers

# for i in l:
#     if i%2==0:
#         continue
#     print(i)

# colors = ['red','green','yellow','blue','orange','black']
# print all colors

# for i in colors:
#     print(i)

#print starting with b
# for i in colors:
#     if i[0]=='b':
#         print(i)

# first color starting with b
# for i in colors:
#     if i[0]=='b':
#         print(i)
#         break

#skip all color starting with b
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i)

# print all characters upto a specific character
# s="python coding is easy and fun"
# ch=input("enter character:")
# for i in s:
#     print(i)
#     if i==ch:
#         break

# write a program to check whether a number is armstrong number

# num = int(input("Enter the number:"))
# sum=0
# for i in str(num):
#     sum = sum+int(i)**len(str(num))
# if sum == num:
#     print("Armstrong")
# else:
#     print("not Armstrong")

# factor of a number

# num = int(input("Enter a number:"))
# for i in range(1,num+1):
#     if(num%i==0):
#         print(i)

# for - else
#
# for i in range(1,6):
#     if(i==3):
#         break
#     print(i)
# else: # it only works after the normal execution of the loop
#     print("hello")

# check whether a number is prime or not

# num = int(input("Enter a number:"))
# if(num>1):
#     for i in range(2,num):
#         if(num%i==0):
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:  #number 1 or 0 or negative
#     print("Number is prime nor composite")

# nested loop

# l=[10,20,30]
# for i in l:
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end=" ")
#     print()
#
# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     for j in i:
#         print(j)

# names=['kelly','alan','jeny']
#
# for i in names:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

# n=[1,2,3]
# q=['what','when','why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()

# d=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':25}]
#
# for i in d:
#     for j in i.values():
#         print(j,end=" ")
#     print()

# d = {'id': 101, 'name': 'arun', 'age': 23}
# for i,j in d.items():
#     print(i,j)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,8,2):
#     for j in range(1,i+1,):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(5,1,-1):
#     for j in range(1,i):
#         print('*',end=" ")
#     print()

# l=[23,45,78,90,12,13,91]
# for i in l:
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)

# find all prime numbers in the range 1-100
# find all armstrong numbers from 100-1000

# for i in range(1,100):
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         print(i)

# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     k=ord('A')
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(i,end=" ")
#         else:
#             print('0',end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==1:
#             print('1',end=" ")
#         else:
#             print('0',end=" ")
#     print()

# for i in range(1,6):
#     for j in range(0,i):
#         print(j,end=" ")
#     print()

# s="hello"
# for i in range(1,6):
#     for j in range(0,i):
#         print(s[j],end=" ")
#     print()

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  # for printing space in each line
#         print(end=" ")
#     for j in range(1,i+1):   # for printing stars in each line
#         print('*',end="   ")
#     k=k-2
#     print()

#

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  # for printing space in each line
#         print(end=" ")
#     for j in range(1,i+1):   # for printing stars in each line
#         print('*',end="   ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):  # for printing space in each line
#         print(end=" ")
#     for j in range(1,i+1):   # for printing stars in each line
#         print('*',end="   ")
#     k=k+2
#     print()

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  # for printing space in each line
#         print(end=" ")
#     for j in range(1,i+1):   # for printing stars in each line
#         print(j,end="   ")
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):  # for printing space in each line
#         print(end=" ")
#     for j in range(1,i+1):   # for printing stars in each line
#         print(j,end="   ")
#     k=k+2
#     print()



































