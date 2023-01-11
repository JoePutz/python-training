#object-oriented, everything is an object
var1 = 'this string'
type(var1) 
#this would say "str"
print(var1)
#would show: this string

var1.upper()
#this would show: 'THIS STRING'

var1.tite()
#'This String'
var1.count()
#this would be wrong. it's an error
#count() requires an error
var1.count(i)
#would show: 2
#because there are 2 i's in 'this string'

dir(var1)
#this would show all the potential methods for a string

myvar = '     Hi.How.Are.You     '
myvar.strp()
#this removes all unneeded spaces.
#would show: 'Hi.How.Are.You'

myvar.replace('.', ' ')
#this replaces all instances of the first variable with the second
#would show: Hi How Are You

print('this' + 'string')
#would be thisstring
print('this' + ' ' + 'string')
# this string

var1 = 'Dude'
print('Hey, ' + var1)
#Hey, Dude

print('Go! ' * 3)
#Go! Go! Go! 

var2 = 3
print('Number: ' + var2)
#this would be a type error. can't concatenate (add on) integer to a string

print('Number: ' + str(var2))
#This would work. str() is apparently how you turn integers into strings

type(str(3))
#should say it's a string

print('This is a {} string!'.format('formatted'))
#This is a formated string!

print('This is a {} string!'.format('random'))
#This is a random string!

print('This is how you enter value {} and value {}'.format(1, 2))
#This is how you enter value 1 and value 2

print('The second positional parameter is {1} and the first is {0}'.format(1, 2))
#The second positional parameter is 2 and the first is 1. 
#See how {1} is the second number and {0} is the first? Neat

print('{0:>5}|{1:^10}'.format('one', 'two'))
#  one|     two     
#The first number is the index. meaning what it will put in the {} so 'one' and 'two'
#The carrots > and ^ mean alignment
#> right aliengment, < left alignment, ^ center alignment
# So the first one is 'one' with alignment of 5 from right. So:
#(space)(space)one. Because two spaces plus each symbol of one = 5
#   two    :spaces before and after the word, plus the symbols of two = 10
#Can use this to format a table

print('{1:5}|{0:>10}'.format('one', 'two'))
#two  |       one
#notice how the first doesn't have a carrot? You can use < but that's the generic one


#F strings are the most useful

print(f'This prints myvariable: {var1}')
#This prints myvariable: Dude
#The f in front of the string makes it all work. Like #{} did for javascript

def greeting(name):
    print('Hey there, ' + name + '!')

def greeting1(name):
    print('Hey there, {}!'.format(name))

def greeting2(name):
    print(f'Hey there, {name}!')


def table():
    print('{0:^10}|{1:^10}'.format('one', 'two'))



