#files

fileobj = open('filename.txt')
#this is a relative file path, it assumes the same folder as we're in

fileobj1 = open('C:/User/joe/folder_name/...')
#this is if it's in a different folder

fileobj.tell()
#0

print(fileobj.read())
#starts at the current position and goes all the way to the end.

fileobj.tell()
#58
#this shows that it reached the end of the file from read()

fileobj.seek(0)
#0
#returns to 0

fileobj.closed
#False

fileobj.close()
#this acutally closes the file

fileobj.closed
#True

#remember to close when done to fix memory

with open('example.txt') as fileobj:
    for line in fileobj:
        print(line)

#This is the first line
#
#Second line
#
#Finally, the third line

with open('example.txt')  as fileobj:
    for line in fileobj:
        print(line.strip())
#This is the first line
#Second line
#Finally the third line

with open('newfile.txt', 'w') as fileobj:
    fileobj.wirte('new text \n is nice \n lines are fun')
    for line in fileobj:
        print(line.strip())

