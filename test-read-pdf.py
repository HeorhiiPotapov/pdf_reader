"""This scrypt can read and output pdf's enternal text.
   run this command in active virtualenv to install 
   required dependencies 'pip install PyPDF2'
"""

if __name__ == "__main__":
    #import reader class from installed lib
    from PyPDF2 import PdfFileReader

    #Define path to PDF file
    pdf_file_name = 'test.pdf'
    # open and read bytes from a target pdf file
    with open(pdf_file_name, 'rb') as pdf_file:
        #point imported reader to readed data from a file
        pdf_reader = PdfFileReader(pdf_file)

        #Get number of pages in the PDF file
        page_nums = pdf_reader.numPages

        #Iterate over each page number
        for page_num in range(page_nums):
            
            #Read the given PDF file page
            page = pdf_reader.getPage(page_num)
            
            #extract text from a page
            text = page.extractText()
            
        #finally print text
        print(text)
