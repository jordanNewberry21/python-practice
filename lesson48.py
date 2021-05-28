#!/usr/bin/env python3

# Controlling the mouse from Python
# using PyAutoGUI to programmatically control mouse and keyboard
# GUI stands for Graphical User Interface

import pyautogui

# pyautogui.size()

# width, height = pyautogui.size()

# print(width, height)

# print(pyautogui.position())

pyautogui.moveTo(150, 100, duration=3)

pyautogui.moveRel(200, 35, duration=2)

pyautogui.moveRel(200, -100, duration=2)

pyautogui.click(811, 172)

pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()

pyautogui.displayMousePosition()




