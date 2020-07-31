# automatic install the python

import pyautogui
import time

stri = "Hi  😁😁😁😁 "
time.sleep(5)
for i in range(3):
    pyautogui.write(stri,interval=0.25)
    pyautogui.press('enter')


pyautogui.write(stri)
pyautogui.press('enter')
