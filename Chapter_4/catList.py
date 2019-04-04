# Create an empty list
catNames = []

# Create a loop for entry into the list
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # List concatenation

# Prints out the current list of cat names
print('The cat names are: ')
for name in catNames:
    print('   ' + name)
