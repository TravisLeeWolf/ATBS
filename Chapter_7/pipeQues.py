#! python3
# pipeQues.py - Testing out the pipe and question mark expressions

import re
# Using | the first occurance of both search items will be returned
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

print(mo1.group())
print(mo2.group())
print()

# Matching using a prefix
batRegex = re.compile(r'Bat(man|mobile|copter)')
mo = batRegex.search('The Batmobile lost a wheel.')

print(mo.group())
print('Bat is the prefix, the later half is ' + mo.group(1))
print()

# Optional matching with the question mark
batGenderRegex = re.compile(r'Bat(wo)?man')
mo3 = batGenderRegex.search('The Adventures of Batman.')
mo4 = batGenderRegex.search('The Adventures of Batwoman.')

print(mo3.group())
print(mo4.group())
