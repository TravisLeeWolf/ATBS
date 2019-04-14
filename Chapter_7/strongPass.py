#! python3
# strongPass.py - Regex check that a password is strong

# Import libraries
import re

# Eight characters long
# Both uppercase and lowercase
# At least one digit

# Use multiple regex to validate strenght

# These functions can run a search and check if .group() is True/False

# Create regex to check uppercase and lowercase
isUppercase = re.compile(r'[A-Z]+')
isLowercase = re.compile(r'[a-z]+')
isNumerical = re.compile(r'\d+')

# Get user input
def userInput():
    print('Type in a password (should be 8 characters long, both upper and lowercase with atleast one numerical):')
    userInput = input()
    checkPassword(userInput)

# Check password over regex formats 
def checkPassword(password):
    if len(password) < 8:
        print('Password length is too short.')
        userInput()
    elif isUppercase.search(password) == None:
        print('Password needs to contain uppercase characters.')
        userInput()
    elif isLowercase.search(password) == None:
        print('Password needs to contain lowercase characters.')
        userInput()
    elif isNumerical.search(password) == None:
        print('Password needs to contain a least one numerical.')
        userInput()
    else:
        print('You created a suitable password.')

# Call functions
userInput()