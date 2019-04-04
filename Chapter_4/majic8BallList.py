import random

# Create list
messages = ['It is certain.',
        'It is decidely so.',
        'Yes, definitley.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Concentrate and ask again.',
        'My reply is no.',
        'Outlook is not so good.',
        'Very doubtful']

# Print randomized output
print(messages[random.randint(0, len(messages) - 1)])
