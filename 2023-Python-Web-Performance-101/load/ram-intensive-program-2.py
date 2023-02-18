import gc
from pdfquery import PDFQuery

def handle_pdf(pdf: PDFQuery) -> None:
    result = pdf.extract([
        ('texts_in_box', 'LTTextLineHorizontal:in_bbox("0,0,395,700")'),
    ])
    del result

def ram_intensive_call() -> None:
    for it in range(100):
        pdf = PDFQuery('load/sample.pdf')
        pdf.load()
        handle_pdf(pdf)
        del pdf
        gc.collect()

if __name__ == '__main__':
    ram_intensive_call()
