def myfunction(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

myfunction('this', 'that')
#this would be an error, as there's no 3rd argument

def myfunction(arg1, arg2, arg3 = 'devault_value'):
    print(arg1)
    print(arg2)
    print(arg3)

myfunction('this','that')
#this would work, as it would just be default_value

myfunction(arg2 = 'that', arg3 = 'other', arg1 = 'this')
#this also works, and can be in a different order. Neat

def addnums(num1, num2):
    results = num1 + num2
    return results

addnums(5, 10)
#this won't show anything, because it would just return the number. which would just go nowhere

print(addnums(5, 10))
#this would print it

def myfunction(*args, **kwargs):
    print(args)
    print(kwargs)
#What this is saying is an arbitrary number of arguments, and an arbitrary number of keyword arguments.
#print the arguments
#print the key word arguments


myfunction(1, 2, 3, 4, val1 = 'this', val2 = 'that')
#(1, 2, 3, 4)
#{'val1': 'this', 'val2': 'that'}
#that's interesting. It prints with the () and {}


def defaultfunc(x = 'default'):
    print(x)

def arbitraryfunc(*x, **y):
    print(x)
    print(y)

def function(x):
    var1 = x
    print(x)

