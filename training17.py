#Errors

#Syntax error would be when you type something wrong

#ZeroDivisionError:
10 * (1/0)
#cuz you can't divide by 0, duh
#this is an exception

4 + spam*3
#NameError: spam isn't defined.

#TypeError:
'2' + 2
#string and integer, can't add them together. 

try: 
    pass
except: 
    pass
#try and except block to help w/ errors


while True: 
    try: 
        user_input = input('Please enter a number: ')
        num = int(user_input)
        break
    except ValueError:
        print('invalid number, please try again.')

#so this asks for a number input, if the user doesn't put in a useable number
#then they send the message

    # except (ValueError, TypeError, NameError):
#This is how to put in multiple errors togeteher

    # except:
#Not recommended, but you can use this for all errors

def turnint(arg):
    return int(arg)

while True: 
    try:
        user_input = input('Please enter a number: ')
        num = int(user_input)
        break
    except ValueError:
        print('Invalid number, please try again')


#You can create your own exceptions as classes

class Error(Exception):
    pass

class FirstError(Error):
    pass

class SecondError(FirstError):
    pass

for cls in [Error, FirstError, SecondError]:
    try:
        raise cls
    except SecondError:
        print('Second')
    except FirstError:
        print('First')
    except Error:
        print('Error')
#Error
#First
#Second
#That order because the first thing in, is Error

#However!!!!
for cls in [Error, FirstError, SecondError]:
    try:
        raise cls
    except Error:
        print('Error')
    except FirstError:
        print('First')
    except SecondError:
        print('Second')

#Error
#Error
#Error
#Why? Because FirstError and SecondError both come from Error. They would go to Error first.
#SecondError is also from FirstError, so even if Error was last, if Second is after First
#IT would be:
#First
#First
#Error


while True: 
    try:
        user_input = input('Please enter a number: ')
        num = turnint(user_input)
    except ValueError:
        print('Invalid number, please try again')
    else: 
        print('success')
        break
#This would not work if there was a break after num

while True asdasafasf:
    print('Hi')
#Syntax error, can't do While True asdasdasfaf:

10/0
#gets ZeroDivisionError
5 + '5'
#TypeError


while True: 
    try: 
        user_input = input('Please enter a number: ')
        num = int(user_input)
    except ValueError:
        print('invalid number, please try again.')
    else: 
        print(num / 2)
        break