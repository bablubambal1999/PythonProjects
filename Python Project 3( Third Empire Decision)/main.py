""""
Author: Bablu
Date: 28 july 2020
Purpose: Making a project with tkinter 3 umpire decisio system
"""

import tkinter
# Image Tk is used to show images into the kinter window
import PIL.Image, PIL.ImageTk  # pip install pillow
import cv2  # pip install opencv-python
# it will put argument but command things that it does't have argument
from functools import partial
import threading
# program will not termindate it will reduce the blocking nature of program
import imutils
import time

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global  flag
    print(f"you clicked on play speed is {speed}")
    #play video in the frames
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+speed)
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(140, 28, fill="green", font="Times 26 bold ", text="Decision Pending")
    flag = not flag


def pending(decision):
    # 1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("pending.jpeg"), cv2.COLOR_BGR2RGB)
    # resizing the frame
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 sec
    time.sleep(2)
    # 3. Display Sponser image
    frame = cv2.cvtColor(cv2.imread("sponsor.jpeg"), cv2.COLOR_BGR2RGB)
    # resizing the frame
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. wait for 1 sec
    time.sleep(1.5)
    # 5. Display out/notout image
    if decision == "out":
        displayimg = "out.jpeg"
    else:
        displayimg = "notout.jpeg"
    frame = cv2.cvtColor(cv2.imread(displayimg), cv2.COLOR_BGR2RGB)
    # resizing the frame
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    # 6. Wait for 1.5 sec


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out")


def notout():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is NOt out")


# frame width and height of our main screen
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter Gui starts here. tkinter is the inbuilt module
window = tkinter.Tk()
window.title("Bablu Bambal Third Umpire Decision Review Kit")

# cv2 images
cv_img = cv2.cvtColor(cv2.imread("welcome.jpeg"), cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
# showing the img into Gui

photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
# packing img on canvas
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to Control Playback:

btn = tkinter.Button(window, text="<<Previous (fast)", width=50, command=partial(play, -25))
btn.pack()
btn = tkinter.Button(window, text="<<Previous (slow)", width=50, command=partial(play, -2))
btn.pack()
btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()
btn = tkinter.Button(window, text="Next  (fast)>>", width=50, command=partial(play, 25))
btn.pack()
btn = tkinter.Button(window, text="Give OUT", width=50, command=out)
btn.pack()
btn = tkinter.Button(window, text="Give NOTOUT", width=50, command=notout)
btn.pack()

# creates a blank window
window.mainloop()
