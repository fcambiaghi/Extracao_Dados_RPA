import pyautogui
 
import time
time.sleep(2)

box_icon = pyautogui.locateOnScreen("C:\\Temp\\Extracao_Dados_RPA-1\\LogoGitHub.png", confidence=0.7)
if box_icon:
    x, y = pyautogui.center(box_icon)
    print(f'posicao: X:{x} Y:{y}')
    pyautogui.click(x,y)
else:
    print("Ícone não encontrado")