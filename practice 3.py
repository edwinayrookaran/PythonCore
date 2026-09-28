# n=12345
# count=0
# s=str(n)
# for i in s:
#     count=count+1
# print(count)
#
# n=12345
# count=0
# while n>0:
#     count=count+1
#     n=n//10
# print(count)

# n=12345
# sum1=0
# while n>0:
#     digit = n % 10
#     sum1=sum1+digit
#     n=n//10
# print(sum1)


# numbers = [10, 25, 8, 40, 15]
# numbers.sort()
# print(numbers[-2])


# numbers = [1, 2, 2, 3, 4, 4, 5, 5]
# l=[]
# for i in numbers:
#     if i not in l:
#         l.append(i)
# print(l)

# numbers = [15, 8, 42, 23, 4, 31]
# # numbers.sort()
# # print(numbers[-1])
# max=numbers[0]
# for i in numbers:
#     if i>max:
#         max=i
# print(max)


# numbers = [15, 8, 42, 23, 4, 31]
# min1=numbers[0]
# for i in numbers:
#     if i<min1:
#         min1=i
# print(min1)

# numbers = [10, 25, 8, 40, 25, 15]
# temp=0
# max=numbers[0]
# for i in numbers:
#     if i>max:
#         temp=max
#         max=i
# print(temp)
#
# s="python"
# c=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         c=c+1
# print(c)

# numbers = [10, 15, 20, 25, 30, 35]
# c=0
# for i in numbers:
#     if i%2==0:
#         c=c+i
# print(c)

# numbers = [1, 2, 2, 3, 1, 2, 4, 3]
# dict={}
# for i in numbers:
#     if i in dict:
#         dict[i]=dict[i]+1
#     else:
#         dict[i]=1
# print(dict)

# numbers = [10, 20, 30, 40, 50]
# dic={}
# for i in numbers:
#     dic[i]=i**2
# print(dic)

# n=5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()

# for i in range(1,100):
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         print(i)

# find all armstrong numbers from 100-1000

# for i in range(100,1000):
#     s=str(i)
#     sum1 = 0
#     for j in s:
#         sum1=sum1+int(j)**len(s)
#     if sum1==i:
#         print(i)

# def digit_sum(n):
#     s=str(n)
#     sum1=0
#     for i in s:
#         sum1=sum1+int(i)
#     return sum1
#
# a=digit_sum(12345)
# print(a)

# def divisible(n):
#     s=str(n)
#     sum1=0
#     for i in s:
#         sum1=sum1+int(i)
#     if n%sum1==0:
#         return True
#     else:
#         return False
#
# a=divisible(18)
# print(a)

# def is_palindrome(n):
#     s=str(n)
#     rev=s[::-1]
#     if s==rev:
#         return True
#     else:
#         return False
#
# a=is_palindrome(121)
# print(a)
#
# def is_perfect(n):
#     sum1=0
#     for i in range(1,n):
#         if n%i==0:
#             sum1=sum1+i
#     if sum1==n:
#         return True
#     else:
#         return False
#
# a=is_perfect(6)
# print(a)

# def is_strong(n):
#     s=str(n)
#     sum1 = 0
#     for i in s:
#         fact = 1
#         for j in range(1,int(i)+1):
#             fact=fact*int(j)
#         sum1=sum1+fact
#     if sum1==n:
#         return True
#     else:
#         return False
#
# a=is_strong(145)
# print(a)


# def is_abundant(n):
#     sum1=0
#     for i in range(1,n):
#         if n%i==0:
#             sum1=sum1+i
#     if sum1>n:
#         return True
#     else:
#         return False
# a=is_abundant(12)
# print(a)

# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
#
# even(20)















