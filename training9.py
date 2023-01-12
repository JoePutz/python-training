input()
#this would be user input

user_input = input()


input('Please enter input: ')
# this is how you do the prompt for the user.

my_integer = 5

my_float = 5.12

type(my_integer)
#int

type(my_float)
#float

num1 = 4
num2 = 2

num1 + num2
#6

num1 - num2
#2

#so on and so forth. with multiplication and division. 
#Division always returns a float
#** is exponential and % is remainder

input('enter number: ')
#This returns a string, even if the input is a number

var1 = input('enter number: ')
type(var1)
#str

var1 = int(var1)
#turns into integer

var1 = float(var1)
#turns into a float


""" this is a multiple line comment
neat
i didn't know this
weird"""

def weirdInput():
    num = input('enter number: ')
    num = float(num)
    return num ** 2

def weirdInput2():
    num = input('enter number: ')
    num = int(num)
    if num % 2 == 0:
        print('even')
    if num % 2 != 0:
        print('odd')


#conditional statements
#essentially if /then or whatever. in python this is all in booleans.

hungry = True
if hungry: 
    print('Getting a sandwich.')

#That's it. since hungry is true, running this code will produce "Getting a sandwich"

lazy = False

if lazy:
    print('doing nothing')
elif hungry:
    print('getting sandwich')
else: 
    print('else statement')

#This shows: getting sandwich
#First it checks lazy. That is false. So goes to the next statement. Hungry is true, so goes there

if None:
    print('this')
if '':
    print('this')
if 0:
    print('this')
if 'this':
    print('that')
#that
#everyhting else goes to False

var1 = 2
var2 = 5

if var1 == var2:
    print('this')
#does nothing

if var1 < var2:
    print('this')
#this

if True and True:
    print('this')
#this

if True and False:
    print('this')
#this doens't print anything, becuase False is False

if True or False:
    print('this')
#this
# since it's 'or' True is True and that's enough

if not True or False:
    print('this')
#nothing happens

#'and' and 'or' returns what it represents
'this' and ''
#returns '' as that shows False

'this' and 'that'
#that, becuase tha'ts the last value

'this' or 'that'
#'this' as this is the first one that works

'' or 'that'
#'that' as taht's the one that actually returned True

'fire' if True else 'ice'
#'fire' 
#this is a shorthand statement to do an either or. 

def grade():
    val = int(input('insert number: '))
    if val >= 94:
        return 'A'
    if 80 <= val < 94:
        return 'B'
    if 70 <= val < 80:
        return 'C'
    if val < 70:
        return 'failed'

myvar = None

'fire' if myvar else 'ice'
#should be 'ice'

'fire' if not myvar else 'ice'
#should be 'fire'


