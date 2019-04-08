# Using justifcation on strings
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

# Create picnic dictionary
picnicItems = {'sandwiches' : 4,
                'apples' : 12,
                'cups' : 4,
                'cookies' : 800}

# Call function and pass dictionary and widths
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)