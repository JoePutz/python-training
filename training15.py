#Classes and object oriented programming

#provide means of bundling data and functionality together
#new class is a new type of object
#allows new instances of that type made
#can have attributes attached to it for maintaining state.
#instances can also have methods (defined by its class) for modifying state

#think of class and blueprint as houses made w/ blueprint. Classes are the blueprint, instances are each individual house made w/ that blueprint

mylist = ['a', 'b', 'c']
print(type(mylist))
#<class 'list'>

list()
tuple()
dict()
#each of these are also classes. 
#makes sense, they are the outline for how a set of data can be interacted w/

class MyClass():
    pass
print(type(MyClass))
#<class 'type'>
#this means its a class of itself


myclass1 = MyClass()

print(type(myclass1))
#<class '__main__.MyClass'>
#main means it's the current script running, the main script
#MyClass is what is running. 
#so it's class is the MyClass class within the main script

#practice
#list is a class, just like int, str, dict, tuple, etc.
#mylist = ['a', 'b', 'c']
#mylist is an instance of the list class
