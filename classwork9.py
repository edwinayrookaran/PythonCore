# # # Q1.Define a function that takes 2 numbers and returns their product

# def product(n1,n2):
#     pro=n1*n2
#     return pro
#
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# c=product(a,b)
# print("Product is",c)

# # Q2.Define a function that takes a string and returns number of vowels

# def vowel(s):
#     count = 0
#     for i in s:
#         if i in 'aeiouAEIOU':
#             count = count + 1
#     return count
#
# s = input("Enter a string: ")
# a = vowel(s)
# print("count is", a)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle

# def rectangle(a,b):
#     area=a*b
#     return area
#
# a=int(input("Enter length:"))
# b=int(input("Enter breadth:"))
# c=rectangle(a,b)
# print("Area is",c)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

# def even(l):
#     l1=[]
#     for i in l:
#         if i%2==0:
#             l1.append(i)
#     return l1
#
# l=[45,78,90,12,35]
# a=even(l)
# print(a)

# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

# def sum(l):
#     l1=[]
#     for i in l:
#         s=str(i)
#         total=0
#         for j in s:
#             total=total+int(j)
#         l1.append(total)
#     return l1
#
# l = [123, 345, 111, 678, 134, 809]
# a=sum(l)
# print(a)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]

# def unique(l):
#     l1=[]
#     for i in l:
#         if i not in l1:
#                 l1.append(i)
#     return l1
#
# l=[12,34,78,12,67,34,90,23]
# a=unique(l)
# print(a)

#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]

# def common(l1,l2):
#     l3=[]
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 l3.append(i)
#     return l3
#
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]
# a=common(l1,l2)
# print(a)


















