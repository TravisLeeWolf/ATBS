#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# Paste text from the clipboard
import pyperclip
text = pyperclip.paste()

# Separate lines and add * to it
lines = text.split('\n')
for i in range(len(lines)): # Loop through all the indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  # Add a star to each string
text = '\n'.join(lines)

# Copy the new text to the clipboard
pyperclip.copy(text)