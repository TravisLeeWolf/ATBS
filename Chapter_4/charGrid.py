def showGrid(dispGrid):
    i =0
    if i < (len(dispGrid)):
        j = 0
        while j < (len(dispGrid[i])):
            print(dispGrid[i][j], end='')
            j =+ 1
        i =+ 1
    else:
        print()


heart = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

showGrid(heart)