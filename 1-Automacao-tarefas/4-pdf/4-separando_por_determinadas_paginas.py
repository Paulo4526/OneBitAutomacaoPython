import os.path

import PyPDF2 as pdf

#1 - Criando um PDF a cada página de um PDF referenciado
def split_pdf(pdf_path, inicio_page:int=0, fim_page:int=0):
    with (open(pdf_path, 'rb') as file):
        reader = pdf.PdfReader(file)
        for page_num in range(inicio_page, fim_page):
            selected_page = reader.pages[page_num] #Iterando as paginas
            writer = pdf.PdfWriter()
            writer.add_page(selected_page) #Selecionando o metodo PdfWriter para escrever um novo pdf
            print(os.path.split(pdf_path)[1]) #Recuperando o path para alterarmos somente o nome do arquivo
            new_filename = f'new_files/nova_page_{page_num+1}.pdf' #Criando um novo nome de arquivo com o nome e o número da página
            with open(new_filename, 'wb') as out:
                writer.write(out)
            print(f"Pdf criado com o nome: {new_filename}")

split_pdf('files/curriculo_novo.pdf', 1, 2)

