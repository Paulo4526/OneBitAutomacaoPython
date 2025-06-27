import PyPDF2 as pdf

#1 - extraindo imagem de um PDF
def extract_images_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        for page_num in range(0, len(reader.pages)):
            selected_pages = reader.pages[page_num]
            print(selected_pages.images)
            for img_file in selected_pages.images:
                with open(f"files/{img_file.name}", 'wb') as out:
                    out.write(img_file.data)

extract_images_from_pdf('files/curriculo_novo.pdf')