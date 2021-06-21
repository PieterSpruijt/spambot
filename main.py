import pyautogui
import webbrowser as wb
import time
time.sleep(5)
pyautogui.write('**PIETER SPRUIJT**', interval=0.02)
pyautogui.press('enter')
pyautogui.write('https://github.com/PieterSpruijt/', interval=0.02)
pyautogui.press('enter')
pyautogui.press('enter')
for i in range(1000):
    pyautogui.write('SPAM', interval=0.01)
    pyautogui.press("enter")