#lists and tuples and sets

courses = ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))

print(courses[1])
#reminder on index, starts on 0 and all that. 

courses[-1]
#this is the last number

courses[0:2]
#this is the starting and stopping point. does not include second index. So this would be
#History, Math

courses.insert(0, 'Art')
print(courses)
#this made Art at 0. Pushed everything else back

courses_2 = ['Art', 'Education']

courses.extend(courses_2)
#This adds each items individually

courses.append(courses_2)
#this would add a single new index that has both Art and Education. Not what we want

courses.pop()
#Removes last value
#returns tha value so
popped = courses.pop()
print(popped)

courses.sort()
#this shuold be alphabetical, or numerical order depending on the list

courses.sort(reverse=True)
#this sorts things backwards. Neat

sorted(courses)
#This returns a new sorted list
#So
sorted_courses = sorted(courses)

num = [1, 2, 3, 4, 5]
sum(num)
#gives sum

courses.index('Art')
#would give the index where art is.
#Value error if not there

print('Art' in courses)
#gives a True or False

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)
#we can access index and value with enumerate function, returns both index and value
#start=1 is a start value, which would essentially ignore what's on position 0. 

course_str = ' - '.join(courses)
#This creates a single string of teh values with - between them
new_list = course_str.split(' - ')
#Returns to initial list

print(course_str)
print(new_list)


#Tuples

#Can't modify tuples. immutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
#These are the same object.
#Changing either of them changes both of them.

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

#tuple_1[0] = 'Art'
#This will get ERROR: TypeError: 'tuple' object does not support item assignment

#Sets
#Unordered and have no duplicates

cs_courses = {'History', 'Math', 'Physics', 'Compsci'}
#If I print this, it might show up in the wrong order.


cs_courses = {'History', 'Math', 'Physics', 'Compsci', 'Math'}
#If I print this, then it will remove the second Math

print ('Math' in cs_courses)
#Prints: True

art_courses = {'History', 'Math', 'Art', 'Design'}

#Test if something is in either.

print(cs_courses.intersection(art_courses))
#{'History', 'Math'}

print(cs_courses.difference(art_courses))
#{'Physics', 'Compsci'}
#It's specifically the ones just in cs_courses

print(cs_courses.union(art_courses))
#Unique values from both sets

#Empty codes
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()
#empty_set = {} creates a Dictionary! Not a Set. Funky.