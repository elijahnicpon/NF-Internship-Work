import pyperclip
import pyautogui
from PIL import ImageGrab
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import Image
import time
from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Listener
from pynput.mouse import Listener

# ----------------------------------------------------------------------------------------------------------------------
rows = 1100
whitelist = set('abcdefghijklmnopqrstuvwxyz ()ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.&<>/-,:#°³^%')
# whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # letters only
# whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.')  # nums and letters only
# whitelist = set('1234567890.')  # nums only
def mouseDown(x, y, button, pressed):
    if pressed:
        return
    if not pressed:
        return False

def keebPress(pressed):
    pressed = str(pressed)
    if pressed == "\'\\\\\'":
        return False
    else:
        return
# ----------------------------------------------------------------------------------------------------------------------
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
while rows > 1:
    pyautogui.click(639, 295)
    pyautogui.click(639, 295)
    pyautogui.click(1341, 276)
    pyautogui.click(639, 295)
    with keyboard.Listener(on_press=keebPress) as listener:
        listener.join()
    pyautogui.click(383, 62)
    pyautogui.hotkey('win', 'shift', 's')
    with mouse.Listener(on_click=mouseDown) as listener:
      listener.join()
    time.sleep(.5)
    img = ImageGrab.grabclipboard()
    img.save('aa.png', 'PNG')
    getImg = Image.open('aa.png')
    datum1 = tess.image_to_string(getImg)
    datum1 = datum1.replace("\n\n", ", ")
    datum1 = datum1.replace("\n", " ")
    datum1 = ''.join(filter(whitelist.__contains__, datum1))
    with keyboard.Listener(on_press=keebPress) as listener:
        listener.join()
    pyautogui.hotkey('win', 'shift', 's')
    with mouse.Listener(on_click=mouseDown) as listener:
      listener.join()
    time.sleep(1)
    img = ImageGrab.grabclipboard()
    img.save('aa.png', 'PNG')
    getImg = Image.open('aa.png')
    datum2 = tess.image_to_string(getImg)
    datum2 = datum2.replace("\n\n", ", ")
    datum2 = datum2.replace("\n", " ")
    datum2 = ''.join(filter(whitelist.__contains__, datum2))

    if datum1 == datum2:
        datum2 = "na"
    prevCache = datum2
    if prevCache == datum1:
        datum1 = "na"

    printme = (datum1 + "\t" + datum2 + "\t")
    time.sleep(.2)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.click(700, 296)
    pyautogui.typewrite(printme)
    pyautogui.scroll(-150, x=1000, y=400)
    with keyboard.Listener(on_press=keebPress) as listener:
        listener.join()
    time.sleep(1)
    rows = rows - 1
