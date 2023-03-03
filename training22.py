int = 2

print(type(int))
#class: int

flo = 2.53
print(type(flo))
#float

print(3+2)
#5

print(3/2)
#1.5

print(3//2)
#1
#This is a floor division. Which means the largest possible integer.

print(3**2)
#9

print(3 % 2)
#1
#called a modulo, but all that means is the remainder

print(3 * 2 + 1)
#7

print(3 * (2 + 1))
#9

#order of operation works correctly in python

num = 1
num = num+1
#num now equals 2
num += 1
#this does the same thing

print(abs(-3))
#3 
#absolute value

print(round(3.75))
#4

print(round(3.75, 1))
#3.8


num_1 = 3
num_2 = 2

print(num_1 == num_2)
#False

print(num_1 != num_2)
#True

print(num_1 < num_2)
#False

#works for all the usualls, ==, !=, >, <, >=, <=
#only important thing, don't really use ===

num_1 = '100'
num_2 = '200'
#these are strings
#how to add together?
print(num_1 + num_2)
#100200

#how to fix? 

num_1 = int(num_1)
#it is now an integer and we can add it together.