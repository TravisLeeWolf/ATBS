# Importing the random module
import random
for i in range(5):
    print(random.randint(1,10))

# Importing sys to exit a program
print()
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')