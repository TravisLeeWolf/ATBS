import os, PyPDF2

os.chdir('S:\\Documents\\GitHub\\ATBS\\Chapter_13')

pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)