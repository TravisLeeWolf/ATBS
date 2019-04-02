# This program says hello and asks for my name.
print('Hello world!')
# Ask for their name.
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
lenName = len(myName)
print('The length of your name is: ' + str(lenName))
# Ask for their age.
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
