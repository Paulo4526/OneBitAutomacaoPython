#Iniciando WebScrapping com beatifull soup em python, instale a biblioteca com o comando "pip install beautifulsoup4"
#Importando a biblioteca beautifulsoup4
#OBS: Tenha o xml instalado com o comando "pip install lxml"
from bs4 import BeautifulSoup

#1 - Importando página HTML existente no diretório local pages
with open('pages/index.html', 'r', encoding='utf-8') as html: #Abrindo o arquivo HTML
    content = html.read() #Atribuindo os valores da página HTML para a variavel content
    soup = BeautifulSoup(content, 'lxml') #Transformando o conteúdo html em xml

#2 - Recuperando todas as informações com referencia em uma tag pai/mãe referenciando uma classe
card_cursos = soup.find_all('div', class_='card') #Recuperando os valores da tag div classe card
for card in card_cursos:
    print(f'\nConteúdo: {card}\n') #Recuperando e iterando todos os valores

#4 - Recuperando itens espeficos de um resultado
for curso in card_cursos:
    print('\n-----------------------------------------------------------------------')
    print(f'Curso: {curso.h6.text}') #Recuperando somente o curso
    print(f'Preço: {curso.a.text.split(" ")[-1]}') #Retornando somente o valor do curso sem as palavras anteriores
    print(f'Descrição: {curso.p.text}') #Recuperando somente a descrição resumida do curso