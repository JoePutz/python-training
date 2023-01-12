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


