# The player's inventory
playerItems = {'rope': 1,
                'torch' : 6,
                'gold coin' : 42,
                'dagger' : 1,
                'arrow' : 12}

# Function to display 
def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for item in inventory:
        itemTotal = itemTotal + playerItems[item]
        print(playerItems[item], end=' ')
        print(item)
    print('Total number of items: ' + str(itemTotal))

displayInventory(playerItems)