#module
#A file that contains python objects

#you could then import the concepts of a different file to this file

import example
#this imports example.py

print(example.addtwo(5))
#7

def main():
    print(example.addtwo(5))

if __name__ == '__main__':
    main()
#This will print it normally, NOT USING THE MAIN() FROM EXAMPLE

import time
#This works because python has some modules that are just pre-set up
time.sleep(1)
print(time.localtime())

#can also import just parts of a module

from time import sleep, localtime


import random as rand
# we imported random, and then we called it just rand

mylist = ['a', 'b', 'c']

rand.shuffle(mylist)

print(mylist)
#this printed a randomized version of mylist

from time import sleep

for item in range(5):
    print(item)
    sleep(1)
#SO this printed out 0, 1..4 but it waited a second after each number