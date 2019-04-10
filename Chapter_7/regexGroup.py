#! python3
# regexGroup.py - To test out the grouping functions of the library re

# Import re
import re

# Assign code to re
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')

# Print out the varous groupings
print('The area code is ' + mo.group(1))
print('The number without code is ' + mo.group(2))
print('The full number is ' + mo.group(0))
