from time import sleep

import pyautogui as gui
import time
import os

#Criando as variaveis
pasta = 'prints'
os.makedirs(pasta, exist_ok=True) #Não cria outra pasta caso já exista uma no diretório

#1 - Realizando o screenshot
dir1 = os.path.join(pasta, f'exemplo_{time.time()}.png')
gui.screenshot(dir1) #Criando um screenshot e salvando no diretório do arquivo rodado
time.sleep(2)

#2 - Utilizando mouse para ações + screenshoot
#Minimizando a tela inicio
gui.moveTo(1238, 10, 2)
time.sleep(1)
gui.click()
time.sleep(1)
dir2 = os.path.join(pasta, f'print_{time.time()}.png')
gui.screenshot(dir2)
#Minimizando fin
time.sleep(2)
#Voltando a tela inicio partindo do pressuposto que somente a minha IDE pycharm está aberta
with gui.hold('alt'):
    time.sleep(1)
    gui.hotkey('tab')
#Voltando a tela fim


