import pdfquery

def handle_pdf(finename: str) -> None:
    for it in range(100):
        pdf = load_pdf()
        # del pdf

def ram_intensive_call() -> None:
    for it in range(100):
        handle_pdf()

if __name__ == '__main__':
    ram_intensive_call()
