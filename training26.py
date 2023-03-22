#modules
import my_module as mm
#This works because my_module is in the same directory/folder
#as mm, means we can call on my_module just by typing mm

#we could have also done from my_module import find_index, test
#this would only import those two things

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

#from my_module import *
#this imports everything, but it is usually frowned upon. As it difficult to figure out where things came from

import sys

print(sys.path)

#What if the module is in a different directory?
#we can add the directory to sys.path
#sys.path.append('/Users/root/Desktop/My_Modules')

import random
#This is from the standard library

random_course = random.choice(courses)
print(random_course)

#some common standard library
#math
#datetime, works w/ dates and times
#calendar, similar but has some different things in it
#os, works directly w/ files