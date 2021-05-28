# Controlling the keyboard with Python

import pyautogui

print(pyautogui.position())

# pyautogui.click(382, 402); pyautogui.typewrite('Hello world!', interval=0.2)

pyautogui.press('return')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('return')
pyautogui.press('return')

print(pyautogui.KEYBOARD_KEYS())

