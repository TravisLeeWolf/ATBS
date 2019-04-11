#! python3
# regexFindAll.py - Understanding how the findall() function works

# Import re
import re

# String for search() and findall() functions to use
myNumbers = 'Cell: 415-555-9999 Work: 212-555-0000'

# Create the regex format
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# Using search() only brings up the first instance
mo = phoneNumRegex.search(myNumbers)
print('Using the search() function: ' + mo.group())

# Using findall() returns a list of matching items
mo1 = phoneNumRegex.findall(myNumbers)
# Returns a list
print('Using the findall() function: ', end='')
print(mo1)

# findall() with groups in the regex returns a tuple of the found items
groupNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = groupNumRegex.findall(myNumbers)
# Returns a tuple
print('Using findall() with groups in regex: ', end='')
print(mo2)