#! python3
# tracebackExample.py - More traceback learning

import traceback, os

os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_10')

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
