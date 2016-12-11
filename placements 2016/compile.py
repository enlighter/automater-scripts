import textract

def compile_day_wise():

    for day in range(1,20):
        main_file = "Day %s.pdf"%(day)
        adjunct_file = "Day %s additional"%(day)

        try:
            main_text = textract.process(main_file)
        except:
            break

        try:
            adjunct_text = textract.process(adjunct_file)
        except:
            adjunct_text = None
            continue

        print(main_text)

        # with open(main_file,'rb') as pdfFileObj:
        #     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #     pageObj = pdfReader.getPage(0)
        #     print(pageObj.extractText())


if __name__ == '__main__':
    compile_day_wise()