# Reading and Editing PDFs

import PyPDF2
import os

os.chdir('/Users/jordannewberry/Desktop')

# 'rb' means open this file in 'read-binary' mode
pdfFile = open('meetingminutes1.pdf', 'rb')

# creating a reader object
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page1 = reader.getPage(0)
print(page1.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())


# Combining
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# creating writer object to write to new PDF file
writer = PyPDF2.PdfFileWriter()

# using a for loop with range to write pages to a new PDF document
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)


for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

# Creating new blank PDF file for the writer object
outputFile = open('combinedminutes.pdf', 'wb')

# Writing the pages to the newly created file
writer.write(outputFile)

outputFile.close()
pdf1File.close()
pdf2File.close()
