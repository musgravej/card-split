import PyPDF2
import os

def process(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    all_pages = set(i for i in range(0, pdfReader.numPages))
    pdf_cards_file = "{0}_CARDS.pdf".format(pdf_file[:-4])
    pdf_envelopes_file = "{0}_ENVELOPES.pdf".format(pdf_file[:-4])

    pdf_cards_pages = PyPDF2.PdfFileWriter()
    pdf_envelopes_pages = PyPDF2.PdfFileWriter()

    if not os.path.isdir(os.path.join(os.curdir, 'split')):
        os.mkdir(os.path.join(os.curdir, 'split'))

    with open(os.path.join(os.curdir, 'split', pdf_cards_file), 'wb') as save_cards:
        with open(os.path.join(os.curdir, 'split', pdf_envelopes_file), 'wb') as save_envelopes:
            for n, i in enumerate(all_pages, 0):
                if n < 1:
                    pass
                else:
                    if n % 3 != 0:
                        pdf_cards_pages.addPage(pdfReader.getPage(i))
                    else:
                        pdf_envelopes_pages.addPage(pdfReader.getPage(i))

            pdf_cards_pages.write(save_cards)
            pdf_envelopes_pages.write(save_envelopes)

    pdfFileObj.close()

def main():
    pdf_list = [f for f in os.listdir() if str(f[-3:]).upper() == 'PDF']
    for pdf in pdf_list:
        process(pdf)

if __name__ == '__main__':
    main()
