# write a program to check the entered number is positive even/positive odd
# negative even/ negative odd

num1 = int(input("Enter a number: "))
if num1>0:
    if num1%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    if num1%2==0:
        print("negative even")
    else:
        print("negative odd")