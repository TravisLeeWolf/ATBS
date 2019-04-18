#! python3
# regexStrip.py - A program that works the same as the .strip() function

# If no other arguments are passed then remove whitespaces
# Otherwise the second argument will strip whatever the user inputs

# Import libraries
import re

# Function to get user input and instructions
def userInput():
    print('This fuction strips a string of text according to the users input.\n')
    print('Type in a string to be stripped:')
    userText = input()
    print('Type the phrase you want to strip: (Leave blank to strip L/R whitespaces)')
    userPhrase = input()
    if userPhrase != '':
        print('Strip ' + userPhrase)
        regexStripInput(userText, userPhrase)
    else:
        print('Strip L/R whitespaces')
        regexStripWhite(userText)

# Strips left and right white spaces
def regexStripWhite(inputText):
    regexLeft = re.compile(r'^\s+')
    leftStripped = regexLeft.sub('', inputText)
    regexRight = re.compile(r'\s+$')
    leftRightStripped = regexRight.sub('', leftStripped)
    print(leftRightStripped)

# Strips any user text
def regexStripInput(inputText, inputPhrase):
    regexUser = re.compile(inputPhrase, re.DOTALL)
    stripped = regexUser.sub('', inputText)
    print(stripped)

# Call function
userInput()