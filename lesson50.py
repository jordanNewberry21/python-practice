# Screenshots and image recognition

import pyautogui

pyautogui.screenshot('/Users/jordannewberry/Desktop/screenshot_example.png')

print(pyautogui.locateOnScreen('/Users/jordannewberry/Desktop/screenshot_1.png', grayscale=True, confidence=.5))

