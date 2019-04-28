#! python3
# requestWrite.py - Writing the downloaded page to a file

# Import libraries
import requests, os

os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_11')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()