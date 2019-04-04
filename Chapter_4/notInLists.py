# A list of our pets
myPets = ['Sam', 'Toby', 'Cookie', 'Cream']

# Checks to see if the user input is in the list
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('We do not have a pet named ' + name)
else:
    print(name + ' is our pet.')
