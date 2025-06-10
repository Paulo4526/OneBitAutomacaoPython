#Importando a biblioteca Path que faz parte do pacote pathlib
from pathlib import Path

#Acessando a pasta dados, e selecionando o arquivo.txt
p1 = Path('files/dados', 'teste.txt') #Primeiro parametro o diretório, segundo o arquivo a ser selecionado
print(p1) #Caso retorne o caminho, significa que foi recinhecido o arquivo
print(type(p1)) #Aqui retorna o tipo de arquivo
print(p1.name) #Aqui retorna o nome do arquivo
print(p1.stem) #Demonstra o nome do arquivo sem o seu sufixo(txt, jpg, jpeg, py, java entre outros)
print(p1.suffix) #Retorna somente o valor do sufixo do arquivo(txt. jpeg, jpg, java entre outros)
print(p1.exists()) #Retorna se o arquivo existe

#Realiza a verificação se o arquivo existe
if p1.exists():
    #Aqui como utilizado no módulo de leitura e escrita de arquivos, utilizamos o with open para ler o arquivo
    with open(p1, 'r', encoding='utf-8') as file:
        print(file.read())

#Iterando com a pasta para saber quais arquivos existem dentro do diretório
p2 = Path('files/dados') # Para isso passamos somente o parametro do path do diretório
print(list(p2.iterdir())) #Aqui utilizamos uma lista e o metodo de iteração com o diretório iterdir

