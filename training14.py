#tuples
#immutable, cannot be changed.

mytuple = ('this', 'that', 'other')

singleTuple = ('this',)
#even if a single value, need to have the comma

print(mytuple[1])
#that

for item in mytuple:
    print(item)
#this
#that
#other

del mytuple
#deletes entire tuple, cannot delete individual items

print(list(mytuple))
#['this', 'that', 'other']

#creating a tuple is called packing

#unpacking
var1, var2, var3 = mytuple
print(var1)
#this

#unpacking also works for lists

def myfun(arg1, arg2):
    print(f'{arg1}, {arg2}')

mylist = ['this', 'that']

myfun(*mylist)
#this, that
#the * works for unpacking
#if you had a dictionary ** works the same way

def myfun(arg1, arg2):
    return arg1, arg2

mylist = ['this', 'that']

myfun(*mylist)
#this would be a tuple

mytuple = myfun(*mylist)
print(mytuple)

print(f'{val1}, {val2}')

#Sets
#stores collections of data, and do not allow duplicate values. Unordered

myset = {'val1', 'val2', 'valN'}
print(myset)
#{'val1', 'val2', 'valN'}

myset = list(myset)
print(myset)
#['val1', 'val2', 'valN']
#notice it's a list now w/ []

mylist = ['val1', 'val2', 'val2', 'valN']
print(mylist)
#['val1', 'val2', 'val2', 'valN']
myset = set(mylist)
print(myset)
#{'val1', 'val2', 'valN'}

myset.add('val3')
#adds based on value
myset.remove('val3')
#removes based on value

myset2 = {'val3', 'val4', 'val1'}

myset.union(myset2)
#{'val1', 'val2', 'val3', 'val4', 'valN'}
#mashes together, no repeat values

myset.intersection(myset2)
#{'val1'}
#the only value in both

daysTuple = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

for day in daysTuple:
    print(daysTuple[day])

name1 = {'Joe', 'Jim', 'John'}
name2 = {'Joe', 'Jimbo', 'James'}

name1.intersection(name2)

emptyTuple = ()
emptyTuple = tuple()
#both make empty tuples