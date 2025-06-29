#Iniciando WebScrapping com beatifull soup em python, instale a biblioteca com o comando "pip install beautifulsoup4"
#Importando a biblioteca beautifulsoup4
#OBS: Tenha o xml instalado com o comando "pip install lxml"
from bs4 import BeautifulSoup

#1 - Importando página HTML existente no diretório local pages
with open('pages/index.html', 'r', encoding='utf-8') as html: #Abrindo o arquivo HTML
    content = html.read() #Atribuindo os valores da página HTML para a variavel content
    print(content) # Mostrando o conteúdo atribuido para o content
    soup = BeautifulSoup(content, 'lxml') #Transformando o conteúdo html em xml
    print('\n------------------------------- XML ABAIXO -------------------------------\n')
    print(soup.prettify())

