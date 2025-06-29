#Iniciando WebScrapping com beatifull soup em python, instale a biblioteca com o comando "pip install beautifulsoup4"
#Importando a biblioteca beautifulsoup4
#OBS: Tenha o xml instalado com o comando "pip install lxml"
from bs4 import BeautifulSoup

#1 - Importando página HTML existente no diretório local pages
with open('pages/index.html', 'r', encoding='utf-8') as html: #Abrindo o arquivo HTML
    content = html.read() #Atribuindo os valores da página HTML para a variavel content
    soup = BeautifulSoup(content, 'lxml') #Transformando o conteúdo html em xml

#2 - Recuperando títulos dos cursos
cursos = soup.find('h6') #O comando .find(), serve para encontrar a tag h6 porém, se tiver mais que 1 ele só encontratá a primeira
print(cursos) #Mostrando a tag com seu valor
all_cursos = soup.find_all('h6') #Já o comando find_all(), encontrará todas as tags h6 existentes no arquivo HTML
for cursos in all_cursos:
    print(cursos.text) #Pegando somente o conteúdo da tag