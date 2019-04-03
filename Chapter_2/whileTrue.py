name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Okay ' + str(name) + ' , there will be ' + str(numOfGuests) + ' people coming!')
print('Done.')