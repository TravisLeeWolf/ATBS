print('Typing 1 prints Hello')
print('Typing 2 prints Howdy')
print('Anything else prints Greetings!')
print()
print('Type something')
spam = input()

if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings!')