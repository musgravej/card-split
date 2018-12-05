import PyPDF2
import time
import os

def process_special(pdf_file, start_rec=1):
    """
    Substitutes art in first page of the card with 
        I:\\Customer Files\\In Progress\\GO Monthly Web Orders\\
        32248 GO Dec 2018 Web Orders\\CARD_HolidayCard_MerryChristmas_FPCoverCX.pdf
    Defaults as pdf with no header page
    """
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    insertPdf = PyPDF2.PdfFileReader(("I:\\Customer Files\\In Progress\\GO Monthly Web Orders\\"
                                     "32248 GO Dec 2018 Web Orders\\"
                                     "CARD_HolidayCard_MerryChristmas_FPCoverCX.pdf"))

    all_pages = set(i for i in range(0, pdfReader.numPages))
    pdf_cards_file = "{0}_CARDS.pdf".format(pdf_file[:-4])
    pdf_envelopes_file = "{0}_ENVELOPES.pdf".format(pdf_file[:-4])

    pdf_cards_pages = PyPDF2.PdfFileWriter()
    pdf_envelopes_pages = PyPDF2.PdfFileWriter()

    if not os.path.isdir(os.path.join(os.curdir, 'split_replace')):
        os.mkdir(os.path.join(os.curdir, 'split_replace'))

    with open(os.path.join(os.curdir, 'split_replace', pdf_cards_file), 'wb') as save_cards:
        with open(os.path.join(os.curdir, 'split_replace', pdf_envelopes_file), 'wb') as save_envelopes:
            for n, i in enumerate(all_pages, start_rec):
                if n < 1:
                    pass
                else:
                    if n % 3 == 1:
                        pass
                    if n % 3 == 2:
                        pdf_cards_pages.addPage(insertPdf.getPage(0))
                        pdf_cards_pages.addPage(pdfReader.getPage(i))
                    if n % 3 == 0:
                        pdf_envelopes_pages.addPage(pdfReader.getPage(i))

            pdf_cards_pages.write(save_cards)
            pdf_envelopes_pages.write(save_envelopes)

    pdfFileObj.close()


def process(pdf_file, start_rec=1):
    """Defaults as pdf with no header page"""
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
            for n, i in enumerate(all_pages, start_rec):
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


def question():
    ans = int(input("PDF contains cover page to skip (0 yes / 1 no): "))
    if TypeError:
        print("Error, invalid response")
        time.sleep(3)
        os.exit()

    if ans not in {0, 1}:
        print("Error, invalid response")
        time.sleep(3)
        os.exit()

    return ans

def main():
    start_rec = question()
    pdf_list = [f for f in os.listdir() if str(f[-3:]).upper() == 'PDF']
    for pdf in pdf_list:
        # process(pdf, start_rec)
        process_special(pdf, start_rec)

if __name__ == '__main__':
    main()
