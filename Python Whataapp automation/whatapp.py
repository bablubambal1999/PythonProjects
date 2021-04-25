import pyautogui 
import time
import random
import webbrowser
import keyboard
import urllib.parse
#time.sleep(5)
arr = ["919182247569","919100978738","917659922474"]
print("working")
time.sleep(2)
msg = urllib.parse.quote("Hi friends how are u all happy ram Navami to you !!")
for i in arr:
    url = f"https://api.whatsapp.com/send/?phone={i}&text={msg}"
    #webbrowser.open(url,new=0, autoraise=True)
    webbrowser.open(url)


    time.sleep(8)
    #pyautogui.keyDown('enter')
    keyboard.send('enter')
    keyboard.send("enter")
    time.sleep(2)
    print("entre clicked")
    
    # pyautogui.keyDown('enter')
    # time.sleep(2)
    print("message send to ",i)