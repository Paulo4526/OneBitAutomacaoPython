from pathlib import Path
from datetime import datetime

#As virgulas separam cada pasta ou arquivo num diretório, tirando a obrigatoriedade de escrever o path absoluto como "files/dados/nome-arquivo.txt"
#Esta maneira facilita, pois caso não nos lembremos de como escrever o Path a própria biblioteca o faz para nós.
path = Path('files', 'dados', 'dados-novo-teste.txt')

#Lembrando também que o path fornecido acima pode não existir, então para confirmarmos podemos utilizar o path.exists
#Pois se realizarmos um print normal no path, sele somente mostrará o path que desejamos acessar.
print(path.exists())

#Aqui mostra somente os dados que introduzimos para a criação do path, ele não verifica se o pth é existente
print(path)

#Tras informações do arquivo
stats = path.stat()
#Recuperando a hora de criação do arquivo
scound_created = stats.st_ctime
#Formatando para ano, mes dia hora minutos e segundo explicação abaixo
# %Y -> Representa o ano que foi criado
# %m -> Representa o mês que foi criado
# %d -> Representa o dia que foi criado
# %H -> Representa a hora que foi criado
# %M -> Representa o minuto que foi criado
# %S -> Representa o segundo que foi criado

#OBS: Vemos abaixo que podemos mostrar o dado da maneira que quisermos contendo somente o ano, somente o dia e ano, o mes e ano, somente a hora, o minuto ou segundo
day_created = datetime.fromtimestamp(scound_created)
print(day_created.strftime('%Y-%m-%d %H:%M:%S'))
print(day_created.strftime('%Y/%m/%d'))