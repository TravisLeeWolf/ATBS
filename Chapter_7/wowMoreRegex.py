#! python3
# wowMoreRegex.py - case-insensitive, substituting with sub() and more

# Check review of regex symbols for more

# Import libraries
import re

# Ignoring case for search
roboText = ['Robocop is part man, part machine, all cop.',
            'ROBOCOP protects the innocent.',
            'Al, likes robocop.']

# Create re format
robocop = re.compile(r'robocop', re.I)
for i in roboText:
    print(robocop.search(i).group())

print()

# Substitute strings with sub()
subText = 'Agent Alice gave the secret documents to Agent Bob.'
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', subText))

subText2 = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', subText2))

# Combining re.I, re.DOTALL and re.VERBOSE
# someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)