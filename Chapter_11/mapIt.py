#! python3
# mapIt.py -    Get command line input or read a clipboard
#               to open up a Google Maps page for that location

# Import libraries
import webbrowser, sys, pyperclip, logging, os

# Change directory so it saves in the right folder
os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_11')

# Let's log the interaction of this program
#logging.disable()
logging.basicConfig(filename='mapItLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.debug('Start of program.')

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
    # Log: Find out what the data is in address
    logging.debug('The address variable from arguments: ' + str(address))
else:
    # Get address from clipboard
    address = pyperclip.paste()
    # Log: Find out what the data is if copied from clipboard
    logging.debug('The address variable from clipboard: ' + str(address))

# Open Google Maps using address variable
webbrowser.open('https://www.google.com/maps/place/' + address)


logging.debug('End of program.s')