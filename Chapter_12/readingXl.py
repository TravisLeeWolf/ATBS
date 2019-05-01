#! python3
# readingXl.py - Learning how to use the openpyxl library

# Import libraries
import os, openpyxl

os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_12')

# Now accessing the excel workbook
wb = openpyxl.load_workbook('example.xlsx')
# File needs to be in current working directory to run this function
print(type(wb))

# Getting sheets from workbook
print(wb.sheetnames)

sheet = wb['Sheet3']
print(sheet)
print(type(sheet))
print(sheet.title)

anotherSheet = wb.active
print(anotherSheet)