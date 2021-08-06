import pyautogui
import time
# -----PLEASE READ----- SETUP: ONLY THREE THINGS OPEN: EXCEL, PYTHON, and FIREFOX. FIREFOX must be at coordinates.
# Comments that say "location:" describes where the coordinates click. These coordinates vary from device to device
# with resolution. Replacement directions below:

# To replace coordinates paste the following code below into a separate script to make a coordinate locator. Place your mouse over the desired location and run the script. It will print the coordinates so they can be replaced.

# import pyautogui
print(pyautogui.position())

# ----------VARIABLE DESCRIPTIONS:----------
# startAt = original excel row to start @
# counter = total number of rows to go
# coordinateColumn = column in original excel that contains coordinates
# titleCellColumn = column title cell will be pasted in; all other attributes pasted to right
# grabFromRow = EJScreen CSV row to grab from
# grabFromColumn = EJScreen CSV column
# numGrabs = (@1st line in loop) number of times to grab (goes down from first on CSV and sideways on original xlsx)
# ----------VARIABLES----------
startAt = 2
counter = 3000
coordinateColumn = "E"
titleCellColumn = "F"
grabFromColumn = "F"
grabFromRow = 25
# NUM GRABS IS IN THE WHILE LOOP!!!
# ----------PROGRAM START----------
# pyautogui.hotkey('alt', 'tab')
while counter < 0:
    numGrabs = 3
    pyautogui.hotkey('ctrl', 'g')
    pyautogui.typewrite(str(coordinateColumn)+str(startAt))
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1321, 1399)
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(14)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.click(2244, 269)
    pyautogui.click(2244, 269)
    pyautogui.click(2244, 269)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(1281, 831)
    time.sleep(1)
    pyautogui.click(1212, 474)
    time.sleep(5)
    pyautogui.scroll(500)
    pyautogui.scroll(500)
    pyautogui.scroll(500)
    pyautogui.click(1138, 1058)
    time.sleep(.5)
    pyautogui.click(2432, 909)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    # ----------TITLE CELL----------
    pyautogui.hotkey('ctrl', 'g')
    pyautogui.typewrite('A1')  # title cell select
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')  # paste title cell
    pyautogui.hotkey('alt', 'tab')
    # ----------FIRST CELL----------
    if numGrabs > 0:
        pyautogui.hotkey('ctrl', 'g')
        pyautogui.typewrite(str(grabFromColumn) + str(grabFromRow))  # looper startpoint
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        # ----------EVERY CELL AFTER FIRST----------
        while (numGrabs - 1) > 0:  # back and forth looper
            pyautogui.press('enter')  # down a row on Excel from CSV
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.hotkey('alt', 'tab')
            pyautogui.press('tab')  # right on column on original Excel
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('alt', 'tab')
            numGrabs = numGrabs - 1
    pyautogui.hotkey('alt', 'fn', 'F4')  # closes excel from the ejscreen csv
    pyautogui.hotkey('alt', 'tab')  # goes to Firefox
    pyautogui.click(1338, 194)  # location: "x" to close the "Explore Reports" Pop-Up
    time.sleep(.2)
    pyautogui.click(1179, 399)  # location:
    pyautogui.press('backspace')
    pyautogui.click('2')
    pyautogui.click(1189, 483)
    time.sleep(5)
    pyautogui.scroll(500)
    pyautogui.scroll(500)
    pyautogui.scroll(500)
    pyautogui.click(1132, 1052)
    time.sleep(.2)
    pyautogui.click(2428, 908)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    # ----------TITLE CELL----------
    pyautogui.hotkey('ctrl', 'g')
    pyautogui.typewrite('A1')  # title cell select
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')  # paste title cell
    pyautogui.hotkey('alt', 'tab')
    # ----------FIRST CELL----------
    if numGrabs > 0:
        pyautogui.hotkey('ctrl', 'g')
        pyautogui.typewrite(str(grabFromColumn) + str(grabFromRow))  # looper startpoint
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        # ----------EVERY CELL AFTER FIRST----------
        while (numGrabs - 1) > 0:  # back and forth looper
            pyautogui.press('enter')  # down a row on Excel from CSV
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.hotkey('alt', 'tab')
            pyautogui.press('tab')  # right on column on original Excel
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('alt', 'tab')
            numGrabs = numGrabs - 1
    pyautogui.hotkey('alt', 'fn', 'F4')  # closes excel from the ejscreen csv
    counter = counter - 1
    startAt = startAt + 1
time.sleep(.1)
