# def add():
#     "Addition of 2 numbers"
#     n1=int(input("Enter 1st number:"))
#     n2=int(input("Enter 2nd number:"))
#     s=n1+n2
#     print("sum is",s)
#     return
# add()
#
#
# define a function to display "hello your name"
#
# def name():
#     n=input("Enter you name:")
#     print("hello",n)
# name()
#
# define a function to find the factorial of a number
#
# def fact():
#     num=int(input("Enter a number:"))
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# fact()
#
# define a function to find the count of a specific character in a given string
#
# def char():
#     s=input("Enter a string:")
#     ch=input("Enter character:")
#     count=0
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
# char()
#
# define a function to check whether a number is prime or not
#
# def prime():
#     n=int(input("Enter a number:"))
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not prime")
#             break
#     else:
#         print('Prime')
# prime()

# define a function to find the factors of a number
#
# def factors():
#     n=int(input("Enter a number:"))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#
# factors()


# def sum(n1,n2):
#     s=n1+n2
#     print('sum is',s)
#     return
#
# sum(5,6)

# define a function that takes 3 arguments amount,years and rate as arguments and find the simple interest

# def interest(amount,years,rate):
#     SI=(amount*years*rate)/100
#     print("Simple interest is",SI)
#     return
#
# p=int(input("Enter amount:"))
# y=int(input("Enter years:"))
# r=int(input("Enter rate:"))
# interest(p,y,r)

# define a function that takes 2 nos as arguments and return sum as result

# def add(n1,n2):
#     s=n1+n2
#     return s
#
# a=add(23,57)
# print("sum is ",a)

# define a function that takes a string as argument and return a new dictionary where keys are wors
# and values are length of each word

# def length(s):
#     dic = {}
#     for i in s.split():
#         dic[i] = len(i)
#     return dic
#
# s = "python coding is easy and fun"
# a=length(s)
# print(a)

# define a function to find the sum of numbers using arbitary type

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
#
# add(10,20,30)

# write a program to create a  list 5 random 3 digit numbers

# import random
# new=[]
# for i in range(5):
#     new.append(random.randint(100,999))
# print(new)

# write a program to create a 5 digit random otp number

# import random
# otp=random.randint(10000,99999)
# print(otp)

# write a program to find the position of a character in a string

# s=input("Enter the string: ")
# ch=input("Enter character: ")
# pos=s.index(ch)
# print(pos)

# define a function that takes a string as arguments and returns a new dictionary

# where keys are characters and values are count of characters

# def count1(s):
#     dic={}
#     for i in s:
#         dic[i]=s.count(i)
#     return dic
#
# s=input("Enter string: ")
# a=count1(s)
# print(a)
# define a function to print the count the digits,spaces,letters in a string

# def count(s):
#     count1=0
#     count2=0
#     count3=0
#     for i in s:
#         if i.isdigit():
#             count1=count1+1
#         elif i.isspace():
#             count2=count2+1
#         elif i.isalpha():
#             count3=count3+1
#
#     print('digits=',count1,"space=",count2,'letters=',count3)
#
# s=input("Enter string:")
# count(s)

# l=[1,2,2,3,4,4,5,6]
# dic={}
# for i in l:
#     if i in dic:
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=1
# print(dic)
#
# l=[11,34,78,23,90,65]
# l.sort()
# print("Largest number:",l[-1])
# print("Second largest:",l[-2])
# print("Smallest number:",l[0])
# print("Second smallest:",l[1])
#
# l=[['arun',23,30000],
#    ['amal',25,50000],
#    ['anu',27,40000]]
# max=0
# for i in l:
#     if i[2]>max:
#         max=i[2]
#     min = i[1]
# for i in l:
#     if i[1]<min:
#         min=i[1]
#
# print(max)
# print(min)

# l=[23,45,67,12,90,78]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print("max:",max)
#
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print("min:",min)

# l=[1,1,2,3,3,4]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#
# l=[1,1,2,3,3,4]
# s=set(l)
# print(s)
#
#
# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))


# def square(n):
#     sq=n*n
#     return sq
#
# n=int(input("Enter a number: "))
# a=square(n)
# print(a)

# a=lambda x:x*x
# print(a(5))

# c=lambda a,b:a+b
# print(c(4,5))

# c=lambda a,b,c:a*b*c
# print(c(4,5,6))

# a=lambda x:x**3
# print(a(5))

# a=lambda s:s[0]
# print(a("edwin"))

# a=lambda s:len(s)
# print(a("Edwin"))

# a=lambda s:s[::-1]
# print(a("edwin"))

# a=lambda d:d['name']
# print(a({'name':'edwin','age':23}))

# a=lambda l:l[1]
# print(a([10,20,30,40]))

# a=lambda x:x+10
# print(a(5))

# l=[1,2,3,4]
#
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))


# #create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))
#
# #create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**.5,l)))
#
# #create a new list of lengths
colors=['red','green','blue','yellow','black']
# print(list(map(lambda x:len(x),colors)))
# #create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
# #create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))
# #create a new list of reverse of each elemnt
# print(list(map(lambda x:x[::-1],colors)))
#
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
# print(list(map(lambda x:x['email'],l)))


# l=[23,45,67,12,89,70]
# print(list(filter(lambda x:x%2==0 and x>50,l)))
#
# colors=['red','green','blue','yellow','orange']
# print(list(filter(lambda x:len(x)>5,colors)))
#
# print(list(filter(lambda x:'n' in x,colors)))

# l=[1,2,3,4]
# import functools
# print(functools.reduce(lambda x,y:x+y,l,0))

























