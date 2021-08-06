import clipboard
from PIL import ImageGrab
import pyautogui
import time
import pygame
import pytesseract
import csv

im = ImageGrab.grabclipboard()
numColumns = 3  # number of iterations it will run, and cells it will create
pyautogui.hotkey('alt', 'tab')
data = []
for x in numColumns:
    pyautogui.hotkey('win' + 'shift' + 's')
    # -----this code has us wait for a mouse click
    copied = False
    while not copied:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP:
            im.save('tempPic.png', 'PNG')
            datum = (pytesseract.image_to_string(im.open('tempPic.png')))
            data.append(datum)
            time.sleep(.1)
            copied = True
print(data)
clipboard.copy()
