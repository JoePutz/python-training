#This goes over functions

#This is the absolute value
abs(-5)

#Max of two values
max(5, 7)

#This is a method to split the the string on the commas
"a,b,c".split(",")
#This should equal ["a", "b", "c"]


#The method for getting functions from a library
#This one allows the reading of a page
from urllib.request import urlopen

page = urlopen("http:....")

page.read()
#This will print out the contents of a webpage


text = input("Text: ")
emails = text.split(",")
output = "\n".join(emails)
#This will run to a page that says Text: Then you could write whatever you want and it will create a list of what you wrote with each section between commas on a different line

#Call min
min(2, 6)

#max
max(2, 6)

#sum of numbers
sum([4, 7, 9, 3])

#all returns if all booleans are true. this will be false
all([True, False, False])

#returns if any are True this is true
any(True, False, False)

#lower takes 0 arguments and makes the lower case of a string
"HAHAHA".lower()

#This will remove all leading spaces so will be 'hehe'
" hehe".lstrip()

#endswith takes 1 string argument and returns True if string ends w/ argument
"he@d.com".endswith(".com")

"Mr. Bean".startswith("Mr.")

#this will find the position of the string it's finding. This will give me 5. 
"supercalifragilistic".find("cali")

#count is the total number.this should be 4
"mississippi".count("i")

#replace takes 2 arguments. this should give us hehehehe
"hahahaha".replace("a", "e")

"Bob poked Bob's dog".replace("Bob", "Jon")
#Jon poked Jon's dog"

#values lists all values in a dictionary. This gives [1, 2]
{"a": 1, "b": 2}.values()

#keys returns the keys, this should give ["a", "b"]
{"a": 1, "b": 2}.keys()

#This joins ths input together separated by / so it will be google.com/mail/hi
"/".join(["google.com", "mail", "hi"])

#so now we're building our functions
def square (x):
  return x*x
#This is the syntax, like JS but no {} it's all in : and then 2 spaces for what's inside

square(5) 
#This will equal 25

#This should go at the top of the file
from urllib.request import urlopen

def get_temperature(city):
    url = "https://wttr.in/" + city + "?format=%t"
    page = urlopen(url)
    raw = page.read()
    temp = raw.decomde("utf-8")
    return temp

city = input("City: ")
temp = get_temperature(city)
print(temp)


def mul3(x):
    return 3*x

def sub3(x):
    return x - 3

def prod(x, y): 
    return x * y

def add(x, y): 
    return x + y

def prod(x, y, z): 
    return x * y * z

#This will return a true/false boolean 
def gt3(x):
    return x > 3

def lt10(x):
    return x < 10

#Will return true only if both are true
def both_gt_3(x, y):
    return x > 3 and y > 3

#takes a list, and sums the entire list, then multiplies the sum by 3
def sum3(lst):
    return sum(lst) * 3

def sumv(dict):
    return sum(dict.values())

def is_jack_one(dict):
    return dict["jack"] == 1

def add3_jack(dict):
    return dict["jack"] + 3