#range and for loops
#range(10) with return range(0, 10)

iterable = range(10)
list(iterable)
#this should give [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#for loop
for i in range(10):
    print(i)
#this should print the above iterable one line for each segment

list("Hello World")
#["H", "e", 'l", "l", "o", "", ... "d"]

for i in "Hello World":
    print(i)
#this will print the above list each symbol on a line

def check(password):
    has_number = False
    for i in password:
        if i.isdigit():
            has_number = True
    return has_number
#This will take a password, it will iterate through every symbol in password, check if the symbol is a number. 
#If it is a number, turns has_number to true. Once gone through every symbol returns if it has a number or not

password = input("Password: ")
has_number = check(password)
print(has_number)
#This will start a program with the input. When you enter it will pop out either True or False if the input has a number

def print_list(lst):
    for string in lst:
        print(string)

def print_gt3(lst):
    for number in lst:
        print(number > 3)

def print_add3(lst):
    for number in lst:
        print(number + 3)

def print_a_names(lst):
    for name in lst:
        if name.startswith("A"):
            print(name)

def print_nums_gt3(lst):
    for number in lst:
        if number > 3:
            print(number)

def get_name(lst):
    for name in lst:
        if name.startswith("A"):
            return name
#RETURN ENDS THE FUNCTION. So this will stop after the first name that starts w/ A

def get_odd(lst):
    for number in lst:
        if number % 2 == 1:
            return number


