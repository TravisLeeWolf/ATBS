passwordFile = open('S:\Documents\GitHub\ATBS\Chapter_1\SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('Wow, such an obvious password')
else:
    print('Access denied')