# import webbrowser 
# new = 2 # open in a new tab, if possible

# # open a public URL, in this case, the webbrowser docs
# url = "http://docs.python.org/library/webbrowser.html"
# webbrowser.get(using='google-chrome').open(url,new=new)
# import webbrowser
# import time
# #webbrowser.open("http://google.com")
# # time.sleep(5)
# webbrowser.open(url, new=0, autoraise=True)
import time
import pyautogui
time.sleep(10)
for i in range(100):
    time.sleep(1)
    pyautogui.keyDown('enter')
print("enter pressed")