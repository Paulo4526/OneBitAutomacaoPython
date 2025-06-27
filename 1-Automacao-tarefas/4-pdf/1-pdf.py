#Primeiramente realizar a instalação da biblioteca PDF no python com o comando "pip install PyPDF2"
#Importando a biblioteca
import PyPDF2 as pdf
from PyPDF2 import PdfReader #Para leitura do pdf

#1 - Verificando Versão e quais metodos estão disponíveis para uso no PyPDF2
print(pdf.__version__) #Para ver qual a versão do PyPDF2
print(dir(pdf)) #Mostra quais os metodos estão a disposição da nossa biblioteca

#2 - Importando arquivo PDF
file = open('files/certificado_py.pdf', 'rb') #Utilizamos o metodo open para abrir o arquivo em modo de leitura
reader = PdfReader(file) #Atribuimos a leitura do pdf para o metodo PdfReader que fará a conversão do PDF
print(reader) #Verificamos o conteúdo, que deverá ser iterado posteriormente
print(reader.metadata) #Verificamos os metadados do arquivo, como data de criação, quem criou e etc.
info = reader.metadata

#3 - Extraindo algumas informações
print(f"Título: {info.title}") #Extraindo o título do metadado caso exista
print(f"Autor: {info.author}") #Extraindo o Author caso exista
print(f"Criador: {info.creator}") #Extraindo o criador do metadado
print(f"Produtor: {info.producer}") #Extraindo o Produtor
print(f"Data de Criação: {info.creation_date}") #Extraindo a data da criação do PDF
print(f"Data de modificação: {info.modification_date}") #Extraindo a data da modificação do PDF
print(f"Assunto: {info.subject}") #Extraindo o assunto do pdf caso exista
print(f"Páginas: {len(reader.pages)}") #Verificando o tamanho de páginas existentes no nosso PDF

#4 - Extraindo o conteúdo da página sendo 0= pagina 1, 1= pagina 2 e assim sucessivamente
print(f"Conteúdo da Página: \n------Início do conteúdo ------ \n{reader.pages[0].extract_text()}--------Fim do conteúdo --------\n")
