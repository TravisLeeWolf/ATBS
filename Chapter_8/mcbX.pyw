#! python3
# mcbX.pyw - Saves and loads pieces of text to the clipboard.
# Usage:    py.exe mcbX.pyw save <keyword> - Saves clipboard to keyword
#           py.exe mcbX.pyw <keyword> - Loads keyword to clipboard
#           py.exe mcbX.pyw list - Loads all keywords to clipboard

# Import libraries
import shelve, pyperclip, sys

mcbShelfX = shelve.open('.\\Chapter_8\\mcbX')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mcbShelfX[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelfX.keys())))
    elif sys.argv[1] in mcbShelfX:
        pyperclip.copy(mcbShelfX[sys.argv[1]])

# TODO: Add a delete function

# Close any open files
mcbShelfX.close()
