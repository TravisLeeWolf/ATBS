#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#           py.exe mcb.pyw list - Loads all keywords to clipboard

# Import libraries
import shelve, pyperclip, sys

mcbShelf = shelve.open('.\\Chapter_8\\mcb')

# TODO: Save clipboard content

# TODO: List keywords and load content

# Close any open files
mcbShelf.close()