#! python3
# wildDotStar.py - Looking at the wildcard char and matching w/ dot-star

# Import libraries
import re

# . char is a wild card that matches any char except for a \n
wildText = 'The cat in the hat sat on the flat mat.'
atRegex = re.compile(r'.at')
print(atRegex.findall(wildText))
# The . char will match just one character

print()

# The .* char can be used for matching anything except \n
fullName = 'First Name: Al Last Name: Sweigart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search(fullName)
for i in mo.groups():
    print(i)

print()

# The .* char uses and greedy mode
# Using .*? uses a nongreedy mode
dinnerText = '<To serve man> for dinner.>'
# Nongreedy
nongreedyRegex = re.compile(r'<.*?>')
# Greedy
greedyRegex = re.compile(r'<.*>')

moN = nongreedyRegex.search(dinnerText)
moG = greedyRegex.search(dinnerText)

print(moN.group())
print(moG.group())

print()

# re.DOTALL matches all characters even the \n char
withNewLine = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'

# Normal .* search
noNewLineRegex = re.compile('.*')
# .* search w/ re.DOTALL
newLineRegex = re.compile('.*', re.DOTALL)

print(noNewLineRegex.search(withNewLine).group())
print(newLineRegex.search(withNewLine).group())