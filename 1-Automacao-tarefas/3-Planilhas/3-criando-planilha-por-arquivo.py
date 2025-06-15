#Aqui aprenderemos a criar uma planilha a partir de um arquivo de texto(arquivo que foi criado na pasta files 'arquivo.txt').
from openpyxl import Workbook

print('Lendo dados a partir de um arquivo de texto')
#1 - Inicializando o Workbook
wb = Workbook()
ws = wb.active

#2 - Recuperando as informações do arquivo
file_txt = open('files/arquivo.txt', 'r', encoding='utf-8').read()
list_data = file_txt.splitlines() #Transformando os dados em um Array(Lista) com o comando split lines, ou seja ele irá transformar em 1 item somente o valor de uma lista

#3 - Iterando os valores da lista
for i in range(0, len(list_data)):
    new_list = list_data[i].split(',') #Aqui transformamos um item de uma lista em 1 array e adicionamos a nossa planilha
    ws.append(new_list)


#4 - Criando a planilha
wb.save('files/gastos.xlsx')#Salvando o arquivo como gastos.xlsx na pasta files