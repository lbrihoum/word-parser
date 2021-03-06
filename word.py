# Word Parser
# April 10, 2020

# Importing required modules
import PyPDF2

# Creating a pdf file object
pdfFileObj = open("thinkpython.pdf", 'rb') # rb stands for read, if I wanted to write I would put "wb"

# Creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Printing number of pages in pdf file
print(pdfReader.numPages)

# Creating a page objext
pageObj = pdfReader.getPage(0)

# Extracting text from page
# MOST IMPORTANT PART
print(pageObj.extractText())

# Closing the pdf file objext
pdfFileObj.close()
