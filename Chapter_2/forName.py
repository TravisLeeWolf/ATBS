print('Using a for loop')
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) +')')

print()
total = 0
for num in range(101):
    total = total + num
print(total)

# An equivalent while loop to the first
print()
print('Using a while loop')
print('My name is')
j = 0
while j < 5:
    print('Jimmy Five Times (' + str(j) +')')
    j = j + 1