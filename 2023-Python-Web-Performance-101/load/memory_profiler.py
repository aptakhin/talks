from pdfquery import PDFQuery

def handle_pdf(pdf: PDFQuery) -> None:
    result = pdf.extract([
        ('texts_in_box', 'LTTextLineHorizontal:in_bbox("0,0,395,700")'),
    ])

@profile
def ram_intensive_call() -> None:
    for it in range(100):
        pdf = PDFQuery('load/sample.pdf')
        pdf.load()
        handle_pdf(pdf)

if __name__ == '__main__':
    ram_intensive_call()
