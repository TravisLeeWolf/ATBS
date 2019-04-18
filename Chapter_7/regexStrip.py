#! python3
# regexStrip.py - A program that works the same as the .strip() function

# If no other arguments are passed then remove whitespaces
# Otherwise the second argument will strip whatever the user inputs

# Import libraries
import re

# TODO: Print out resulting string

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

def regexStripWhite(inputText):
    # TODO: Regex to strip L/R whitespaces
    print('This should strip L/R whitespaces in: ' + inputText)

def regexStripInput(inputText, inputPhrase):
    # TODO: Regex to strip user phrase
    print('This should strip: ' + inputText + ' of the char: ' + inputPhrase)

# Call function
userInput()