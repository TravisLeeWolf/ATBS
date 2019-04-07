birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Gets user to enter in new persons name
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    print('To stop type q')
    stop = input()
    if stop == 'q':
        break

# Checks dictionary if no name is entered asks for birthdate
if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')