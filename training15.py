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


#How do classes store their own data?
#Class variables are called attributes

class MyClass: 
    class_attribute = 'value'


class House():
    city = 'barcelona'
    bedroom = 3
    bathrooms = 2
    floor = ['title', 'hardwood', 'carpet']
    has_pool = True

house1 = House()
house2 = House()
#creates two separate instances of one class

house2.city = 'sydney'
house2.bedrooms -= 1
house2.bathrooms -= 1
house2.floor.remove('hardwood')
#The first 3 only change house2
#HOWEVER!!! house2.floor.romove('hardwood') removes from the House object for some reason.

house2.floor = house2.floor.copy()
house2.floor.remove('hardwood')
#this would work
#It has something to do w/ the array I think. Don't know for certain




#functionality is thru methods

mylist = list()
print(mylist)
#[]
print(dir(mylist))
#this will just be the list of methods

#so since classes are like list. we can make functions w/in a class

class MyHouse():
    def mymethod(self):
        print('method ran.')

myhouse1 = MyHouse()

myhouse1.mymethod()
#method ran
#REMEMBER TO PASS IN SELF!

MyHouse.mymthod(myhouse1)
#method ran

#another way to do it. The Class. the method to work with the class. Then the input

myhouse1 = MyHouse('barcelona', 3, 2, ['tile', 'hardwood', 'carpet'], True)

#to get that to work use the dunder method __init__(self)

class MyClass():
    def __init__(self, city, bedrooms, bathrooms, floors, has_pool):
        self.city = city
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.floors = floors
        self.has_pool = has_pool

#then we could use the above myhouse1 and it would work.

#dunder method dunder means double underscore

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Hello my name is {self.name.title()} dont forget it hoe!')

myperson = Person('joe', 33)
myperson.greet