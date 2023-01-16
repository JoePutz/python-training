#lists

mylist = ['item1', 'item2', 'item3']
print(mylist)

emptylist = []

print(mylist[0])
#item1

print(mylist[-1])
#item3

mylist.append('new_item')
#adds the item to the end

mylist.insert(1, 'inserted_item')
#['item1', 'inserted_item', 'item2', ...]

del mylist[1]
#removes inserted_item

mylist.remove('item1')
#removes where that is

mylist.pop()
#removes the last item of list and returns it

print(mylist.pop())
#this will print the last item that has now been removed

print(mylist[0:2])
#this would print from 0 to the number before the second number. Strongely. so 0, 1 but NOT 2

print(mylist[1:])
#goes from 1 to the end

print(mylist[:3])
#goes from beginning to 2

print(mylist[-2:])
#the last 2 numbers of the list

print(id(mylist))
#this would make the number that represents the list

mylist_copy = mylist

print(mylist_copy.pop())

print(mylist)

#this will modify both mylist and the copY!!!!
#this is because both mylist and the copy are the same object

#we can get around this w/
mylist_copy = mylist.copy()
mylist_copy = mylist[:]
#any changes to copy will no longer change original


mylist.index('item2')
#this will return the number where that is on mylist so for the original list it would be 1

mylist = ['apple', 'elephant', 'car', 'etc.']
mylist.sort()
#this will put them alphabetical

sorted(mylist)
#this will return the list as if it was sorted, but won't actually sort the list

range(5)
#returns range(0, 5)

list(range(5))
#[0, 1, 2, 3, 4]

list(range(1, 5))
#[1, 2, 3, 4]

list(range(1, 5, 2))
#[1, 3]
#so go from 1 to 5, but every 2 increments. Basically all odd numbers from 1 to 5

list(range(1, 20, 2))
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

mylist = list(range(1, 20, 2))

min(mylist)
#1

max(mylist)
#19

sum(mylist)
#100

testlist = [1, 'hi', False, 50, 'this', True]
del testlist[3]
testlist.remove(False)
print(testlist[1:5])
testlist_copy = testlist[:]
#or testlist_copy = testlist.copy()

#sort actually sorts the list, sorted shows what the list would be if sorted (so kinda temporary)

list(range(5))
#this would be [0, 1, ... 4]

list(range(2, 5))
#[2, 3, 4]

list(range(5, 25, 5))
#[5, 10, 15, 20, 25]