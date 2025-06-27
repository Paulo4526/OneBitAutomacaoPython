#Primeiramente precisamos baixar a biblioteca de automações como o mouse e teclado com o comando "pip install pyautogui"
import pyautogui
import time

#1 - Obtendo tamanho da tela
print(pyautogui.size()) #Retorna a resolução da tela do computador atual

#2 - Obtendo a posição atual do cursor
print(pyautogui.position())

#3 - App para ver a posição do mouse em tempo real
#No terminal digitar os seguintes comandos:
#3.1 - python
#3.2 - from pyautogui import mouseInfo
#3.3 - mouseInfo()
#3.4 - Note que após as ações acima será aberto uma janela com as informações do mouse como posição, cor do objeto em que o mouse está encima e etc e etc.

#4 - Mover o cursor do mouse com a função moveTo
#Após utilizarmos o mouseInfo, coloque o mouse encima de onde quer clicar e pegue os valores descritos no "XY Position",
#esse comando moverá nosso mouse para  aposição selecionada
#OBS: O parametro duration que é o ultimo dentro do moveTo, configura a duração do movimento até o local, asism podendo ser visto o cursor se mover até o local
pyautogui.moveTo(1238, 10, 2) #Comando moveTo com os valores descritos dentro do XY Position, que será na barra de minimizar a IDE Pycharm
time.sleep(2.5) #Adicionando o time para que seja pausado o comando por 2.5s e vermos que o mouse foi para o local indicado e depois do tempo será feito o click
pyautogui.click() #Comando para que seja feito o click e minimize a IDE PyCharm
#Note que ao executar o script o cursor so mouse se moverá até o ponto que escolhermos dentro do mouseInfo e fará o click

#5 - Utilizando o scroll
time.sleep(1.5)
pyautogui.moveTo(700, 400, 1.5) #Centralizando o mouse
time.sleep(1)
pyautogui.scroll(-900) #Fazendo o scroll para baixo sentido final do conteúdo, caso positivo o número ele ira rolar para cima sentido início do conteúdo