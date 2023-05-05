import os

print(dir(os.getcwd()))
# get current working directory

#os.chdir('/Users/JoesLaptop/Desktop/')
# change directory

os.mkdir('OS-Demo-2')
#This one goes 1 deep
os.makedirs('OS-Demo-3/Sub-Dir-1')
#This one makes multiple levels, such as the above sub directory 1

print(os.listdir())

os.rmdir('OS-Demo-2')
# deletes directory

os.rename('test.txt', 'demo.txt')
#rename the first fite to the second file

print(os.stat('demo.txt').st_size)
#os.stat('application) shows the statistics of the given file
# prints out the size of the file
print(os.stat('demo.txt').st_mtime)
# prints the time last modified

os.walk()
#generator yields tuple (3 things) directory, directoy path, and the files w/in that path
#so for example it will show the directory path, the directory names within that path, and the files within those
# Goes thru the entire directory, the entire path, down the entire everything. 

os.environ.get('HOME')
#This captures the home directory

#what if we want to create a file w/in that home directory? 
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
#This just would show the path, it apparently doesn't create the file. 

os.path.basename('/tmp/test.txt')
# Grabs the file name that we're working. The basename of above is just 'text/txt

os.path.dirname('/tmp/test.txt')
#Grabs the directory of the file. In this case itwould be tmp

os.path.split('tmp/test.txt')
#Gives a (dirname, basename)

os.path.exists('/tmp/test.txt')
# T/F if the file exists

os.path.isdir('/tmp/test.txt')
#T/F if directory

os.path.isfile('/whatever')
#T/F if a file

os.path.splitext('/tmp/test.txt')
#('/tmp/test', '.txt')

dir(os.path)
#this will show all the other functionality 