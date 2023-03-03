#dictionaries

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#these are key: value pairs

print(student['name'])
#John

#the keys do not have to strings, but most are strings or integers

#print(student('phone'))
#error. edited out now so it doesn't mess up other work

print(student.get('name'))
#John

print(student.get('phone'))
#None

print(student.get('phone', 'Not Found'))
#Not Found

student['phone'] = '555-5555'
#this adds a new key: value pair

student['name'] = 'Jane'
#this also edits 

print(student['name'])

student.update({'name': 'Johnny', 'phone': '552-5555', 'awesome': True})
#This update will take in a dictionary itself to update all of the original student dictionary
print(student)

del student['age']
#this deletes the age key:value

awesome = student.pop('awesome')
#another method of deleting a key:value pair.
print(student)
print(awesome)
#True
#Though it is deleted from the dictionary, it is still saved as the variable awesome

#looping thru the dictionary

print(len(student))
#3
#how many keys we have

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)