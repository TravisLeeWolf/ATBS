#! python3
# shelveVar.py - Using the shelve module to save variables

# Import libraries
import os, shelve

# Create myData in Chapter_8
# Change directory to Chapter_8
os.chdir('.\\Chapter_8')

shelfFile = shelve.open('myData')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()