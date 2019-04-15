#! python3
# openingFiles.py - Learning how to open files in Python

#1. Call the open() function to return a File object
#2. Call the read() or wirte() method on the File object
#3. Close the file by calling the close() methond on the File object

# With open() you can only read data
helloFile = open('S:\\Documents\\GitHub\\ATBS\\Chapter_8\\hello.txt')

# Reading the file
helloContent = helloFile.read()
print(helloContent)
helloFile.close()

sonnetFile = open('.\\Chapter_8\\sonnet29.txt')
print(sonnetFile.readlines())
sonnetFile.close()