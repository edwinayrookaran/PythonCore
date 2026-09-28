# list comprehension

# l=[1,2,3,4]
# new=[i**2 for i in l]  # in each iteration adds i**2 where i takes value from list l
# print(new)
#
# new=[5 for i in l]
# print(new)

# l=[23,56,34,12,89,90,24]
# new=[i for i in l if(i%2==0)]
# print(new)
#
# new=[i for i in l if i>=50]
# print(new)
#
# colors=['red','green','blue','orange']
# new=[i[0] for i in colors]
# print(new)
#
# new=[len(i) for i in colors]
# print(new)

# l=[1,2,3,4]
# new=[i**3 for i in l]
# print(new)


# l=[25,36,81,100]
# import math
# new=[math.sqrt(i) for i in l]
# print(new)

# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# new=[i['email'] for i in l]
# print(new)

# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
# new=[i for i in d.keys()]
# print(new)
# # # create a list of marks
# new=[i for i in d.values()]
# print(new)
# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # #create a list of string values
# new=[i for i in l if(type(i)==str)]
# print(new)
# # #create a list of floats
# new=[i for i in l if(type(i)==float)]
# print(new)
# # #create a list of positive numbers
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
# #
# #
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if(len(i)>6)]
# print(new)
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101) if(i%3==0)]
# print(new)
# s="python coding  is easy and fun"
# # # create a new list with only vowels
# new=[i for i in s if i in 'aeiouAEIOU']
# print(new)


#set comprehension
# s="python coding  is easy and fun"
# new={i for i in s if i in 'aeiouAEIOU'}
# print(new)

# dictionary comprehension
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)
#
# new={i:i**3 for i in l}
# print(new)

# l=[10,20,30,40]
# # create a new list where keys are indexes and values are numbers
# new={i:l[i] for i in range(0,len(l))}
# print(new)

# s='hello world'
# for i in s.split():
#     print(i)

# s="python coding is easy and fun"
# # create a new dictionary where key are words and value are length of each word
# new={i:len(i) for i in s.split()}
# print(new)

# define a function that takes a number as argument and check whether that number is spy number
# or not

# def spy(n):
#     s = str(n)
#     sum = 0
#     pro = 1
#     for i in s:
#         sum = sum + int(i)
#         pro = pro * int(i)
#     if sum == pro:
#         print("Spy number")
#     else:
#         print("No")
#
#
# n = int(input("Enter a number: "))
# spy(n)


































