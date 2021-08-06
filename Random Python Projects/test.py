import pyperclip
import pyautogui
from PIL import ImageGrab
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
from PIL import Image
import time
from pynput import mouse
from pynput.mouse import Listener


# ----------------------------------------------------------------------------------------------------------------------
columns = 1  # number of columns//datum to copy per line
whitelist = set('abcdefghijklmnopqrstuvwxyz ()ABCDEFGHIJKLMNOPQRSTUV1234567890.&<>/-,:#ÀÁÃÂÉÊÍÓÔÕÚÜÇàáãâéêíõôóúüç°³^%')
                            # (portuguese whitelist + nums & chars)
# whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUV')  # letters only
# whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUV1234567890.')  # nums and letters only
# whitelist = set('1234567890.')  # nums only
# ----------------------------------------------------------------------------------------------------------------------
def mouseDown(x, y, button, pressed):
    if pressed:
        return
    if not pressed:
        return False
# ----------------------------------------------------------------------------------------------------------------------
pyautogui.hotkey('alt', 'tab')
data = []
while columns > 0:
    pyautogui.hotkey('win', 'shift', 's')
    with mouse.Listener(on_click=mouseDown) as listener:
      listener.join()
    time.sleep(.5)
    img = ImageGrab.grabclipboard()
    img.save('aa.png', 'PNG')
    getImg = Image.open('aa.png')
    datum = tess.image_to_string(getImg, lang='por')
    datum = ''.join(filter(whitelist.__contains__, datum))
    time.sleep(.1)
    data.append(datum)
    time.sleep(.1)
    columns = columns - 1
text = ""
for x in data:
    text = (text + x + " \t")
print(text)
pyperclip.copy(text)
