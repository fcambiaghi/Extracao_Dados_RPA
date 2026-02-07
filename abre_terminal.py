import pyautogui
import time

pyautogui.press('win')
time.sleep(0.5)

pyautogui.write('terminal', interval=0.1)
time.sleep(0.5)

pyautogui.press('enter')
time.sleep(3)

pyautogui.write('ipconfig', interval=0.1)
pyautogui.press('enter')
