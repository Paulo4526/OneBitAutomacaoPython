import os.path

import PyPDF2 as pdf

#1 - criando a rotação dos PDF's
def rotate_pdf(pdf_path, page_num: int, rotation: int = 90):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        writer = pdf.PdfWriter()

        # Primeiro, seleciona a página do reader
        page = reader.pages[page_num]

        # Faz a rotação nela
        page.rotate(rotation)

        # Agora adiciona ao writer
        writer.add_page(page)

        # Gera o novo nome de arquivo
        filename = os.path.split(pdf_path)[1]
        new_filename = f'new_files/{filename}_page{page_num}_rotated{rotation}.pdf'

        # Salva o novo PDF
        with open(new_filename, 'wb') as out:
            writer.write(out)


rotate_pdf('new_files/merged_files.pdf', 1)