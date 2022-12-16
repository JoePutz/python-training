#some built in functions

player = "Ronaldo"

len(player)
#that will show the length of player which is Ronaldo which is 7

type(player)
#wil show it's a string or str

id(player)
#tells the location in memory of player, which shuold be a long number

dir(player)
#shows the directory

help(player)
#gives documentation, but this one wouldn't have one normally

#you can google the python built in function

#to create a function it is def. Went thru this before.

def printhi():
    print("hi")
    print(player)
#will pring hi /n Ronaldo

def myfunction():
    """ This would be the doc string. the same as # as far as I can tell """
    pass

def myfunction(first_name, last_name): 
    print('Hi')
    print(first_name)
    print(last_name)
#this will be Hi /n first_name /n last_name

help(myfunction)
#IF you enter this, you will get the documentation string! That's cool.
#To exit the help section hit q

#the test section

sentence = "this string"

def printlength(sentence):
    x = len(sentence)
    print(x)

def greeting(input):
    print("Hi")
    print(input)

def add(x, y):
    print(x + y)


