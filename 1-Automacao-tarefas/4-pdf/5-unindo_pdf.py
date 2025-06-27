import os

import PyPDF2 as pdf

#1 - Recuperando o path de cada arquivo que contem a extensão em PDF
def fetch_all_pdf_files(parent_folder:str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder): #Aqui recuperamos o Path, os Subdiretórios se tiver, e os arquivos
        for name in files: #Iterando os arquivos encontrados
            if name.endswith('.pdf'): #Criando uma condicional para somente exibir caso a extensão seja em pdf
                print(f"Este arquivo termina com PDF: {name}")
                target_files.append(os.path.join(path, name)) #Adicionando o nome da extensão ao array target_files
    return target_files #Retornando um array com o path de cada arquivo existente

#2 - Realizando o merge entre os PDF's
def merge_pdf(list_pdf, output_filename:str): #Criando uma função que recebe uma lista de paths, e um diretório para o arquivo novo
    merger = pdf.PdfMerger() #Instanciando o PdfMErger
    with open(output_filename, 'wb') as file: #Usando o metodo open para escrever ou criar um novo arquivo
        for path in list_pdf: #Iterando os paths passados como parametro
            merger.append(path) #Recebendo cada arquivo com seus conteúdos a serem únidos e adicionando à memória do merge
        merger.write(file) #Utilizando o merge para criar um arquivo único no diretório especificado pelo file


list_file = fetch_all_pdf_files('new_files/') #Iniciando a função de recuperação de valores por uma variavel
merge_pdf(list_file, 'new_files/merged_files.pdf') #Inserindo valores da função merge