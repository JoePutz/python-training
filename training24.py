if True:
    print('Conditional was True')

#This owrks in normal python

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif langauge == 'Javascript':
    print('Language is Javascript')
else: 
    print('No match')
#This shows how to do else if

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in: 
    print('Admin Page')
else:
    print('Bad Creds')
#Shows that and can be the same as && in JS

if user == 'Admin' or logged_in: 
    print('Admin Page')
else:
    print('Bad Creds')
##Or is ||

if not logged_in: 
    print('stuff')
#not just does makes work on False

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
#True
print(a is b)
#False
#they have 2 different ids, even though they match

c = [1, 2, 3]
d = c
print(c is d)
#True

#False is False
#None is False
#when wokring wiht numbers, condition being 0 evaluates to False
#Empty sequences: '', (), {} are all False
#everything else goes to True

#LOOPS AND STUFF

nums = [1, 2, 3, 4, 5]

for num in nums: 
    if num == 3:
        print('Found!')
        break
    print(num)
#prints all the numbers until 3, and then prints out Found. Break ends the loop.

#to ignore value but not break out: Continue

for num in nums:
    if num == 3: 
        print('Found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)
#1 a, 1 b, 1 c, 2 a, 2 b, 2 c, 3 a, 3 b, 3 c, ...

for i in range(10):
    print(i)
#prints 0  thru 9

for i in range (1, 11):
    print(i)
#prints 1 thru 10

x = 0

while x < 10: 
    print(x)
    x += 1
#prints 0 thru 9

#while's go on forever unless you have a means for it to break out of the loop
#in this example the increasing of x along with the while x < 10 will end it.

while True:
    # if x == 5:
    #     break
    print(x)
    x += 1
#this is an infinite loop that thankfully has a different end condition

#If you ever have an infinite loop that isn't interrupted, you can stop the program w/ Ctr C


