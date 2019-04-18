#! python3
# regexStrip.py - A program that works the same as the .strip() function

# If no other arguments are passed then remove whitespaces
# Otherwise the second argument will strip whatever the user inputs

# Import libraries
import re

randomText = 'Two plus two equals four.'

# TODO: Create regex to remove whitespaces
regexSpace = re.compile(r'\s', re.DOTALL)
subText = '_'
print(regexSpace.sub(subText, randomText))

# TODO: Create function to accept user input and change regex format

# TODO: Print out resulting string