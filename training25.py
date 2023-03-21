#functions and stuff

def hello_func():
    pass
print(hello_func)
#This does not execute the func

def hello_func2():
    print('Hello Function!')

hello_func2()
#Hello Function!

#return vs print
#return doesn't print anything on the screen, but it stores the info. Print has the info display on our terminal

#print(hello_func2().upper())
#HELLO FUNCTION!
#why didn't that work?

def hello_func3(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)
print(hello_func3('Hi')) 
#Hi You

print(hello_func3('Hi', name="Bob"))
#Hi Bob

#THe second is the keyword argument. 

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
#arguments and keyword arguments

student_info('Math', 'Art', name='John', age=22)
#('Math', 'Art')
#{'name': 'John', 'age': 22}

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)
#('Math', 'Art')
#{'name': 'John', 'age': 22}

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017, 2))