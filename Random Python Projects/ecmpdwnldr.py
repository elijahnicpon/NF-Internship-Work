import pyautogui
import time






import pyperclip

# 75% chrome 2k monitor;
# start at 4/29/2021 compliance
# oneIsDownload = [1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

pyautogui.hotkey('alt', 'tab')
print(pyautogui.position())
time.sleep(0.5)
counter = 60
while counter > 0:
    pyautogui.moveTo(911, 180)
    time.sleep(.1)
    pyautogui.scroll(-35)
    time.sleep(.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(1410, 180)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.mouseUp()
    time.sleep(.1)
    txt = pyperclip.paste()
    index1 = txt.find("VIDEO")
    index2 = txt.find("RECEIPT")
    if (index1 != -1) | (index2 != -1):
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(.2)
    else:
        time.sleep(45)
        pyautogui.click(2335, 232)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.press('enter')
        pyautogui.press('esc')
        time.sleep(.1)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(.2)
