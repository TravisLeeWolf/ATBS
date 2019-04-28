#! python3
# request2.py - Working with raise for status

import requests

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

# To check if there is an error in downloading the page
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Always call raise_for_status() after calling requests.get()
# You want to be sure that the download as worked before running more code
