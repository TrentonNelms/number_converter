import math 
from math import sqrt

user_num = int(input('Enter an integer:\n'))
sqrt = math.sqrt(user_num)
square = user_num ** 2
cube = user_num ** 3

print('You entered: '), user_num

print ('The square root of'),user_num, ('is'), sqrt

print user_num, ('squared is'), square

print user_num,('cubed is'), cube

user_num2 = int(input('Enter another number:\n'))

print user_num, '+', user_num2, 'is', 
print user_num + user_num2

print user_num, '*', user_num2, 'is', 
print user_num * user_num2

print user_num, '/', user_num2, 'is', 
print user_num / user_num2

print user_num, '-', user_num2, 'is', 
print user_num - user_num2

print user_num, '%', user_num2, 'is', 
print user_num % user_num2