import PyPDF2, urllib.request , nltk , textract
from io import BytesIO
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#nltk.download('stopwords')  

#Reading the PDF from web
#wFile = urllib.request.urlopen('....pdf')
#pdfreader = PyPDF2.pdf.PdfFileReader(BytesIO(wFile.read()) )

#Reading the PDF from local file
pdfFileObj = open('C:/Users/Ayegba Joshua Arome/Documents/projects/python/scrap/Grace L. Samson Research Group.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)

#extracting page 2 of the docuemnt
pageObj = pdfReader.getPage(1)
#print(pageObj.extractText())
page=pageObj.extractText()
pdfFileObj.close()

#Cleaning the text
punctuations = ['(',')',';',':','[',']',',','...','.','-','_']
tokens = word_tokenize(page)
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
print(tokens)