import PyPDF2 as pdf

#1 - Criando uma função para leitura do pdf
def get_pdf_metadata(pdf_path): #Função que recebe o path do arquivo como parametro
    with open(pdf_path, 'rb') as file: #Utilizando o metodo open informando o path
        reader = pdf.PdfReader(file)
        info = reader.metadata
    return info

#2 - Função para extração dos arquivos
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file) #Utilizando o metodo PdfReader para leitura dos dados do PDF
        result = [] #Criando um array para receber os valores de cada PDF
        for i in range(0, len(reader.pages)): #Iterando cada página para que após a leitura do conteúdo, esse conteúdo seja adicionado ao nosso array
            selected_page = reader.pages[i].extract_text()
            result.append(selected_page)
        return ''.join(result) #Retornando o valor de results juntamente a string vazia que servirá de espaçamento

print(get_pdf_metadata('files/certificado_py.pdf'))
print(extract_text_from_pdf('files/certificado_py.pdf'))
print(extract_text_from_pdf('files/curriculo_novo.pdf'))