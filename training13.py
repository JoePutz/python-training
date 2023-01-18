#dictionaries

example = {}
#empty dictionary

mydict = {'first_name': 'John', 'last_name': 'Smith'}

print(mydict['first_name'])
#John

print(mydict['age'])
#KeyError

print(mydict.get('age'))
#None

print(mydict.get('age', 'does not have age'))
#does not have age

mydict['age'] = 27
#this would add the new key/value pair to mydict

mydict['first_name'] = 'Mike'
#this overwrites John

del mydict['last_name']
#Removes both the key and value

print(mydict.keys())
#dict_keys(['first_name', 'last_name', 'age'])
print(mydict.values())
#dict_values(['Mike', 'Smith', '27'])
print(mydict.items())
#dict_items([('first_name', 'Mike'), ('last_name', 'Smith'), ('age', '27')])

if 'first_name' in mydict.keys():
    print('yes')

#dictionaries are not ordered, so if you loop it might not come out in the right order

for item in mydict.keys():
    print(item)
#first_name
#last_name
#age

for key, value in mydict.items():
    print(f'key: {key}, value: {value}')
#key: first_name, value: Mike
#key: last_name, value: Smith
#key: age, value: 27

contact = {'name': 'Joe', 'age': '33', 'email_address': 'josephputz89@gmail.com'}

print(contact['email'])
#this is different form contact.get('email') as it will error if there's none

contact['age'] = 34
#changes the age

for key in contact.keys():
    print(key)

for value in contact.values():
    print(value)

for key, value in contact.items():
    print(f'key: {key}, value: {value}')
