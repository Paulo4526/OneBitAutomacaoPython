from time import sleep

import pyautogui as gui
import time
import os

from matplotlib.pyplot import title

pasta = 'graficos'
os.makedirs(pasta, exist_ok=True)

#1 - Abrindo o crhome
gui.press('winleft')
time.sleep(1)
gui.write('chrome')
time.sleep(1)
gui.press('enter')
time.sleep(3)

#2 - Selecionando a barra de pesquisa do chrome com o mouse para acessar o indice ibovespa
gui.moveTo(710,62, 1)
time.sleep(1)
gui.click()
time.sleep(1)
gui.write('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/') #Digitando o site
time.sleep(1)
gui.press('enter')
time.sleep(3)
gui.moveTo(242, 440, 2) #Movendo o mouse para selecionar os graficos do indice
time.sleep(1)
gui.click()
time.sleep(2)
gui.scroll(-100) #Scrolando par abaixo para tirar um print claro do indice e o grafico
time.sleep(1)
dir = os.path.join(pasta, f'indice-ibovespa-{time.time()}.png')
gui.screenshot(dir)
time.sleep(1)
