import pyautogui
import clipboard
import time
# -----PLEASE READ-----
# EJScreenMiner will take your coordinates and radii and reference EJScreen for data.
# SETUP: Enter variables in the VARIABLES section below.
# ONLY THREE THINGS SHOULD BE OPEN: EXCEL, PYTHON, and FIREFOX. FIREFOX must be at coordinates.
# Comments that say "location:" describes where the coordinates click. These coordinates vary from device to device
# with resolution. Replacement directions below:
# Must install pyautogui & clipboard libraries by typing "pip install pyautogui" & "pip install clipboard" into the
# terminal. EJScreen miner will not function without these libraries, which allow python to control mouse and keyboard
# and access your device's clipboard
# This code was written for a keyboard with a "fn" aug key. delete
# To replace coordinates paste the following code below into a separate script to make a coordinate locator. Place
# your mouse over the desired location and run the script. It will print the coordinates so they can be replaced.

# import pyautogui
# print(pyautogui.position())

# ----------VARIABLE DESCRIPTIONS:----------
# startAt = original excel row to start @
# counter = total number of rows to go
# coordinateColumn = column in original excel that contains coordinates. Include NS/EW for best results
# grabFromRow = EJScreen CSV row to grab from
# grabFromColumn = EJScreen CSV column
# numGrabs = (@1st line in loop) number of times to grab (goes down from first on CSV and sideways on original xlsx)
# ----------VARIABLES----------
startAtRow = 718
counter = 2
coordinateColumn = "V"
csvExcelLocations = ["F25", "F26", "F27"]
radii = ["1", "2"]
speedMultiplier = 2
# ----------PROGRAM START----------
numRadii = len(radii)
pyautogui.hotkey('alt', 'tab')

while counter > 0:
    time.sleep(.1)
    rowCounter = 0
    pyautogui.hotkey('ctrl', 'g')
    pyautogui.typewrite(str(coordinateColumn) + str(startAtRow))
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'c')  # copies coordinates
    time.sleep(.1)
    pyautogui.press('tab')
    time.sleep(.1)
    pyautogui.click(1321, 1399)  # location: firefox on taskbar
    pyautogui.hotkey('ctrl', 'r')  # refreshes firefox and resets the page
    time.sleep(10 * speedMultiplier)  # change this based on connection/browser speed
    pyautogui.press('esc')  # stops refresh in case of slow internet connection
    time.sleep(1)
    pyautogui.click(2244, 269)  # location: EJScreen Searchbar
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3 * speedMultiplier)
    for x in radii:
        pyautogui.click(1281, 831)  # location: coordinate crosshair
        time.sleep(2)
        pyautogui.click(1188, 390)  # location: radius selection box
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.5)
        pyautogui.typewrite(str(x))
        time.sleep(.5)
        pyautogui.click(1212, 474)  # location: "Explore Reports" button
        time.sleep(5 * speedMultiplier)
        pyautogui.click(633, 785)  # location: area is to small text. to make this text appear, enter .01 into radius
        pyautogui.click(633, 785)  # box in a rural area.
        pyautogui.click(633, 785)
        pyautogui.hotkey('ctrl', 'c')

        if clipboard.paste() == "The area is too small or sparsely populated to generate an EJSCREEN chart.":
            pyautogui.hotkey('alt', 'tab')
            pyautogui.typewrite('no data for this area. coordinate and remaining radii skipped.')
            pyautogui.hotkey('alt', 'tab')
            break  # skips coordinate when there is no data
        if clipboard.paste() == "Loading...Please Wait":
            pyautogui.hotkey('alt', 'tab')
            pyautogui.typewrite('long load time. coordinate and remaining radii skipped. if recurring, try increasing '
                                'time multiplier')
            pyautogui.hotkey('alt', 'tab')
            break

        pyautogui.scroll(-15000)  # scrolls down on the "Explore Reports" window
        time.sleep(.1)
        pyautogui.click(1164, 1091)  # location: "Get Data Table" button
        time.sleep(.5)
        pyautogui.click(2432, 909)  # location: download data table as CSV button (little blue thing in corner of
        # Tabular View Window)
        time.sleep(2 * speedMultiplier)
        pyautogui.press('enter')
        time.sleep(6 * speedMultiplier)
        # ----------TITLE CELL---------- (for some reason, needs to be done twice)
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')  # paste title cell
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('alt', 'tab')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')
        pyautogui.hotkey('alt', 'tab')
        time.sleep(.2)
        data = []
        for y in csvExcelLocations:
            # ----------CELLS----------
            pyautogui.hotkey('ctrl', 'g')
            pyautogui.typewrite(str(y))  # looper startpoint
            pyautogui.press('enter')
            pyautogui.hotkey('ctrl', 'c')
            data.append((clipboard.paste())[:-1])
        pyautogui.hotkey('alt', 'tab')
        for y in data:
            pyautogui.typewrite(y)
            pyautogui.press('tab')
        pyautogui.hotkey('alt', 'tab')
        # ----------LABEL MAKER----------
        # labeler runs at end of program, labeling row 1
        if (counter <= 1) and ((rowCounter + 1) == numRadii):
            pyautogui.hotkey('alt', 'tab')
            pyautogui.hotkey('ctrl', 'g')
            pyautogui.typewrite(str(coordinateColumn) + '1')
            pyautogui.press('enter')
            pyautogui.press('tab')
            for z in radii:
                pyautogui.typewrite(z + ' mile radius title cell')
                pyautogui.press('tab')
                pyautogui.hotkey('alt', 'tab')
                labels = []
                for w in csvExcelLocations:
                    pyautogui.hotkey('ctrl', 'g')
                    text1 = w[0:1]
                    pyautogui.typewrite(str(text1) + '2')
                    pyautogui.press('enter')
                    pyautogui.hotkey('ctrl', 'c')
                    titleProperty1 = (clipboard.paste())[:-1]
                    pyautogui.hotkey('ctrl', 'g')
                    text2 = w[1:]
                    pyautogui.typewrite('C' + str(text2))
                    pyautogui.press('enter')
                    pyautogui.hotkey('ctrl', 'c')
                    titleProperty2 = (clipboard.paste())[:-1]
                    label = (z + " mile radius , " + titleProperty2 + ", " + titleProperty1)
                    labels.append(label)
                pyautogui.hotkey('alt', 'tab')
                for w in labels:
                    pyautogui.typewrite(w)
                    pyautogui.press('tab')
            pyautogui.hotkey('alt', 'tab')
        # ----------END LABEL MAKER----------
        time.sleep(.2)
        rowCounter = rowCounter + 1
        pyautogui.hotkey('alt', 'fn', 'F4')  # closes excel from the ejscreen csv
        time.sleep(.2)
        pyautogui.hotkey('alt', 'tab')  # goes to Firefox
        pyautogui.click(1370, 194)  # location: "x" to close the "Explore Reports" Pop-Up
        time.sleep(.2)
    startAtRow = startAtRow + 1
    counter = counter - 1
    pyautogui.hotkey('alt', 'tab')
time.sleep(.1)
pyautogui.press('tab')
pyautogui.typewrite("Task Complete. Thank you for using EJScreenMiner, brought to you by Elijah Nicpon at NewFields.")
