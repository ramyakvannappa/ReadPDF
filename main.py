# importing required modules
import PyPDF2
from pathlib import Path

# creating pdf file object
pdfFileObj = open('thinkstats2.pdf', 'rb')  # binary file

# creating pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# number of pages in the pdf file
print(pdfReader.numPages)

# combine the text from all the pages and save as a string
str = ""
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    text_in_page = pageObj.extractText()
    list_for_each_page = text_in_page.splitlines()
    str += text_in_page
print(str)  # extracted data is in the form of a string
print(list_for_each_page) # extracted data is in the form of a list


# writing all the read text into a file
with open("thinkstats.txt", "w",encoding = 'utf-8') as file:
    file.write(str)
