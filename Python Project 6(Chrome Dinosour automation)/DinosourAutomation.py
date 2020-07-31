""""
Author: Bablu Bambal
Date: 29 july 2020
Description : making the dinosour of the chrome automate

Problems:
 1. Cactus Detection in the image
 2. Making the jumping when cactus is near

 Packages Required:
 pip install pyautogui  ## used to automate the click mouse and hit enter key



#plan ..
first using pill grab image and check if a black pixel is there or not then i hit up arrow key

"""

import pyautogui
import time
from PIL import Image, ImageGrab
from numpy import asarray


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # for cactus
    for i in range(160, 240):
        for j in range(395, 470):
            if data[i, j] < 100:
                hit("up")
                return

    # for birds
    for i in range(180, 210):
        for j in range(300, 395):
            if data[i, j] < 100:
                hit("down")
                return
    return


# def takeScreenshot():
#     image = ImageGrab.grab().convert('L')
#     return image

if __name__ == '__main__':
    print("Dino Game is going to start in 3 seconds")
    time.sleep(5)
    hit("up")

#     image = ImageGrab.grab().convert('L')
#     # image = takeScreenshot()
#     data = image.load()
#     # print(data)
#     # print(asarray(img))
#
#     #drawing rectangel for cactus
#     for i in range(160,240):
#         for j in range(395,470):
#             data[i, j] = 0
#     #drwaing for birdss
#     for i in range(180,210):
#         for j in range(300,395):
#             data[i, j] = 171
# ##It shows the image which is captured
#     image.show()

    # Playing game in loop
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
