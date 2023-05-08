#writing a python script to change file names

#We have a list of files, that should be read in order, however, all of them have the number somewhere within the file name, not the front
#How do we work through the system to reorganize correctly / rename the files?

import os

os.chdir('/Users/coreyschafer/Projects/Demos/Python/Videos')
#This will gibe us all the files.

for f in os.listdir():
    print(os.path.splitext(f))
    #This would print a tuple of the title and file extension. So: 'Earth - Our Solar System - #4', '.mp4'

#what if we want to call these split paths? 
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f)
    print(f_name)
    #this would just print each file name
    f_title, f_course, f_num = f_name.split('-')
    #this would split the file_name based on '-' to use our example we would have:
    # 'Earth', 'Our Solar System ', ' #4'
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    #This would set up what we want, but a little weird. Ex: 
    #' #4- Our Solar System -Earth .mp4' See how the unwanted ' ' are weird?
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
    #.strip() removes whitespace
    #So ex: 
    #'#4-Our Solar System-Earth.mp4'
    f_num = f_num[1:]
    #This will strip off the '#' at the start of the thing
    f_num = f_num.zfill(2)
    #This will turn 1, 2, 3, etc. into 01, 02, 03, etc. 
    #Why? 
    #This will make the program do the correct order, instead of probably going from 1 to 10 to 2, etc.
    
    #whatif we want to remove the course? We don't need it: 
    new_name = '{}={}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name)

#Alright let's do this the streamlined no explanation way: 

for f in os.listdir():
    f_nmae, f_ext = os.path.splitext(f)

    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)
