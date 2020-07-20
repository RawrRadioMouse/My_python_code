import PyPDF2
pdfFile=open('secret.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
charset=("x","y","z","Z","1")
pwlength =6
pwlist=[]


for current in range(5):
    a = [i for i in charset]
    for n in range(current):
        a = [x+i for i in charset for x in a]
    pwlist = pwlist+a


for word in pwlist:
    if pdfReader.decrypt(word) == 1:
            print("Password is: "+ word)
