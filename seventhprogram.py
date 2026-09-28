#write a program to interchange(swap) two variables
from tempfile import tempdir
#
a = 2
b = 3

# #using temporary variable
#
# temp = a
# a = b
# b = temp
#
# print(a)
# print(b)

#without using 3rd variable

a,b = b,a
print(a)
print(b)

