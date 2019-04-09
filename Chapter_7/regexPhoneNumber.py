#! python3
# regexPhoneNumber.py - A recreation of the isPhoneNumber.py program using regular expressions

# Importing the regex library
import re

# \d is a digit character
# Define function to do this
def phoneNumRegex(text):
    numRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = numRegex.search(text)
    numFound = mo.group()
    return numFound

# String and function call
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print('Phone number found: ' + phoneNumRegex(message))
# Need to add loop to check text for other instaces of numbers