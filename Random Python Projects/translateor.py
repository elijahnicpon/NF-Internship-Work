import pyperclip

def hyphen_split(a):
    if a.count(" ") == 1:
        return a.split(" ")[0]
    return " ".join(a.split(" ", 2)[:2])

text = pyperclip.paste()
x = text.find('Ɵ')
while x != -1:
    text = text.replace("Ɵ", "ti")
    x = text.find('Ɵ')

array = text.split('%')
finalArray = []
for x in array:
    y = hyphen_split(x)
    x = x.replace(y, '')
    x = x.replace(' ', '')
    finalArray.append(y)
    finalArray.append(x)
counter = 0
finalString = ""
for z in finalArray:
    if (counter % 2) == 0:
        finalString += z
        finalString += "\t"
    if (counter % 2) == 1:
        finalString += z
        finalString += "%\n"
    counter = counter + 1
pyperclip.copy(finalString)
print(finalArray)

