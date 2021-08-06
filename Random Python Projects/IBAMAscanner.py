from googletrans import Translator
import pyperclip

whitelist = set('-¹²³⁴abcdefghijklmnopqrstuvwxyz ()ABCDEFGHIJKLMNOPQRSTUV1234567890.&<>/-,:#ÀÁÃÂÉÊÍÓÔÕÚÜÇàáãâéêíõôóúüç°³^%')
                            # (portuguese whitelist + nums & chars)
def hyphen_split(a):
    if a.count(" ") == 1:
        return a.split(" ")[0]
    return " ".join(a.split(" ", 2)[:2])
# for some reason ti OCRs in as a theta. this part fixes that
text = pyperclip.paste()
x = text.find('Ɵ')
while x != -1:
    text = text.replace("Ɵ", "ti")
    x = text.find('Ɵ')
# check if text is to be translated or table formatted
q = text.find("ndica")
r = text.find("ormas")
s = text.find("estri")
# check if text is to be translated or table formatted
if (q != -1) or (r != -1) or (s != -1):  # translation sequence
    text = ''.join(filter(whitelist.__contains__, text))
    translator = Translator()
    translation = translator.translate(text, dest='en')
    print(translation.text)
    pyperclip.copy(translation.text)
# check if text is to be translated or table formatted
else:  # (q == -1) or (r == -1) or (s == -1)  # formatting sequence
    array = text.split('%')
    finalArray = []
    for x in array:
        y = hyphen_split(x)
        x = x.replace(y, '')
        x = x.replace(' ', '')
        finalArray.append(y)
        finalArray.append(x)
    finalArray.append("Other ingredients")
    finalArray.append("%")
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

