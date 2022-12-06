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