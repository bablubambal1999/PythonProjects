import pyautogui 
import time
import random
time.sleep(5)
arr = ["gud","amazing","great","mahaan","idiot","good idiot"]
print("working")
for i in range(10):
	pyautogui.typewrite(" Idiot ",interval=0.06)
        
	# pyautogui.typewrite(str(i+1)+" U are "+arr[random.randint(0,5)],interval=0.25)
	pyautogui.keyDown('enter')
print("done")

input()
