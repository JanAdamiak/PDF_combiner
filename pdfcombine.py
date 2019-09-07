import os
import PyPDF2


pdf_files = [] #Create an empty list to fill with


for filename in os.listdir('C:\\Users\\Jan\\Desktop\\Statements\\.'): #Loop through files in the directory
    if filename.endswith('.pdf'): #Only select pdf files
        pdf_files.append(filename) #Add them to the list pdf_files
pdf_files.reverse() #Reverse so the last downloaded file(modified) is last page.

pdf_writer = PyPDF2.PdfFileWriter() #All files will be saved in this variable

for filename in pdf_files: #For each file in the pdf_files list.
    pdfFileObj = open(filename, 'rb') #Open the pdf in read-binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #Read the pdf file as an object.
    for page_num in range(1, pdfReader.numPages): #Cycle through the pages
        page_obj = pdfReader.getPage(page_num) #
        pdf_writer.addPage(page_obj) #Add pages to the file

pdf_final = open('C:\\Users\\Jan\\Desktop\\Statements\\Bank_Statement.pdf', 'wb') #Open the output file and write in it
pdf_writer.write(pdf_final) #Create a pdf
pdf_final.close() #Close to stop the program
