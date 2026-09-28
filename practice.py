# Level 1 — Basic Functions
# Q1. Even or Odd
#
# Write a function even_odd(n) that checks whether a number is even or odd.
#
# Example:
#
# Input: 8
# Output: Even

# def even(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("odd")
#
# n=int(input("Enter a number:"))
# even(n)

# Q2. Greatest of Two
#
# Write a function greatest(a, b) that returns the greater of two numbers.
#
# Input: 10 25
# Output: 25
# def great(a,b):
#     if a>b:
#         print(a)
#     elif a==b:
#         print("Equal")
#     else:
#         print(b)
#
# great(10,25)
# Q3. Square of a Number
#
# Write a function square(n) that returns the square of a number.
#
# Input: 6
# Output: 36
# 🟡 Level 2 — Functions + Loops
# Q4. Factorial ⭐
#
# Write a function factorial(n) to find the factorial of a number.
#
# Input: 5
# Output: 120

# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#
# n=int(input("Enter a number: "))
# a=fact(n)
# print(a)
# Q5. Sum of Digits ⭐
#
# Write a function digit_sum(n) that finds the sum of all digits.
#
# Input: 12345
# Output: 15

# def sum(n):
#     sum=0
#     for i in str(n):
#         sum=sum+int(i)
#     print(sum)
#
# n=int(input("Enter a number: "))
# sum(n)
#
# Hint: You can convert the number to a string.
#
# Q6. Reverse a Number
#
# Write a function reverse(n) that reverses a number.
#
# Input: 1234
# Output: 4321

# def reverse(n):
#     s=str(n)
#     for i in s:
#         s=s[::-1]
#     print(s)
#
# n=int(input("Enter a number: "))
# reverse(n)
# Q7. Prime Number ⭐
#
# Write a function prime(n) that checks whether a number is prime.
#
# Input: 17
# Output: Prime
# Input: 20
# Output: Not Prime

# def prime(n):
#     if (n>1):
#         for i in range(2,n):
#             if n%i==0:
#                 print("Not prime")
#                 break
#         else:
#             print("Prime")
#     else:
#         print("neither Prime nor composite")
#
# n=int(input("Enter a number: "))
# prime(n)
# 🟠 Level 3 — Important Assessment Questions
# Q8. Palindrome Number ⭐⭐⭐
#
# Write a function that checks whether a number is a palindrome.
#
# Input: 121
# Output: Palindrome
# Input: 123
# Output: Not Palindrome

# def palindrome(n):
#     s=str(n)
#     rev=""
#     for i in s:
#         rev=i+rev
#     if s==rev:
#         print("palindrome")
#     else:
#         print("no")
#
# n=int(input("Enter a number: "))
# palindrome(n)
# Q9. Armstrong Number ⭐⭐⭐
#
# Write a function armstrong(n) to check whether a number is an Armstrong number.
#
# Example:
#
# 153
#
# Because:
#
# 1³ + 5³ + 3³ = 153
#
# Output:
#
# Armstrong Number

# def armstrong(n):
#     s=str(n)
#     sum=0
#     for i in s:
#         sum=sum+int(i)**len(s)
#     if sum==n:
#         print("Armstrong")
#     else:
#         print("Not Armstrong")
#
# n=int(input("Enter a number: "))
# armstrong(n)

# Q10. Spy Number ⭐⭐⭐
#
# You've already started this one. Write the complete function yourself without looking at your previous code.
#
# Example:
#
# Input: 1124
# Output: Spy Number
#
# Because:
#
# Sum = 1 + 1 + 2 + 4 = 8
# Product = 1 × 1 × 2 × 4 = 8

# def spy(n):
#     sum1=0
#     pro=1
#     for i in str(n):
#         sum1=sum1+int(i)
#         pro=pro*int(i)
#     if sum1==pro:
#         print("Spy")
#     else:
#         print("No")
#
# n=int(input("Enter a number: "))
# spy(n)

# 🔴 Level 4 — Strings
# Q11. Count Vowels ⭐⭐⭐
#
# Write a function that counts the number of vowels in a string.
#
# Input: "python programming"
# Output: 4

# def vowel(s):
#     count=0
#     for i in s:
#         if i in 'aeiouAEIOU':
#             count=count+1
#     return count
#
# s=input("Enter String:")
# a=vowel(s)
# print(a)
# Q12. String Palindrome ⭐⭐⭐
#
# Write a function that checks whether a string is a palindrome.
#
# Input: madam
# Output: Palindrome
# Input: hello
# Output: Not Palindrome
# Q13. Count Characters
#
# Write a function that counts how many times each character occurs.
#
# Input: "hello"
# Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#
# def char(s):
#     dic={}
#     for i in s:
#         if i in dic:
#             dic[i]=dic[i]+1
#         else:
#             dic[i]=1
#     return dic
#
# s=input("Enter string: ")
# a=char(s)
# print(a)

# Q14. Word Length Dictionary ⭐⭐⭐
#
# This is similar to the question you already practiced.
#
# Write a function that takes a sentence and creates a dictionary containing each word and its length.
#
# Input:
# python coding is fun
#
# Output:
# {'python': 6, 'coding': 6, 'is': 2, 'fun': 3}

# def length(s):
#     dic={}
#     for i in s.split():
#         dic[i]=len(i)
#     return dic
#
# s=input("Enter string: ")
# a=length(s)
# print(a)
# 🔥 Challenge Question
# Q15. Strong Number
#
# Write a function to check whether a number is a Strong Number.
#
# A number is Strong if the sum of the factorials of its digits equals the original number.
#
# Example:
#
# 145
#
# Because:
#
# 1! + 4! + 5!
# = 1 + 24 + 120
# = 145
#
# Output:
#
# Strong Number

# def strong(n):
#     sum1=0
#     s=str(n)
#     for i in s:
#         fact=1
#         for j in range(1,int(i)+1):
#             fact=fact*j
#         sum1=sum1+fact
#     if sum1==n:
#         print("Yes")
#     else:
#         print("No")
#
# n=int(input("Enter a number:"))
# strong(n)


# def long(s):
#     longest=""
#     for i in s.split():
#         if len(i)>len(longest):
#             longest=i
#     return longest
#
# s=input("Enter string: ")
# a=long(s)
# print(a)
#
# def evenodd(l):
#     count1=0
#     count2=0
#     for i in l:
#         if i%2==0:
#             count1=count1+1
#         else:
#             count2=count2+1
#     return count1,count2
#
# l=[2,3,4,5,6,7]
# a=evenodd(l)
# print(a)



# def perfect(n):
#     sum1=0
#     for i in range(1,n):
#         if n%i==0:
#             sum1=sum1+i
#
#     if sum1==n:
#         print("Yes")
#     else:
#         print("No")
#
#
# n=int(input("Enter a number:"))
# perfect(n)


# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         c=a+b
#         a=b
#         b=c
#
#
# n=int(input("Enter a number:"))
# fibonacci(n)

# def smallest(l):
#     min=l[0]
#     for i in l:
#         if i<=min:
#             min=i
#     return min
#
#
# l=[10,20,30,40]
# a=smallest(l)
# print(a)

# def words(s):
#     count=0
#     for i in s.split():
#         count=count+1
#     return count
#
# s=input("Enter string: ")
# a=words(s)
# print(a)


# l=[1, 2, 2, 3, 4, 4, 5]
#
# def unique(l):
#     l1=[]
#     for i in l:
#         if i not in l1:
#             l1.append(i)
#     return l1
#
# a=unique(l)
# print(a)

# def digits(s):
#     for i in s:
#         if i < '0' or i > '9':
#             print("Not only digits")
#             break
#     else:
#         print("Only digits")
#
# s = input("Enter string: ")
# digits(s)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
#
# def add(a,b):
#     sum1=a+b
#     print(sum1)
#
# def subtract(a,b):
#     difference=a-b
#     print(difference)
#
# def product(a,b):
#     pro=a*b
#     print(pro)
#
# def divide(a,b):
#     div=a/b
#     print(div)
#
# op=input("Enter operator:")
# if op=='+':
#     add(a,b)
# elif op=='-':
#     subtract(a,b)
# elif op=='*':
#     product(a,b)
# elif op=='/':
#     divide(a,b)

































