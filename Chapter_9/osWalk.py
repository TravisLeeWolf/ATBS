#! python3
# osWalk.py - Learning how to walk a directory tree

import os

for folderName, subFolders, fileNames in os.walk('S:\\Documents\\GitHub\\ATBS'):
    print('The current folder is ' + folderName)

    for subFolder in subFolders:
        print('SUBFOLER OF ' + folderName + ': ' + subFolder)
    for fileName in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + fileName)

    print('')