# Function that takes list arg and prints list with commas
def listPrint(userList):
    for i in range(len(userList)):
        if i < len(userList) - 2:
            print(userList[i], end=', ', flush=True)
        elif i < len(userList) - 1:
            print(userList[i], end=' and ', flush=True)
        else:
            print(userList[i] + '.')

# Function to get user inputted list
def userInput():
    # Create empty list
    myList = []
    print('Type an item you want to add to the list (Press enter when finished).')
    userItem = input()
    while userItem != '':
        myList.append(userItem)
        print('Next item or enter to end entries.')
        userItem = input()
    else:
        listPrint(myList)

# Initiate userInput()
userInput()