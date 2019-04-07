# Using the pprint library to neaten up the output
import pprint
# Write a message and create a dictionary to assign keys and values
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# Loop to add the values to the keys
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# Now using pprint
pprint.pprint(count)

# Make into fuctions if you want to later