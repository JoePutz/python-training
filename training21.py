my_message = 'Hello World'
#'' and ""  are kinda the same. However if you use a ' in the string "" wors better, pr \'
#all are the same
other_message = 'He\'s here'
other_message_2 = "He's here"

print(my_message)

long_message = """Bobby's World was a good cartoong
in the 1990s
I watched it"""
#""" works for multiple lines
print(long_message)

message = 'Hello World'
print(len(message))
#length of the message
print(message[0])
#index of 0. Get "H"
print(message[-1])
#index of the last. "d"
print(message[0:5])
#a range from 0 to 4. Does not include the last index. "Hello"
print(message[:5])
#"Hello" assumes it starts at 0
print(message[6:])
#from 6 to end. "World"

print(message.lower())
#hello world
print(message.upper())
#HELLO WORLD
print(message.count('Hello'))
#1
print(message.count('l'))
#3
print(message.find('World'))
#6 where it can be found
print(message.find('Sup'))
#-1

message.replace('World', 'Universe')
print(message)
#Hello World
#Why? because replace makes a new string

new_message = message.replace('World', 'Universe')
print(new_message)
#Hello Universe

greeting = 'Hello'
name = 'Michael'

message = greeting + name
print(message)
#HelloMichael

message = greeting + ', ' + name
print(message)
#Hello, Michael

#formated string
message = '{}, {}'.format(greeting, name)
print(message)
#Hello, Michael
#This is easier with more complex strings

#f strings
message = f'{greeting}, {name}'
print(message)

message = f'{greeting}, {name.upper()}'
print(message)
#this works, we can do methods in the brackets

print(dir(name))
#short for directory, shows all functions that work on name

print(help(str))
#This also gives descriptions and arguments

print(help(str.lower))
#tells you what lower does