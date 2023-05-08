#opening files

f = open('test.txt', 'r')
#if working in different directory, have to use the whole path. test.txt is just in the same directory

#r = reading
#w = write
#a = append
#r+ = read and write

print(f.name)

f.close()
#If you opena  file you must close it at the end.

#this all works, but context managers are better

with open('test.txt', 'r') as f:
#This automatically closes when you're done
    f_contents = f.read()
    print(f_contents)
    #This gives the read file

# read is just the entire file
# readlines is have it in lines using \n instead of actual printing out as written
# readline does a single line. Each time used it does the next line

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='')
    #This prints the first 2 lines. 
    # Note end='' is used to remove line breaks between each line
    #otherwise there would be an empty line

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
        #This goes thru each line individually. 
        #Why good? Only saves one line at a time in memory. Wopn't overload memory

with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)
    #This prints out the first 100 characters in file, also a means of reducing memory load
    #Wach use after the first is the next 100 characters

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='-')
        f_contents = f.read(size_to_read)
#another method w/ while loop
#for every 100 char block. While f_contents > 0 print a line. Then incraese f_contents by the amount printed

with open('test2.txt', 'w') as f:
    f.write('Test')
    #This will create a file if it doesn't exist. But will overwtie a file if it does. 
    #Overwrite meaning it will replace with what you write. 
    #if you don't want to replace just add, then you should use append = a

with open('test2.txt', 'w') as f:
    f.write('Test')
    #writes test
    f.seek(0)
    #brints us back to position 0
    f.write('P')
    #rewrites the letter at position 0 to P. So Test becomes Pest

with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf:
        for line in rf: 
            wf.write(line)
#for test.txt we are opening on read.
#we are creating a new file test_copy
#for each line in test.txt we are writing that line in test_copy

#What if we want to do reading and copy of more complicated files like jpegs?
with open('bronx.jpg', 'rb') as rf:
    with open ('bronx_copy.jpeg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
#rb and wb means write or read in binary. 
#Going chunk by chunk copying and pasting into the new bronx_copy