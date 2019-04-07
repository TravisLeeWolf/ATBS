# Write a message and create a dictionary to assign keys and values
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

# Loop to add the values to the keys
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)