#loops
for item in iterable:
    pass
#this is the rough outline

player = 'Neymar'

for item in player:
    print(item)
#would pring the name w/ 1 letter on each line

count = 0

while count <= 5:
    print('Hey')
    count +=1
#prints Hey! 6 times

#if you didn't add the count+=1 part it would run forever

#continue and break are also important. 

while count <= 5:
    print('hey!')
    continue
    print(count)
#the continue will make it skip everything that's after it. So this would not print the count, just loop the Hey!

#break of course would break the while to stop it

while count <= 5:
    print('hey!')
    if count == 3:
        break
#this owuld just do Hey! to get to 3 then break.

mylist = ['Ronaldo', 'Messi', 'Neymar']

for item in range(0, len(mylist), 2):
    print(item)
#this would proint every other name in the list
#Renaldo, Neymar

if 'Ronaldo' in mylist:
    print('Yes!')
#Yes!

if 'Ronaldo' not in mylist:
    print('No')
else:
    print('Yes')

myotherlist = []

for item in mylist:
    if 'e' in item:
        myotherlist.append(item)
print(myotherlist)
#Messi, Neymar



testlist = ['cool','things', 'im', 'writing']

for item in testlist:
    print(item)

count = 0
while count < len(testlist) - 1:
    print(testlist[count])
    count += 1

for item in range(0, len(testlist), 2):
    print(mylist[item])
#so from the range of 0 to the length of testlist, every other answer
#cool, im
