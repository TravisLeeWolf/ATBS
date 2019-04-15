#! python3
# writingFiles.py - Learning how to write files in Python

# Writing to a file replaces any previous information
baconFile = open('.\\Chapter_8\\bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

# Appending to a file adds after previous entries
baconFile = open('.\\Chapter_8\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

# Read the file and print contents
baconFile = open('.\\Chapter_8\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)