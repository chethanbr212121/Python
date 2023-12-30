import os
# Print current directory.
# print(os.getcwd())

# Change directory.
# os.chdir('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files')
# print(os.getcwd())

# Create new directory.
# os.mkdir('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/')

# Change directory using dot
# os.chdir('.')
# os.chdir('..')
# print(os.getcwd())

"""Calling os.path.abspath(path) will return a string of the absolute path of the argument. 
This is an easy way to convert a relative path into an absolute one."""
# print(os.path.abspath('.'))

''' Calling os.path.isabs(path) will return True if the argument is an abso-
lute path and False if it is a relative path.'''
# print((os.path.isabs('.')))
# print((os.path.isabs(os.path.abspath('.'))))

# path_name = '/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/Read_write_file_1.py'
# print(os.path.basename(path_name))    ## returns files name
# print(os.path.dirname(path_name))     ## Returns full path.

## Finding File Sizes and Folder Contents
'''Calling os.path.getsize(path) will return the size in bytes of the file in
the path argument'''
# print(os.path.getsize('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/Read_write_file_1.py'))

'''Calling os.listdir(path) will return a list of filename strings for each file
in the path argument. (Note that this function is in the os module, not
os.path.)'''
# print(os.listdir('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/'))

# To find total size of all files in folder.
''' Total_size = 0
for files in os.listdir('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/'):
    Total_size = Total_size + os.path.getsize(os.path.join('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/', files))

print(Total_size)'''

## Checking Path Validity
# print(os.path.exists('/home/chethan/Documents/Coding'))   ## return TRUE because this path exist in my local.

# print(os.path.isdir('/home/chethan/Documents/Coding'))    ## return True because it is a directory.

# print(os.path.isfile('/home/chethan/Documents/Coding'))    ## return False because it is a directory not a file.


# open files and read contents.
# file_1 = open('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Code with harry/1.txt')
# print(file_1.read())
# print(file_1.readlines())

# Open file and write text to file.
# file_3 = open('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/write.txt', 'w')
# file_3.write('First lines')
# file_3.close()
# read text from file
# file_3 = open('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/write.txt')
# print(file_3.read())

# Append text to file.
# file_3 = open('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/write.txt', 'a')
# file_3.write('Second lines, \n')    ## \n for new line
# file_3.close()
# read text from file
# file_3 = open('/home/chethan/Documents/Coding/Pycharm/Python_Practice/chethan_Project/Read_write_files/write.txt')
# print(file_3.read())


































