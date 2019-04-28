#! python3
# request1.py - Learning the request library

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
# Check to see if the download succeded
a = res.status_code == requests.codes.ok
print(a)
print(len(res.text))
print(res.text[:250])
