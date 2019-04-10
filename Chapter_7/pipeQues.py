#! python3
# pipeQues.py - Testing out the pipe and question mark expressions

import re
# Using | the first occurance of both search items will be returned
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman.')

print(mo1.group())
print(mo2.group())

