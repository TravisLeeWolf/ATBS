#! python3
# charClasses.py - The character classes used by the re library

# Shorthand character classes
# \d    Any numeric digit from 0 to 9
# \D    Any char that is not a numeric from 0 to 9
# \w    Any letter, numeric or underscore
# \W    Any char that is not \w
# \s    Any space, tab or \n char
# \S    Any char that is not \s

# Import re
import re

# Using these char classes to get a specialized match
xmasItems = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans'

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(xmasItems)
print('Using char classes to find specialized strings: ', end='')
print(mo)

print()

# Making your own char classes
# Finding vowels in a string
roboText = 'Robocop eats baby food. BABY FOOD.'

vowelRegex = re.compile(r'[aeiouAEIOU]') # When using [] no need for backslash
vowelNeg = re.compile(r'[^aeiouAEIOU]') # The ^ will pass a negative of the char class
mo1 = vowelRegex.findall(roboText)
mo2 = vowelNeg.findall(roboText)
print('Using custom char class to find vowels: ', end='')
print(mo1)
print()
print('Negative using ^: ', end='')
print(mo2)
