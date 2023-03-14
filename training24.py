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