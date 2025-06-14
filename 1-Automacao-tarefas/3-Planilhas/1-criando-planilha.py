#Criando a primeira planilha após instalar a biblioteca openpyxl comando 'pip install openpyxl'
#Instalar no pycharm o ExcelReader em plugins

from openpyxl import Workbook

#1 - Criando o workbook(planilha em excel)
wb = Workbook()
file_name = 'files/teste.xlsx'

#2 - Utilizando o Worksheet(Planilha)
ws1 = wb.active
ws1.title = 'Planilha 1' #alterando nome da planilha

#3 - adicionando os dados
data = [
    ['Ano', 'Lucro', 'Custos'],
    [2021, '25%', '40%'],
    [2022, '45%', '50%'],
    [2023, '15%', '10%']
]

for line in data:
    ws1.append(line)

#4 - Criando nova planilha
ws2 = wb.create_sheet(title='Funcionarios')
func = [
    ["Nome", "Função", 'Valor Diaria'],
    ["Paulo Bueno", "Eletricista", 150],
    ["Fabio Bueno", "Bartenteder", 150],
    ["Ana Bunker", "Assistente de Bar", 100]
]
count = 1
for line in func:
    ws2.append(line)

wb.save(filename=file_name) #Salvando o arquivo