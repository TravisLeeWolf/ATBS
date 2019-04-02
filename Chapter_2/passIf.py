print('What is your name?')
name = input()
if name == 'Mary':
    print('Hello Mary.')
    print('What is the password?')
    password = input()
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
else:
    print('Incorrect user.')