#! python3
# usingBS4.py - Learning how to access HTML with Beautiful Soup

# Import libraries
import requests, bs4, os

# Change dir to working dir
os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_11')

# Get the website data
res = requests.get('http://nostarch.com')
res.raise_for_status()

# Run res data through BS function
noStarchSoup = bs4.BeautifulSoup(res.text)
print('From website:')
print(type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print('From file:')
print(type(exampleSoup))