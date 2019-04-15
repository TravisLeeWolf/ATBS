#! python3
# files.py - Learning file control in Python

# Always import os when dealing with files
import os

# Returns the working directory of a program
print(os.getcwd())

# Returns string of the absolute path
print(os.path.abspath('.\\Chapter_8'))

# Returns boolean if path is absolute path
print(os.path.isabs('.'))

# Basename and dirname
path = 'S:\\Documents\\GitHub\\ATBS\\Chapter_8\\files.py'
pathDirname = os.path.dirname(path)
print(os.path.basename(path))
print(os.path.dirname(path))

# Get dirname and basename in a tupple
print(os.path.split(path))

print()
# Getting file sie and folder contents
print(os.path.getsize(path))
print(os.listdir(pathDirname))

# Total size of ATBS
totalSize = 0
for filename in os.listdir('S:\\Documents\\GitHub\\ATBS'):
    totalSize = totalSize + os.path.getsize(os.path.join('S:\\Documents\\GitHub\\ATBS', filename))
print(totalSize)        

print()
# Check if dir or file exists
print(os.path.exists(pathDirname))
print(os.path.isfile(path))