#! python3
# savingPretty.py - Using the pprint library to save files

# Import libraries
import pprint, os, sys

cats = [{'name' : 'Zophie', 'desc' : 'chubby'},
        {'name' : 'Pooka', 'desc' : 'fluffy'}]

# Write to file
fileObj = open('.\\Chapter_8\\hisCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')

# Close the file
fileObj.close()