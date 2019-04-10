#! python3
# tablePrint.py - Prints a list of lists of strings in a neat table

# Table containing items
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Function to print lists in a table
def tableJustify(listItems):
    # Finds the longest string lenght in the lol strings
    stringLength = 0
    for i in range(len(listItems)):
        for j in listItems[i]:
            if stringLength < len(j):
                stringLength = len(j)
            else:
                continue
    print(stringLength)

# Call function
tableJustify(tableData)