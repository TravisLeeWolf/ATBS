# Function to add looted inventory to player inventory
def addToInventory(inventory, addedItems):
    for loot in addedItems:
        if loot in inventory:
            inventory[loot] = inventory[loot] + 1
        else:
            inventory.setdefault(loot, 1)
    return inventory

# Function to display inventory
def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for item in inventory:
        itemTotal = itemTotal + inventory[item]
        print(inventory[item], end=' ')
        print(item)
    print('Total number of items: ' + str(itemTotal))

# Player's inventory
playerInventory = {'gold coin' : 42,
                    'rope' : 1}
# Dragon's inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Call functions
playerInventory = addToInventory(playerInventory, dragonLoot)
displayInventory(playerInventory)