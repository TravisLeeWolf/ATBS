#! python3
# yetMoreRegex.py - Looking at caret and dollar sign chars and more

# Import libraries
import re

# Using ^ at the beginning for begins with match
helloText = ['Hello world!', 'He said hello.']
beginsWithHello = re.compile(r'^Hello')
for i in helloText:
    print(beginsWithHello.search(i))

print()

# Using $ at the end for ends with match
endsNum = ['Your number is 42', 'Your number is forty two.']
endsWithNumber = re.compile(r'\d$')
for j in endsNum:
    print(endsWithNumber.search(j))

print()

# Using both ^ and $ to get a match that begin and end with search char
bothNum = ['1234567890', '12345xzy67890','12 34567890']
wholeStringIsNum = re.compile(r'^\d+$')
for k in bothNum:
    print(wholeStringIsNum.search(k))
