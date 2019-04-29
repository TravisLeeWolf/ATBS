#! python3
# exampleSelect.py - Using the BS select function

# Import libraries
import bs4, os

os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_11')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')

print(type(elems))
print(len(elems))
print(type(elems[0]))

elems[0].getText()
print(str(elems[0]))
print(elems[0].attrs)