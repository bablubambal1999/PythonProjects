# install pillow into the system
from PIL import Image,ImageGrab
import time

def takeScreenshot():
    image = ImageGrab.grab()
    image.show()

if __name__ == '__main__':
    time.sleep(4)
    takeScreenshot()