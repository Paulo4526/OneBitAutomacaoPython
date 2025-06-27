import pyautogui
import pyautogui as gui
import time

#1 - Automatizando a abertura de um aplicativo que será a calculadora
gui.press('winleft') #Pressionando a tecla windows do lado esquerdo
time.sleep(1)
pyautogui.write('calculadora') #Comando passando o que será escrito após apertar a tecla windows
time.sleep(1)
pyautogui.press('enter') #Pressionando enter para selecionar a calculadora
time.sleep(3)
gui.hotkey('alt', 'f4') #fechando o programa com o comando alt + f4
time.sleep(2)

#2 - Abrindo gerenciador de tarefas
gui.hotkey('ctrl', 'shift', 'esc')
time.sleep(3)
gui.hotkey('alt', 'f4') #fechando o programa com o comando alt + f4
time.sleep(2)

#3 - Dividindo as telas
#Descomente o código abaixo e comente os de cima para não gerar conflitos
# with gui.hold('winleft'):
#     gui.press('left')
#
# time.sleep(1)
# gui.click()
# time.sleep(2)
#
# with gui.hold('winleft'):
#     gui.press('right')